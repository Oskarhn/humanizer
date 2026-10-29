"""Optional offline NorBERT measurement/search helper. Python 3.10+.

No downloads, LLM calls or text generation. Supply your own reviewed alternatives.
The external cleaner is hash-verified and only applied to model input, never output.
Detector scores are not evidence of authorship or preservation of meaning.
"""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
import hashlib
import json
import math
import os
from pathlib import Path
import re
import sys
import tempfile
from typing import Any

MODEL_REPO = "pegesund/norwegian-ai-detector"
REVISION = "0df563e67066e1eadd08eaceac80f1db4ed71f90"
PINNED = {
    "onnx/detector_int8.onnx": "7a4096d8a720129520d0fb90792aee5ff27cc88e23039199aa93ed399ed338e7",
    "tokenizer.json": "5c1c0abf91d5944d039872765d7b36c889640ceb5b99ebc601d02873cfbcb600",
    "clean_text.py": "cbc68efcaeae508f7478030f6bd5bc4ba4989e6486e6c86e78b8f199d5589582",
}
MAX_TOKENS = 1024
MAX_INPUT_BYTES = 16 * 1024 * 1024
MAX_TEXT_CHARS = 1_000_000
NORWEGIAN = {"no", "nb", "nn", "norwegian", "bokmål", "nynorsk"}
FIDELITY = "NOT_PERFORMED_BY_SCRIPT"


class InputError(ValueError):
    pass


class TooLong(InputError):
    pass


class BudgetExhausted(Exception):
    pass


class ReferenceBudgetExhausted(BudgetExhausted):
    pass


def text_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def file_hash(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_pinned_cleaner(path: Path):
    # ASVS 15.2.4: execute only the exact verified source bytes, never cached .pyc
    # or packet text. Reusing these bytes also avoids a hash-then-reopen race.
    source_bytes = path.read_bytes()
    if hashlib.sha256(source_bytes).hexdigest() != PINNED["clean_text.py"]:
        raise InputError("Pinned artifact hash mismatch: clean_text.py")
    namespace = {"__name__": "_pinned_norbert_cleaner", "__file__": str(path)}
    exec(compile(source_bytes, str(path), "exec", dont_inherit=True), namespace)
    cleaner = namespace.get("clean")
    if not callable(cleaner):
        raise InputError("Pinned cleaner does not expose callable clean")
    return cleaner


def require_text(value: Any, field: str) -> str:
    # ASVS 2.2.1, 15.3.5: validate types and bounded text at the CLI boundary.
    if not isinstance(value, str) or not value.strip() or len(value) > MAX_TEXT_CHARS:
        raise InputError(f"{field} must be nonempty text of at most {MAX_TEXT_CHARS} characters")
    return value


def positive_int(value: str) -> int:
    number = int(value)
    if not 1 <= number <= 256:
        raise argparse.ArgumentTypeError("must be an integer from 1 to 256")
    return number


def probability(margin: float) -> float:
    if margin >= 0:
        return 1.0 / (1.0 + math.exp(-margin))
    exp_margin = math.exp(margin)
    return exp_margin / (1.0 + exp_margin)


@dataclass
class Prepared:
    windows: list[Any]
    token_count: int
    content_token_count: int
    cleaned_sha256: str

    @property
    def calls(self) -> int:
        return len(self.windows)


class LocalScorer:
    def __init__(self, model_dir: Path, windowed: bool = False, threads: int = 1):
        # ASVS 15.2.4: verify every externally executed/loaded model artifact first.
        self.model_dir = model_dir.resolve(strict=True)
        for relative, expected in PINNED.items():
            if relative == "clean_text.py":
                continue
            if file_hash(self.model_dir / relative) != expected:
                raise InputError(f"Pinned artifact hash mismatch: {relative}")
        self.clean = load_pinned_cleaner(self.model_dir / "clean_text.py")
        import numpy as np
        import onnxruntime as ort
        import tokenizers
        from tokenizers import Tokenizer

        self.np = np
        self.windowed = windowed
        self.tokenizer = Tokenizer.from_file(str(self.model_dir / "tokenizer.json"))
        self.tokenizer.no_padding()
        self.tokenizer.no_truncation()
        self.window_tokenizer = Tokenizer.from_file(str(self.model_dir / "tokenizer.json"))
        self.window_tokenizer.no_padding()
        self.window_tokenizer.enable_truncation(max_length=MAX_TOKENS, stride=0)
        options = ort.SessionOptions()
        options.intra_op_num_threads = threads
        options.inter_op_num_threads = 1
        self.session = ort.InferenceSession(str(self.model_dir / "onnx/detector_int8.onnx"),
                                            sess_options=options, providers=["CPUExecutionProvider"])
        inputs = {x.name: x.type for x in self.session.get_inputs()}
        if inputs != {"input_ids": "tensor(int64)", "attention_mask": "tensor(int64)"}:
            raise InputError("Unexpected ONNX input contract")
        outputs = self.session.get_outputs()
        if len(outputs) != 1 or outputs[0].shape[-1] != 2:
            raise InputError("Unexpected ONNX output contract")
        self.provenance = {
            "repo": MODEL_REPO, "revision": REVISION, "sha256": PINNED,
            "local_model_dir": str(self.model_dir), "provider": "CPUExecutionProvider",
            "class_order": {"0": "human", "1": "AI"},
            "numpy_version": np.__version__, "onnxruntime_version": ort.__version__,
            "tokenizers_version": tokenizers.__version__,
            "onnxruntime_threads": {"intra_op": threads, "inter_op": 1},
            "tokenizer_postprocessor": "pinned tokenizer.json; no manual EOS",
            "upstream_declared_license": "CC-BY-SA-4.0 (separately supplied artifacts)",
            "upstream_credit": "LTG-UiO NorBERT-4; Petter Egesund fine-tuning",
        }

    def prepare(self, text: str) -> Prepared:
        cleaned = self.clean(text)
        if not cleaned:
            raise InputError("Model cleaner produced empty input")
        encoded = self.tokenizer.encode(cleaned, add_special_tokens=True)
        count = len(encoded.ids)
        content_count = sum(1 - x for x in encoded.special_tokens_mask)
        if not content_count:
            raise InputError("Model input has no content tokens")
        if count > MAX_TOKENS and not self.windowed:
            raise TooLong(f"Input has {count} model tokens; maximum is {MAX_TOKENS}; use explicit --windowed")
        if count > MAX_TOKENS:
            first = self.window_tokenizer.encode(cleaned, add_special_tokens=True)
            windows = [first, *first.overflowing]
        else:
            windows = [encoded]
        # Check complete, non-overlapping content coverage after tokenizer postprocessing.
        original_content = [t for t, s in zip(encoded.ids, encoded.special_tokens_mask) if not s]
        covered = [t for w in windows for t, s in zip(w.ids, w.special_tokens_mask) if not s]
        if covered != original_content or any(len(w.ids) > MAX_TOKENS for w in windows):
            raise InputError("Tokenizer window coverage validation failed")
        return Prepared(windows, count, content_count, text_hash(cleaned))

    def infer(self, prepared: Prepared) -> dict:
        details = []
        offset = 0
        for index, encoded in enumerate(prepared.windows):
            ids = self.np.asarray([encoded.ids], dtype=self.np.int64)
            mask = self.np.asarray([encoded.attention_mask], dtype=self.np.int64)
            values = self.session.run(None, {"input_ids": ids, "attention_mask": mask})[0]
            logits = [float(x) for x in values[0]]
            if len(logits) != 2 or not all(math.isfinite(x) for x in logits):
                raise InputError("Model returned invalid logits")
            margin = logits[1] - logits[0]
            content = sum(1 - x for x in encoded.special_tokens_mask)
            details.append({"index": index, "logits": logits, "ai_probability": probability(margin),
                            "ai_minus_human_margin": margin, "tokens_with_specials": len(encoded.ids),
                            "content_token_start": offset, "content_token_end_exclusive": offset + content})
            offset += content
        worst = max(details, key=lambda x: x["ai_minus_human_margin"])
        return {"logits": worst["logits"], "ai_probability": worst["ai_probability"],
                "ai_minus_human_margin": worst["ai_minus_human_margin"],
                "tokens_with_specials_full_input": prepared.token_count,
                "content_tokens_full_input": prepared.content_token_count,
                "window_count": len(details), "windows": details,
                "aggregation": "worst_window_AI_margin_NONSTANDARD" if len(details) > 1 else "single_full_text",
                "full_content_coverage": True, "overlap_content_tokens": 0,
                "model_cleaned_sha256": prepared.cleaned_sha256}


class MeasurementCache:
    def __init__(self, scorer: Any, max_calls: int):
        self.scorer = scorer
        self.max_calls = max_calls
        self.actual_calls = 0
        self.cache_hits = 0
        self.requests = 0
        self.cache: dict[str, dict] = {}

    def measure(self, text: str, *, prepared: Prepared | None = None) -> dict:
        self.requests += 1
        if text in self.cache:
            self.cache_hits += 1
            return self.cache[text]
        if prepared is None:
            prepared = self.scorer.prepare(text)
        # ASVS 15.2.2: budget actual ONNX session.run calls, including all windows.
        if self.actual_calls + prepared.calls > self.max_calls:
            raise BudgetExhausted()
        result = self.scorer.infer(prepared)
        self.actual_calls += prepared.calls
        self.cache[text] = {"text": text, "sha256": text_hash(text), **result}
        return self.cache[text]

    def counts(self) -> dict:
        return {"actual_inference_calls": self.actual_calls, "inference_call_budget": self.max_calls,
                "unique_full_text_measurements": len(self.cache), "cache_hits": self.cache_hits,
                "measurement_requests": self.requests}


def word_count(text: str) -> int:
    return len(re.findall(r"\b\w+(?:[-']\w+)*\b", text, flags=re.UNICODE))


def numeric_spellings(text: str) -> Counter:
    # Literal spellings/counts only; neither unit association nor semantic proof.
    # Preserve signs, scientific exponents and common explicit uncertainty forms.
    number = r"\d+(?:[.,:/\-]\d+)*(?:[eE][+\-−]?\d+)?"
    literal = rf"(?<!\w)(?:[+\-−±][ \t]*)?{number}(?:[ \t]*±[ \t]*[+\-−]?{number})?(?:\s?[%‰])?(?!\w)"
    return Counter(re.findall(literal, text))


def validate_search_packet(packet: Any) -> tuple[list[tuple[str, ...]], str, str]:
    if not isinstance(packet, dict):
        raise InputError("Search packet must be an object")
    require_text(packet.get("id"), "id")
    language = require_text(packet.get("language"), "language").lower()
    if language not in NORWEGIAN:
        raise InputError("Search only supports explicitly Norwegian packets; English workflow is unchanged")
    source = require_text(packet.get("source"), "source")
    baseline = require_text(packet.get("baseline"), "baseline")
    # ASVS 2.2.1: optional references obey the same bounded-text contract.
    if "accepted_reference" in packet:
        require_text(packet["accepted_reference"], "accepted_reference")
    groups = packet.get("groups")
    if not isinstance(groups, list) or not 1 <= len(groups) <= 128:
        raise InputError("groups must contain 1 to 128 paragraph groups")
    options = []
    for group in groups:
        if not isinstance(group, dict):
            raise InputError("Each group must be an object")
        original = require_text(group.get("original"), "original")
        alternatives = group.get("alternatives")
        if not isinstance(alternatives, list) or len(alternatives) != 3:
            raise InputError("Each group requires exactly three alternatives")
        options.append((original, *(require_text(x, "alternative") for x in alternatives)))
    if "\n\n".join(o[0] for o in options) != baseline:
        raise InputError("Joining original groups with blank lines must exactly equal baseline")
    return options, source, baseline


def search_packet(packet: dict, scorer: Any, *, beam_width: int = 4, passes: int = 2,
                  max_calls: int = 256, guard_numbers: bool = False,
                  guard_word_bounds: bool = False) -> dict:
    options, source, baseline = validate_search_packet(packet)
    if not 1 <= beam_width <= 256 or not 1 <= passes <= 256 or not 1 <= max_calls <= 256:
        raise InputError("Search limits must be between 1 and 256")
    meter = MeasurementCache(scorer, max_calls)
    reference_names: dict[str, list[str]] = {}
    for name in ("source", "baseline", "accepted_reference"):
        if name in packet:
            reference_names.setdefault(packet[name], []).append(name)
    # Preflight every distinct mandatory reference, including every window, before
    # inference. A partially measured reference set cannot protect an earlier best.
    prepared_references = {text: scorer.prepare(text) for text in reference_names}
    required_calls = sum(prepared.calls for prepared in prepared_references.values())
    if required_calls > max_calls:
        raise ReferenceBudgetExhausted(
            f"Protected references require {required_calls} inference calls; budget is {max_calls}")
    protected_references = [
        {**meter.measure(text, prepared=prepared_references[text]), "names": names,
         "source_fidelity": FIDELITY}
        for text, names in reference_names.items()
    ]
    base_score = meter.cache[baseline]
    initial = tuple(0 for _ in options)
    beam = [(initial, base_score)]
    measured = {baseline: (initial, base_score)}
    log = []
    stopped = False
    source_numbers = numeric_spellings(source)
    max_words = math.floor(word_count(source) * 1.1)
    for pass_index in range(passes):
        for group_index in range(len(options)):
            pool = {record[1]["text"]: record for record in beam}
            for state, _ in beam:
                for option_index in range(4):
                    next_state = state[:group_index] + (option_index,) + state[group_index + 1:]
                    text = "\n\n".join(options[g][choice] for g, choice in enumerate(next_state))
                    require_text(text, "assembled candidate")
                    event = {"pass": pass_index + 1, "group": group_index,
                             "option": option_index, "sha256": text_hash(text)}
                    reason = None
                    if guard_numbers and numeric_spellings(text) != source_numbers:
                        reason = "literal_numeric_spellings_differ"
                    if guard_word_bounds and not 150 <= word_count(text) <= max_words:
                        reason = "word_bounds_150_to_110_percent_source"
                    if reason:
                        log.append({**event, "status": "guard_rejected", "reason": reason})
                        continue
                    previous_calls = meter.actual_calls
                    try:
                        score = meter.measure(text)
                    except TooLong:
                        log.append({**event, "status": "over_token_limit_rejected"})
                        continue
                    except BudgetExhausted:
                        log.append({**event, "status": "budget_exhausted_unmeasured"})
                        stopped = True
                        break
                    measured.setdefault(text, (next_state, score))
                    pool.setdefault(text, (next_state, score))
                    log.append({**event, "status": "measured" if meter.actual_calls > previous_calls else "cache_hit",
                                "actual_calls_added": meter.actual_calls - previous_calls,
                                "ai_minus_human_margin": score["ai_minus_human_margin"]})
                if stopped:
                    break
            beam = sorted(pool.values(), key=lambda r: (r[1]["ai_minus_human_margin"], r[1]["sha256"]))[:beam_width]
            if stopped:
                break
        if stopped:
            break
    ranked = sorted(measured.values(), key=lambda r: (r[1]["ai_minus_human_margin"], r[1]["sha256"]))
    top = [{**score, "choices": list(state)} for state, score in ranked if score["text"] != baseline][:3]
    best_measured = min(meter.cache.values(), key=lambda r: (r["ai_minus_human_margin"], r["sha256"]))
    return {"id": packet["id"], "language": packet["language"], "source_sha256": text_hash(source),
            "baseline": {**base_score, "choices": list(initial)}, "top_candidates": top,
            "protected_references": protected_references,
            "best_measured_sha256": best_measured["sha256"],
            "status": "budget_exhausted_measured_results_only" if stopped else "completed",
            "counts": meter.counts(), "search_log": log,
            "settings": {"beam_width": beam_width, "passes": passes, "options_per_group": 4,
                         "guard_numbers": guard_numbers, "guard_word_bounds": guard_word_bounds,
                         "baseline_retained_even_if_guards_fail": True},
            "source_fidelity": FIDELITY,
            "required_host_review": "Review source fidelity before accepting any candidate; low detector score alone is insufficient."}


def reject_duplicate_keys(pairs: list) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise InputError("Duplicate JSON object key")
        result[key] = value
    return result


def read_packets(path: Path) -> list:
    # ASVS 1.5.2: plain UTF-8 JSON only; never pickle or execute packet content.
    if path.stat().st_size > MAX_INPUT_BYTES:
        raise InputError("Input JSON exceeds 16 MiB")
    data = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicate_keys,
                      parse_constant=lambda _: (_ for _ in ()).throw(InputError("Nonfinite JSON number")))
    if not isinstance(data, list) or not 1 <= len(data) <= 256:
        raise InputError("Input must be a JSON array of 1 to 256 packets")
    ids = []
    for packet in data:
        if not isinstance(packet, dict):
            raise InputError("Each packet must be an object")
        ids.append(require_text(packet.get("id"), "id"))
    if len(ids) != len(set(ids)):
        raise InputError("Packet ids must be unique")
    return data


def atomic_json(path: Path, value: Any) -> None:
    # ASVS 5.3.2: output path comes exclusively from explicit CLI, not packet fields.
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="\n", prefix=".norbert-",
                                         suffix=".tmp", dir=path.parent, delete=False) as stream:
            temporary = Path(stream.name)
            json.dump(value, stream, ensure_ascii=False, indent=2, allow_nan=False)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["score", "search"])
    parser.add_argument("--model-dir", required=True, type=Path)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--windowed", action="store_true", help="explicit full-coverage, nonstandard worst-window scoring")
    parser.add_argument("--threads", type=positive_int, default=1)
    parser.add_argument("--beam-width", type=positive_int, default=4)
    parser.add_argument("--passes", type=positive_int, default=2)
    parser.add_argument("--max-inferences", type=positive_int, default=256)
    parser.add_argument("--guard-numbers", action="store_true")
    parser.add_argument("--guard-word-bounds", action="store_true")
    args = parser.parse_args(argv)
    try:
        input_path = args.input.resolve(strict=True)
        output_path = args.output.resolve()
        if input_path == output_path or (output_path.exists() and os.path.samefile(input_path, output_path)):
            raise InputError("Input and output must be different files")
        packets = read_packets(input_path)
        if args.command == "search":
            for packet in packets:
                validate_search_packet(packet)
        else:
            for packet in packets:
                require_text(packet.get("text"), "text")
        scorer = LocalScorer(args.model_dir, windowed=args.windowed, threads=args.threads)
        results = []
        for document_index, packet in enumerate(packets, start=1):
            if args.command == "search":
                result = search_packet(packet, scorer, beam_width=args.beam_width, passes=args.passes,
                                       max_calls=args.max_inferences, guard_numbers=args.guard_numbers,
                                       guard_word_bounds=args.guard_word_bounds)
            else:
                meter = MeasurementCache(scorer, args.max_inferences)
                result = {"id": packet["id"], **meter.measure(packet["text"]), "counts": meter.counts()}
            results.append(result)
            # Numeric-only progress: never log IDs or user text during long batches.
            print(json.dumps({"document_index": document_index, "document_total": len(packets),
                              **result["counts"]}), file=sys.stderr, flush=True)
        atomic_json(output_path, {"schema": "norbert-local-helper-v1", "command": args.command,
                                  "model_provenance": scorer.provenance, "results": results,
                                  "warning": "Detector scores are not authorship probabilities or source-fidelity proof."})
        print(json.dumps({"status": "written", "documents": len(results)}, ensure_ascii=False))
        return 0
    except (InputError, BudgetExhausted, OSError, json.JSONDecodeError, UnicodeError) as exc:
        # ASVS 16.5.1/16.5.3: no raw text, paths or exception payloads in progress/errors.
        category = ("budget_too_small_for_protected_references" if isinstance(exc, ReferenceBudgetExhausted)
                    else "budget_too_small_for_baseline" if isinstance(exc, BudgetExhausted)
                    else type(exc).__name__)
        print(json.dumps({"status": "failed", "category": category,
                          "reason": str(exc) if isinstance(exc, (InputError, ReferenceBudgetExhausted))
                          else "Local input/model operation failed"}), file=sys.stderr)
        return 2
    except Exception:
        print('{"status":"failed","category":"runtime_error","reason":"Local scoring failed; no output committed"}', file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
