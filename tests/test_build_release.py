import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
SPEC = importlib.util.spec_from_file_location('build_release', ROOT / 'scripts/build_release.py')
builder = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(builder)


class ReleaseTests(unittest.TestCase):
    def stage(self, directory):
        source = Path(directory) / 'source'
        shutil.copytree(ROOT, source, ignore=shutil.ignore_patterns('.git', 'dist', '__pycache__', '.venv'))
        return source

    def test_member_hashes_and_extracted_package(self):
        with tempfile.TemporaryDirectory() as temp:
            source = self.stage(temp)
            result = builder.build_release(source)
            archive_path = Path(result['archive'])
            self.assertEqual(hashlib.sha256(archive_path.read_bytes()).hexdigest(), result['sha256'])
            with zipfile.ZipFile(archive_path) as archive:
                self.assertIsNone(archive.testzip())
                manifest = json.loads(archive.read('humanizer/RELEASE-MANIFEST.json'))
                self.assertEqual(len(manifest['files']) + 1, len(archive.namelist()))
                for name, digest in manifest['files'].items():
                    self.assertEqual(hashlib.sha256(archive.read('humanizer/' + name)).hexdigest(), digest)
                    self.assertEqual(archive.read('humanizer/' + name), (source / name).read_bytes())
                extract = Path(temp) / 'extracted'
                archive.extractall(extract)
            self.assertEqual(builder.validate(extract / 'humanizer'), [])

    def test_same_bytes_produce_same_archive(self):
        with tempfile.TemporaryDirectory() as temp:
            source = self.stage(temp)
            a = builder.build_release(source, Path(temp) / 'a')
            b = builder.build_release(source, Path(temp) / 'b')
            self.assertEqual(Path(a['archive']).read_bytes(), Path(b['archive']).read_bytes())
            # Rebuilding into the same directory is a no-op for matching bytes.
            self.assertEqual(builder.build_release(source, Path(temp) / 'a')['sha256'], a['sha256'])

    def test_local_and_private_artifacts_are_excluded(self):
        with tempfile.TemporaryDirectory() as temp:
            source = self.stage(temp)
            for name in ['.git/private.md', 'dist/private.md', 'evals/runs/private.md',
                         'references/private.pdf', 'scripts/__pycache__/private.pyc', '.env']:
                p = source / name
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text('local material', encoding='utf-8')
            result = builder.build_release(source)
            with zipfile.ZipFile(result['archive']) as archive:
                self.assertFalse(any('private' in name or name.endswith('/.env') for name in archive.namelist()))

    def test_different_existing_archive_is_preserved(self):
        with tempfile.TemporaryDirectory() as temp:
            source = self.stage(temp)
            output = Path(temp) / 'out'
            output.mkdir()
            target = output / f'humanizer-v{builder.skill_version(source)}.zip'
            target.write_bytes(b'keep this existing file')
            with self.assertRaises(FileExistsError):
                builder.build_release(source, output)
            self.assertEqual(target.read_bytes(), b'keep this existing file')

    def test_invalid_package_does_not_write_output(self):
        with tempfile.TemporaryDirectory() as temp:
            source = self.stage(temp)
            (source / 'references/evidence.md').unlink()
            out = Path(temp) / 'out'
            with self.assertRaises(ValueError):
                builder.build_release(source, out)
            self.assertFalse(out.exists())

    def test_mismatched_tag_does_not_write_output(self):
        with tempfile.TemporaryDirectory() as temp:
            source = self.stage(temp)
            out = Path(temp) / 'out'
            with self.assertRaises(ValueError):
                builder.build_release(source, out, 'v999.0.0')
            self.assertFalse(out.exists())

    def test_symlink_member_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            source = self.stage(temp)
            external = Path(temp) / 'external.md'
            external.write_text('not a source member', encoding='utf-8')
            try:
                (source / 'references/external.md').symlink_to(external)
            except (OSError, NotImplementedError) as exc:
                self.skipTest(f'Symlink creation unavailable: {exc}')
            with self.assertRaises(ValueError):
                builder.build_release(source)

    def test_unexpected_file_type_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            source = self.stage(temp)
            (source / 'references/unexpected.bin').write_bytes(b'no binary release member')
            with self.assertRaises(ValueError):
                builder.build_release(source)


if __name__ == '__main__':
    unittest.main()
