from contextlib import redirect_stderr, redirect_stdout
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest

MODULE = Path(__file__).resolve().parents[1] / "scripts" / "review_text.py"
SPEC = importlib.util.spec_from_file_location("review_text", MODULE)
review_text = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(review_text)


class ReviewTests(unittest.TestCase):
    def test_faithful_paraphrase_has_no_automatic_flags(self):
        original = "Among 42 users, time fell from 8.4 to 6.9 minutes [7]. We cannot establish causation."
        revised = "Time fell from 8.4 to 6.9 minutes among 42 users [7]. Causation remains unestablished."
        self.assertEqual(review_text.review(revised, original)["status"], "no_automatic_flags")

    def test_changed_sample_size_and_citation_need_review(self):
        report = review_text.review("Among 420 users [8].", "Among 42 users [7].")
        flags = {f["category"]: f for f in report["flags"]}
        self.assertEqual(flags["numbers"]["removed"], {"42": 1, "7": 1})
        self.assertEqual(flags["bracketed_citations"]["added"], {"[8]": 1})

    def test_same_numbers_do_not_imply_same_meaning(self):
        report = review_text.review("Reduced to 20%.", "Reduced by 20%.")
        self.assertEqual(report["status"], "no_automatic_flags")
        locked = review_text.review("Reduced to 20%.", locks={"required_literals": ["by 20%"]})
        self.assertEqual(locked["flags"][0]["kind"], "missing_required_literal")

    def test_polarity_drift_is_not_falsely_certified(self):
        report = review_text.review("The intervention helped.", "The intervention did not help.")
        self.assertIn("No semantic", report["limitations"])
        self.assertEqual(report["status"], "no_automatic_flags")

    def test_signed_decimal_scientific_numbers(self):
        self.assertEqual(review_text.literals("−0,25 +3.4 -1e-3 42% 20‰")["numbers"],
                         {"−0,25": 1, "+3.4": 1, "-1e-3": 1, "42%": 1, "20‰": 1})

    def test_duplicate_numeric_occurrence_is_detected(self):
        report = review_text.review("Use 5 ml.", "Use 5 ml, then another 5 ml.")
        number = next(f for f in report["flags"] if f.get("category") == "numbers")
        self.assertEqual(number["removed"], {"5": 1})

    def test_changed_url(self):
        report = review_text.review("See https://example.org/b.", "See https://example.org/a.")
        self.assertTrue(any(f.get("category") == "urls" for f in report["flags"]))

    def test_inline_and_fenced_code(self):
        original = "Run `x += 1`.\n\n```python\nx = 2\n```\n"
        revised = "Run `x += 2`.\n\n```python\nx = 3\n```\n"
        categories = {f.get("category") for f in review_text.review(revised, original)["flags"]}
        self.assertTrue({"inline_code", "fenced_code"} <= categories)

    def test_tilde_fence_and_longer_closing_fence(self):
        text = "~~~text\nin conclusion\n~~~~\n"
        self.assertEqual(len(review_text.code_blocks(text)[0]), 1)
        self.assertEqual(review_text.surface_flags(text), [])

    def test_code_does_not_trigger_phrase_cues(self):
        text = "```text\nit is important to note that\n```\nThis sentence is fine."
        self.assertEqual(review_text.surface_flags(text), [])

    def test_invisible_characters_are_locations_not_authorship_claims(self):
        flags = review_text.surface_flags("Norsk tekst\nuten\u200b mellomrom")
        self.assertEqual(flags[0]["line"], 2)
        self.assertEqual(flags[0]["kind"], "invisible_or_directional_character")

    def test_norwegian_unicode_and_phrase_location(self):
        report = review_text.review("Ærlig tekst.\nDet er viktig å merke seg at dette gjelder nå.")
        self.assertEqual(report["flags"][0]["line"], 2)

    def test_repeated_paragraph(self):
        p = "This is a substantial paragraph with more than eight words."
        flags = review_text.surface_flags(p + "\n\n" + p)
        self.assertEqual(flags[0]["kind"], "repeated_paragraph")
        self.assertEqual(flags[0]["first_line"], 1)
        self.assertEqual(flags[0]["line"], 3)

    def test_explicit_locks_and_length(self):
        report = review_text.review("This proves causation.", locks={"required_literals": ["may"],
                                  "forbidden_literals": ["proves causation"], "min_words": 5})
        self.assertEqual({f["kind"] for f in report["flags"]},
                         {"missing_required_literal", "forbidden_literal_present", "length_constraint"})

    def test_invalid_locks_are_rejected(self):
        for locks in ([], {"required_literals": [""]}, {"max_words": True}, {"min_words": -1},
                      {"max_words": "20"}, {"min_words": 4, "max_words": 2}, {"typo": 1}):
            with self.subTest(locks=locks), self.assertRaises(ValueError):
                review_text.review("text", locks=locks)

    def test_cli_reports_invalid_file_without_modifying_input(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "source.pdf"
            path.write_bytes(b"not a supported format")
            with redirect_stderr(io.StringIO()) as err:
                code = review_text.main([str(path)])
            self.assertEqual(code, 2)
            self.assertEqual(json.loads(err.getvalue())["status"], "input_error")
            self.assertEqual(path.read_bytes(), b"not a supported format")

    def test_cli_utf8_bom_and_exit_codes(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "text.md"
            path.write_text("Ærlig og presis tekst.", encoding="utf-8-sig")
            before = path.read_bytes()
            with redirect_stdout(io.StringIO()) as out:
                code = review_text.main([str(path)])
            self.assertEqual(code, 0)
            self.assertEqual(json.loads(out.getvalue())["status"], "no_automatic_flags")
            self.assertEqual(path.read_bytes(), before)
            path.write_text("In conclusion, we are done.", encoding="utf-8")
            with redirect_stdout(io.StringIO()):
                self.assertEqual(review_text.main([str(path)]), 1)


if __name__ == "__main__":
    unittest.main()
