"""Failure controls for retained evidence integrity; no PTY compatibility claims."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import warnings
import zipfile

spec = importlib.util.spec_from_file_location('verify_evidence', Path(__file__).with_name('verify-evidence.py'))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class EvidenceIntegrity(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'evidence.zip'

    def make_archive(self, payload=b'pass\n', indexed_payload=None, extra=None, rows=None):
        expected = payload if indexed_payload is None else indexed_payload
        if rows is None:
            rows = [{'path': 'artifacts/result.txt', 'bytes': len(expected),
                     'sha256': hashlib.sha256(expected).hexdigest()}]
        with zipfile.ZipFile(self.path, 'w', zipfile.ZIP_DEFLATED) as archive:
            archive.writestr('artifacts/result.txt', payload)
            archive.writestr(module.INDEX, json.dumps(rows))
            if extra:
                with warnings.catch_warnings():
                    warnings.simplefilter('ignore', UserWarning)
                    archive.writestr(extra, b'extra')
        return hashlib.sha256(self.path.read_bytes()).hexdigest()

    def test_good_archive_without_extraction(self):
        result = module.verify(self.path, self.make_archive())
        self.assertEqual(result['members'], 2)
        self.assertEqual(result['status'], 'verified')
        self.assertEqual(list(Path(self.temp.name).iterdir()), [self.path])

    def test_wrong_trusted_digest(self):
        self.make_archive()
        with self.assertRaisesRegex(ValueError, 'archive SHA-256 mismatch'):
            module.verify(self.path, '0' * 64)

    def test_changed_member_same_size(self):
        sha = self.make_archive(payload=b'fail\n', indexed_payload=b'pass\n')
        with self.assertRaisesRegex(ValueError, 'member SHA-256 mismatch'):
            module.verify(self.path, sha)

    def test_unsafe_duplicate_and_unindexed_members(self):
        for name in ('../outside.txt', '/outside.txt', 'C:/outside.txt',
                     'a\\b', 'a/./b', 'artifacts/result.txt', 'unindexed.txt'):
            with self.subTest(name=name), self.assertRaises(ValueError):
                module.verify(self.path, self.make_archive(extra=name))

    def test_false_size_and_index(self):
        for row in ({'path': 'artifacts/result.txt', 'bytes': True, 'sha256': '0' * 64},
                    {'path': 'artifacts/result.txt', 'bytes': 99, 'sha256': '0' * 64},
                    {'path': module.INDEX, 'bytes': 0, 'sha256': '0' * 64}):
            with self.subTest(row=row), self.assertRaises(ValueError):
                module.verify(self.path, self.make_archive(rows=[row]))

    def test_truncated_archive(self):
        self.make_archive()
        self.path.write_bytes(self.path.read_bytes()[:-10])
        with self.assertRaises(zipfile.BadZipFile):
            module.verify(self.path, hashlib.sha256(self.path.read_bytes()).hexdigest())

    def test_bounds(self):
        sha = self.make_archive()
        for name, limit in (('MAX_ARCHIVE', 1), ('MAX_EXPANDED', 1),
                            ('MAX_INDEX', 1), ('MAX_MEMBERS', 1)):
            original = getattr(module, name)
            try:
                setattr(module, name, limit)
                with self.subTest(bound=name), self.assertRaises(ValueError):
                    module.verify(self.path, sha)
            finally:
                setattr(module, name, original)


if __name__ == '__main__':
    unittest.main()
