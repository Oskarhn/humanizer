#!/usr/bin/env python3
"""Build a reproducible source-skill archive without changing installations."""
from __future__ import annotations

import argparse
from fnmatch import fnmatch
import hashlib
import io
import json
from pathlib import Path
import re
import sys
import zipfile

from validate_package import validate

ROOT = Path(__file__).resolve().parents[1]
TOP_FILES = (
    'SKILL.md', 'README.md', 'LICENSE', 'CHANGELOG.md', 'CONTRIBUTING.md',
    'SECURITY.md', 'AGENTS.md', 'CLAUDE.md', '.editorconfig', '.gitattributes', '.gitignore',
)
DIRECTORIES = ('agents', 'references', 'scripts', 'tests', 'evals', 'docs', '.github')
IGNORED_DIRS = {'.git', '__pycache__', '.venv', '.pytest_cache', 'node_modules', 'dist', 'runs'}
IGNORED_PATTERNS = ('*.pyc', '*.pyo', '*.pdf', '*.zip', '*.bundle', '.DS_Store', '.env', '.env.*')
TEXT_SUFFIXES = {'.md', '.py', '.json', '.yaml', '.yml', '.cff'}


def skill_version(root: Path) -> str:
    text = (root / 'SKILL.md').read_text(encoding='utf-8')
    match = re.search(r'^  version: [\"\']?(\d+\.\d+\.\d+)[\"\']?\s*$', text, re.MULTILINE)
    if not match:
        raise ValueError('Expected a three-part version in SKILL.md metadata')
    return match[1]


def selected_files(root: Path) -> dict[str, Path]:
    paths = [root / name for name in TOP_FILES if (root / name).exists() or (root / name).is_symlink()]
    for name in DIRECTORIES:
        directory = root / name
        if directory.is_symlink():
            raise ValueError(f'Symlink is not a release member: {name}')
        if directory.exists():
            paths.extend(directory.rglob('*'))
    result = {}
    for path in sorted(paths):
        relative = path.relative_to(root)
        if any(p in IGNORED_DIRS for p in relative.parts):
            continue
        if any(fnmatch(path.name, pattern) for pattern in IGNORED_PATTERNS):
            continue
        if path.is_symlink():
            raise ValueError(f'Symlink is not a release member: {relative.as_posix()}')
        if not path.is_file():
            continue
        if not path.resolve().is_relative_to(root.resolve()):
            raise ValueError(f'Release path escapes its source directory: {relative.as_posix()}')
        if path.suffix not in TEXT_SUFFIXES and relative.as_posix() not in TOP_FILES:
            raise ValueError(f'Unsupported release file: {relative.as_posix()}')
        path.read_text(encoding='utf-8')
        result[relative.as_posix()] = path
    return result


def build_release(root: Path = ROOT, output_dir: Path | None = None, check_tag: str | None = None) -> dict:
    root = root.resolve()
    if not (root / 'SKILL.md').is_file():
        raise ValueError('The source directory does not contain SKILL.md')
    # Check the selected tree before reading Markdown references through a symlink.
    members = selected_files(root)
    errors = validate(root)
    if errors:
        raise ValueError('Package validation failed: ' + '; '.join(errors))
    version = skill_version(root)
    if check_tag is not None and check_tag != f'v{version}':
        raise ValueError(f'Tag {check_tag!r} does not match skill version v{version}')
    output_dir = (output_dir or root / 'dist').resolve()
    payload = {name: path.read_bytes() for name, path in members.items()}
    manifest = {
        'skill': 'humanizer', 'version': version,
        'files': {name: hashlib.sha256(data).hexdigest() for name, data in payload.items()},
    }
    payload['RELEASE-MANIFEST.json'] = (json.dumps(manifest, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in sorted(payload.items()):
            info = zipfile.ZipInfo('humanizer/' + name, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    archive_bytes = buffer.getvalue()
    digest = hashlib.sha256(archive_bytes).hexdigest()
    filename = f'humanizer-v{version}.zip'
    outputs = {
        output_dir / filename: archive_bytes,
        output_dir / (filename + '.sha256'): f'{digest}  {filename}\n'.encode('ascii'),
    }
    for path, data in outputs.items():
        if path.exists() and (not path.is_file() or path.read_bytes() != data):
            raise FileExistsError(f'Refusing to overwrite a different artifact: {path}')
    output_dir.mkdir(parents=True, exist_ok=True)
    for path, data in outputs.items():
        if not path.exists():
            with path.open('xb') as stream:
                stream.write(data)
    return {'version': version, 'source_files': len(members), 'archive_members': len(payload),
            'archive': str(output_dir / filename), 'sha256': digest}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=ROOT, help='Skill source directory')
    parser.add_argument('--output-dir', type=Path, help='Output directory; default: <source>/dist')
    parser.add_argument('--check-tag', help='Require a release tag to equal v<skill-version>')
    args = parser.parse_args(argv)
    try:
        print(json.dumps(build_release(args.source, args.output_dir, args.check_tag), indent=2))
    except (OSError, ValueError, UnicodeError, zipfile.BadZipFile) as exc:
        print(f'Cannot build release: {exc}', file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
