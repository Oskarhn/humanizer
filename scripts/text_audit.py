"""Read-only UTF-8 character audit and protected-literal comparison.

Python 3.10+, standard library only. No rewriting, normalization or networking.
Positions use Unicode code points, not bytes or UTF-16 editor columns.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata as ud
from pathlib import Path

MAX_BYTES = 4 * 1024 * 1024
MAX_MANIFEST_BYTES = 64 * 1024
MAX_LITERALS = 128
SPECIAL = {0x00AD, 0x034F, 0x115F, 0x1160, 0x17B4, 0x17B5,
           0x180B, 0x180C, 0x180D, 0x180E, 0x180F, 0x3164, 0xFFA0}
BIDI = {0x061C, 0x200E, 0x200F, *range(0x202A, 0x202F), *range(0x2066, 0x206A)}


class InputError(ValueError):
    pass


def read_utf8(name: str, limit: int = MAX_BYTES) -> tuple[bytes, str]:
    # ASVS 5.2.1 / 2.2.1: bounded reads and strict input validation.
    if name == "-":
        data = sys.stdin.buffer.read(limit + 1)
    else:
        with Path(name).open("rb") as stream:
            data = stream.read(limit + 1)
    if len(data) > limit:
        raise InputError(f"input exceeds {limit} bytes")
    if b"\x00" in data or data.startswith((b"%PDF-", b"PK\x03\x04", b"PK\x05\x06")):
        raise InputError("plain UTF-8 text required; binary containers and UTF-16 are unsupported")
    try:
        return data, data.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise InputError("input is not valid UTF-8; no encoding conversion was attempted") from exc


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def kind(ch: str) -> str | None:
    cp = ord(ch)
    if cp in BIDI:
        return "directionality"
    if 0x2061 <= cp <= 0x2064:
        return "mathematical_format"
    if 0xFE00 <= cp <= 0xFE0F or 0xE0100 <= cp <= 0xE01EF:
        return "variation_selector"
    if cp in SPECIAL or ud.category(ch) == "Cf":
        return "format_or_invisible"
    if ud.category(ch) == "Zs" and ch != " ":
        return "layout_space"
    if ud.category(ch) == "Co":
        return "private_use"
    if ud.category(ch) == "Cc" and ch not in "\r\n\t":
        return "control"
    return None


def inspect(text: str, limit: int) -> dict:
    findings, total = [], 0
    line, column = 1, 1
    for offset, ch in enumerate(text):
        category = kind(ch)
        if category:
            total += 1
            if len(findings) < limit:
                findings.append({"offset": offset, "line": line, "column": column,
                                 "codepoint": f"U+{ord(ch):04X}", "name": ud.name(ch, "UNNAMED"),
                                 "kind": category, "decision": "REVIEW_IN_CONTEXT"})
        if ch == "\n":
            line, column = line + 1, 1
        else:
            column += 1
    mixed, mixed_total = [], 0
    for match in re.finditer(r"[^\W\d_]+", text):
        scripts = {s for ch in match[0] for s in ("LATIN", "CYRILLIC", "GREEK")
                   if s in ud.name(ch, "")}
        if len(scripts) > 1:
            mixed_total += 1
            if len(mixed) < limit:
                mixed.append({"offset": match.start(), "length": len(match[0]),
                              "scripts": sorted(scripts), "decision": "REVIEW_IN_CONTEXT"})
    return {"characters": len(text), "character_findings_total": total, "findings": findings,
            "findings_truncated": total > len(findings), "mixed_script_tokens_total": mixed_total,
            "mixed_script_tokens": mixed, "mixed_script_tokens_truncated": mixed_total > len(mixed),
            "offset_unit": "unicode_codepoints", "line_and_column_base": 1,
            "unicode_database": ud.unidata_version,
            "scope": "Selected format/control characters, layout spaces, variation selectors, private use and Latin/Cyrillic/Greek mixtures; not every confusable or encoded artifact"}


def literal_count(text: str, literal: str) -> int:
    # Escape literals rather than interpreting a supplied regular expression.
    left = r"(?<!\w)" if literal[0].isalnum() or literal[0] == "_" else ""
    right = r"(?!\w)" if literal[-1].isalnum() or literal[-1] == "_" else ""
    return len(re.findall(left + re.escape(literal) + right, text))


def unique_keys(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise InputError("duplicate JSON object keys are not allowed")
        result[key] = value
    return result


def compare(before: str, after: str, source_hash: str, manifest: dict) -> list[dict]:
    # ASVS 1.5.2 / 2.2.1: data-only JSON, bounded schema and source binding.
    if not isinstance(manifest, dict) or set(manifest) != {"source_sha256", "literals"}:
        raise InputError("manifest must contain only source_sha256 and literals")
    if manifest["source_sha256"] != source_hash:
        raise InputError("manifest source hash does not match the actual input bytes")
    literals = manifest["literals"]
    if not isinstance(literals, list) or not 1 <= len(literals) <= MAX_LITERALS:
        raise InputError(f"manifest needs 1 through {MAX_LITERALS} literals")
    if any(not isinstance(s, str) or not 1 <= len(s) <= 4096 for s in literals):
        raise InputError("each protected literal must be a nonempty string of at most 4096 characters")
    if len(set(literals)) != len(literals):
        raise InputError("duplicate protected literals are not allowed")
    rows = []
    for index, literal in enumerate(literals):
        original = literal_count(before, literal)
        if not original:
            raise InputError(f"protected literal {index} is absent from the source")
        revised = literal_count(after, literal)
        rows.append({"literal_index": index, "before_count": original,
                     "after_count": revised, "preserved_count": original == revised})
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    scan = sub.add_parser("inspect", help="Report character positions; never edit the input")
    scan.add_argument("input", help="UTF-8 file or - for stdin")
    scan.add_argument("--limit", type=int, default=200, help="Maximum entries per finding list (1–1000)")
    pair = sub.add_parser("compare", help="Check selected literal counts; not semantic equivalence")
    pair.add_argument("before")
    pair.add_argument("after")
    pair.add_argument("--protect", required=True, help="UTF-8 JSON manifest bound to the source SHA-256")
    args = parser.parse_args()
    try:
        if args.command == "inspect":
            if not 1 <= args.limit <= 1000:
                raise InputError("limit must be between 1 and 1000")
            data, text = read_utf8(args.input)
            report = {"schema": "humanizer-text-audit-v1", "command": "inspect",
                      "source_sha256": sha(data), **inspect(text, args.limit)}
            result = int(bool(report["character_findings_total"] or report["mixed_script_tokens_total"]))
        else:
            if [args.before, args.after, args.protect].count("-") > 1:
                raise InputError("stdin can supply only one of before, after or manifest")
            bd, bt = read_utf8(args.before)
            ad, at = read_utf8(args.after)
            _, raw = read_utf8(args.protect, MAX_MANIFEST_BYTES)
            manifest = json.loads(raw, object_pairs_hook=unique_keys)
            checks = compare(bt, at, sha(bd), manifest)
            report = {"schema": "humanizer-text-audit-v1", "command": "compare",
                      "source_sha256": sha(bd), "revision_sha256": sha(ad),
                      "literal_checks": checks, "semantic_fidelity": "NOT_CHECKED"}
            result = int(any(not row["preserved_count"] for row in checks))
        report.update(source_modified=False, statistical_watermark="NOT_TESTED", authorship="NOT_ESTABLISHED")
        # ASCII JSON escapes bidi/control characters instead of emitting them to a terminal.
        print(json.dumps(report, ensure_ascii=True, indent=2))
        return result
    except (InputError, OSError, UnicodeError, json.JSONDecodeError, RecursionError) as exc:
        message = str(exc) if isinstance(exc, InputError) else "cannot read or parse the supplied UTF-8 input"
        print("text_audit: " + message, file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
