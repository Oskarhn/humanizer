import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_package", ROOT / "scripts/validate_package.py")
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class PackageTests(unittest.TestCase):
    def stage(self, tmp):
        target = Path(tmp) / "skill"
        shutil.copytree(ROOT, target, ignore=shutil.ignore_patterns("__pycache__", "runs", ".git", "dist", ".venv"))
        return target

    def test_current_package(self):
        self.assertEqual(validator.validate(ROOT), [])

    def test_missing_runtime_entrypoint_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.stage(tmp)
            (root / "SKILL.md").unlink()
            self.assertIn("Missing SKILL.md", validator.validate(root))

    def test_broken_local_reference_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.stage(tmp)
            with (root / "README.md").open("a", encoding="utf-8") as stream:
                stream.write("\n[missing reference](references/missing.md)\n")
            self.assertTrue(any("Broken local link" in error for error in validator.validate(root)))

    def test_corrupt_source_hash_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.stage(tmp)
            path = root / "references/supplied-pdfs.json"
            records = json.loads(path.read_text(encoding="utf-8"))
            records[0]["sha256"] = "bad hash"
            path.write_text(json.dumps(records), encoding="utf-8")
            self.assertIn("Invalid source SHA-256", validator.validate(root))

    def test_additional_distinct_source_is_accepted(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.stage(tmp)
            path = root / "references/supplied-pdfs.json"
            records = json.loads(path.read_text(encoding="utf-8"))
            records.append({"file": "additional.pdf", "sha256": "1" * 64, "pages": 2})
            path.write_text(json.dumps(records), encoding="utf-8")
            self.assertEqual(validator.validate(root), [])

    def test_duplicate_source_content_is_not_counted_twice(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.stage(tmp)
            path = root / "references/supplied-pdfs.json"
            records = json.loads(path.read_text(encoding="utf-8"))
            records.append(dict(records[0], file="renamed-copy.pdf"))
            path.write_text(json.dumps(records), encoding="utf-8")
            self.assertTrue(any("Duplicate source content" in error for error in validator.validate(root)))

    def test_duplicate_behavioral_case_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.stage(tmp)
            path = root / "evals/cases.json"
            cases = json.loads(path.read_text(encoding="utf-8"))
            cases[1]["id"] = cases[0]["id"]
            path.write_text(json.dumps(cases), encoding="utf-8")
            self.assertIn("Invalid/duplicate case ID", validator.validate(root))

    def test_malformed_json_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.stage(tmp)
            (root / "evals/cases.json").write_text("invalid JSON", encoding="utf-8")
            self.assertTrue(any("Invalid JSON input" in error for error in validator.validate(root)))


if __name__ == "__main__":
    unittest.main()
