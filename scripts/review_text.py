#!/usr/bin/env python3
"""Local review cues and literal change checks. Not an AI detector or rewriter.

Exit 0: no flags; 1: review flags; 2: input/configuration error.
Only reads files/stdin and writes a report to stdout. Standard library only.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys
import unicodedata

NUMBER = re.compile(r"(?<![\w])[-+−]?\d+(?:[.,]\d+)*(?:[eE][-+−]?\d+)?(?:%|‰)?(?!\w)")
URL = re.compile(r"https?://[^\s<>\[\]\"`]+")
CITATION = re.compile(r"\[(?:\d+(?:\s*[,;–—-]\s*\d+)*|@[^\]\n]+|\^[-\w]+)\]")
INLINE_CODE = re.compile(r"(?<!`)(`+)(?!`)(.+?)(?<!`)\1(?!`)", re.DOTALL)
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
# These are review locations, never banned words or provenance signals.
PHRASES = (
    "in today's rapidly evolving", "it is important to note that",
    "it is worth noting that", "in conclusion", "det er viktig å merke seg at",
    "i dagens stadig skiftende", "avslutningsvis kan vi konkludere med",
)


def read_text(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    file = Path(path)
    if file.suffix.lower() not in {".txt", ".md", ".markdown"}:
        raise ValueError(f"Expected .txt/.md/.markdown, got {file.suffix!r}; extract other formats first")
    return file.read_text(encoding="utf-8-sig")


def code_blocks(text: str) -> tuple[list[str], str]:
    """Return fenced blocks and prose with those blocks blanked, retaining lines."""
    blocks, prose, current = [], [], []
    marker, size = None, 0
    for line in text.splitlines(keepends=True):
        match = FENCE.match(line.rstrip("\r\n"))
        if marker is None and match:
            marker, size = match[1][0], len(match[1])
            current = [line]
            prose.append("\n")
        elif marker is not None:
            current.append(line)
            prose.append("\n")
            if match and match[1][0] == marker and len(match[1]) >= size and not match[2].strip():
                blocks.append("".join(current))
                marker, size, current = None, 0, []
        else:
            prose.append(line)
    if current:
        blocks.append("".join(current))
    return blocks, "".join(prose)


def literals(text: str) -> dict[str, Counter]:
    blocks, prose = code_blocks(text)
    return {
        "numbers": Counter(NUMBER.findall(text)),
        "urls": Counter(x.rstrip(".,;:!?)'") for x in URL.findall(text)),
        "bracketed_citations": Counter(CITATION.findall(text)),
        "fenced_code": Counter(blocks),
        "inline_code": Counter(x[1] for x in INLINE_CODE.findall(prose)),
    }


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def surface_flags(text: str) -> list[dict]:
    flags = []
    _, prose = code_blocks(text)
    for index, char in enumerate(prose):
        if char in {"\u200b", "\u2060", "\ufeff", "\u202a", "\u202b", "\u202c", "\u202d", "\u202e", "\u2066", "\u2067", "\u2068", "\u2069"}:
            flags.append({"kind": "invisible_or_directional_character", "line": line_number(prose, index),
                          "detail": f"U+{ord(char):04X} {unicodedata.name(char, 'UNKNOWN')}; inspect purpose before changing"})
    for phrase in PHRASES:
        for match in re.finditer(re.escape(phrase), prose, flags=re.IGNORECASE):
            flags.append({"kind": "phrase_to_review", "line": line_number(prose, match.start()),
                          "detail": match[0], "note": "May be appropriate; inspect function, not authorship"})
    seen: dict[str, int] = {}
    for match in re.finditer(r"(?:[^\n]+(?:\n(?!\s*\n)[^\n]+)*)", prose):
        paragraph = re.sub(r"\s+", " ", match[0]).strip()
        if len(paragraph.split()) < 8:
            continue
        if paragraph in seen:
            flags.append({"kind": "repeated_paragraph", "line": line_number(prose, match.start()),
                          "first_line": seen[paragraph], "detail": paragraph})
        else:
            seen[paragraph] = line_number(prose, match.start())
    return flags


def validate_locks(locks: object) -> dict:
    if not isinstance(locks, dict):
        raise ValueError("Locks must be a JSON object")
    unknown = set(locks) - {"required_literals", "forbidden_literals", "min_words", "max_words"}
    if unknown:
        raise ValueError(f"Unknown lock keys: {', '.join(sorted(unknown))}")
    for key in ("required_literals", "forbidden_literals"):
        value = locks.get(key, [])
        if not isinstance(value, list) or any(not isinstance(s, str) or not s for s in value):
            raise ValueError(f"{key} must be a list of nonempty strings")
    for key in ("min_words", "max_words"):
        if key in locks and (type(locks[key]) is not int or locks[key] < 0):
            raise ValueError(f"{key} must be a nonnegative integer")
    if locks.get("min_words", 0) > locks.get("max_words", float("inf")):
        raise ValueError("min_words must not exceed max_words")
    return locks


def review(revised: str, original: str | None = None, locks: dict | None = None) -> dict:
    locks = validate_locks({} if locks is None else locks)
    flags = surface_flags(revised)
    if original is not None:
        before, after = literals(original), literals(revised)
        for category in before:
            removed, added = before[category] - after[category], after[category] - before[category]
            if removed or added:
                flags.append({"kind": "literal_change", "category": category,
                              "removed": dict(removed), "added": dict(added),
                              "note": "Inspect against source; literal differences may be legitimate"})
    for literal in locks.get("required_literals", []):
        if literal not in revised:
            flags.append({"kind": "missing_required_literal", "detail": literal})
    for literal in locks.get("forbidden_literals", []):
        if literal in revised:
            flags.append({"kind": "forbidden_literal_present", "detail": literal})
    words = len(revised.split())
    for key, violation in (("min_words", words < locks.get("min_words", 0)),
                           ("max_words", words > locks.get("max_words", float("inf")))):
        if violation:
            flags.append({"kind": "length_constraint", "constraint": key, "limit": locks[key], "observed": words})
    return {
        "status": "review_required" if flags else "no_automatic_flags",
        "word_count_whitespace": words,
        "original_compared": original is not None,
        "flags": flags,
        "limitations": "Literal checks and surface cues only. No semantic, factual, voice, authorship, or detector-resistance certification.",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("text", help="Revised UTF-8 .txt/.md/.markdown file, or - for stdin")
    parser.add_argument("--original", help="Original UTF-8 text file for literal comparisons")
    parser.add_argument("--locks", help="JSON file with explicit preservation/length constraints")
    parser.add_argument("--format", choices=("json", "text"), default="json")
    args = parser.parse_args(argv)
    try:
        if args.text == "-" and args.original == "-":
            raise ValueError("Only one input may read stdin")
        revised = read_text(args.text)
        original = read_text(args.original) if args.original else None
        locks = json.loads(Path(args.locks).read_text(encoding="utf-8-sig")) if args.locks else {}
        report = review(revised, original, locks)
    except (OSError, UnicodeError, ValueError) as exc:
        print(json.dumps({"status": "input_error", "error": str(exc)}, ensure_ascii=True), file=sys.stderr)
        return 2
    if args.format == "json":
        print(json.dumps(report, indent=2, ensure_ascii=True))
    else:
        print(f"Status: {report['status']}")
        print(report["limitations"])
        for flag in report["flags"]:
            print(json.dumps(flag, ensure_ascii=True))
    return 1 if report["flags"] else 0


if __name__ == "__main__":
    sys.exit(main())
