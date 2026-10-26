#!/usr/bin/env python3
"""Dependency-free structural checks for this package; no behavioral claims."""
from __future__ import annotations

import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def validate(root: Path = ROOT) -> list[str]:
    errors = []
    required = ("SKILL.md", "LICENSE", "README.md", "agents/openai.yaml",
                "references/evidence.md", "references/supplied-pdfs.json", "evals/cases.json",
                "references/watermarks-and-provenance.md", "evals/watermark-cases.json")
    for relative in required:
        if not (root / relative).is_file():
            errors.append(f"Missing {relative}")
    if errors:
        return errors
    skill = (root / "SKILL.md").read_text(encoding="utf-8")
    front = re.match(r"\A---\n(.*?)\n---\n", skill, re.DOTALL)
    if not front:
        errors.append("SKILL.md needs YAML frontmatter")
    else:
        if not re.search(r"^name: humanizer$", front[1], re.MULTILINE):
            errors.append("Unexpected skill name")
        if not re.search(r"^description: .{30,1024}$", front[1], re.MULTILINE):
            errors.append("Missing or invalid description")
    if len(skill.split()) > 2300:
        errors.append("Entrypoint exceeds this project's 2300-word context budget")
    for file in sorted(root.rglob("*.md")):
        if any(part in {".git", ".venv", "__pycache__", "dist", "node_modules", "runs"}
               for part in file.relative_to(root).parts):
            continue
        text = file.read_text(encoding="utf-8")
        if "[TODO:" in text:
            errors.append(f"Unfinished scaffold: {file.relative_to(root)}")
        if re.search(r"[A-Z]:[\\/](?:Users|home)[\\/]|/home/[a-z]+/", text):
            errors.append(f"Machine-specific absolute path: {file.relative_to(root)}")
        for target in re.findall(r"\[[^\]\n]+\]\(([^)]+)\)", text):
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            clean = target.split("#", 1)[0]
            if clean and not (file.parent / clean).is_file():
                errors.append(f"Broken local link: {file.relative_to(root)} -> {target}")
    try:
        manifest = json.loads((root / "references/supplied-pdfs.json").read_text(encoding="utf-8"))
        if not isinstance(manifest, list) or not manifest:
            errors.append("Expected a nonempty list of supplied PDF records")
        else:
            names = set()
            digests = set()
            for row in manifest:
                if not isinstance(row, dict):
                    errors.append("Manifest entries must be objects")
                    continue
                if not isinstance(row.get("file"), str) or not row["file"].endswith(".pdf"):
                    errors.append("Invalid manifest filename")
                elif row["file"] in names:
                    errors.append("Duplicate manifest filename")
                names.add(row.get("file"))
                if not re.fullmatch(r"[0-9a-f]{64}", str(row.get("sha256", ""))):
                    errors.append("Invalid source SHA-256")
                elif row["sha256"] in digests:
                    errors.append("Duplicate source content; record a resubmission as an alias instead")
                digests.add(row.get("sha256"))
                if type(row.get("pages")) is not int or row["pages"] < 1:
                    errors.append("Invalid source page count")
        cases = json.loads((root / "evals/cases.json").read_text(encoding="utf-8"))
        extra_cases = json.loads((root / "evals/watermark-cases.json").read_text(encoding="utf-8"))
        if not isinstance(extra_cases, list) or not extra_cases:
            errors.append("Expected a nonempty list of provenance cases")
        if not isinstance(cases, list) or len(cases) < 20:
            errors.append("Expected at least twenty behavioral cases")
        else:
            if isinstance(extra_cases, list):
                cases = cases + extra_cases
            ids = set()
            for case in cases:
                if not isinstance(case, dict):
                    errors.append("Case entries must be objects")
                    continue
                if not isinstance(case.get("id"), str) or case["id"] in ids:
                    errors.append("Invalid/duplicate case ID")
                ids.add(case.get("id"))
                for key in ("category", "request", "input"):
                    if not isinstance(case.get(key), str) or not case[key]:
                        errors.append(f"Case {case.get('id')} has invalid {key}")
                expectations = case.get("expectations")
                if not isinstance(expectations, list) or not expectations or any(not isinstance(s, str) or not s for s in expectations):
                    errors.append(f"Case {case.get('id')} has invalid expectations")
    except (ValueError, OSError) as exc:
        errors.append(f"Invalid JSON input: {exc}")
    return errors


if __name__ == "__main__":
    errors = validate()
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    print("Package structure, local links, source records, and behavioral case shape: PASS")
