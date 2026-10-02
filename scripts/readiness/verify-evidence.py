"""Verify a sealed private evidence ZIP without extraction or target execution."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import stat
import sys
import zipfile
import zlib

MAX_ARCHIVE = 64 * 1024 * 1024
MAX_EXPANDED = 1024 * 1024 * 1024
MAX_INDEX = 4 * 1024 * 1024
MAX_MEMBERS = 10000
INDEX = 'artifacts/rc3-private-evidence-members.json'
SHA = re.compile(r'[0-9a-f]{64}\Z')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def valid_name(name):
    require(isinstance(name, str) and bool(name), 'invalid member name')
    require('\\' not in name and ':' not in name and '\x00' not in name,
            'nonportable member name')
    parts = name.split('/')
    require(not PurePosixPath(name).is_absolute() and
            all(p not in ('', '.', '..') for p in parts), 'unsafe member path')


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, 'duplicate JSON key')
        result[key] = value
    return result


def digest(stream):
    sha = hashlib.sha256()
    while chunk := stream.read(1024 * 1024):
        sha.update(chunk)
    return sha.hexdigest()


def verify(path, expected_sha256):
    require(isinstance(expected_sha256, str) and SHA.fullmatch(expected_sha256),
            'expected SHA-256 must be 64 lowercase hex characters')
    with Path(path).open('rb') as source:
        source.seek(0, 2)
        archive_bytes = source.tell()
        require(archive_bytes <= MAX_ARCHIVE, 'archive exceeds 64 MiB limit')
        source.seek(0)
        actual_sha = digest(source)
        require(actual_sha == expected_sha256, 'archive SHA-256 mismatch')
        source.seek(0)
        with zipfile.ZipFile(source) as archive:
            members = archive.infolist()
            require(0 < len(members) <= MAX_MEMBERS, 'member count exceeds bounds')
            names = {}
            expanded = 0
            for member in members:
                valid_name(member.filename)
                require(member.filename not in names, 'duplicate ZIP member')
                require(not member.is_dir() and not member.flag_bits & 1,
                        'directories and encrypted members are unsupported')
                require(not stat.S_ISLNK(member.external_attr >> 16),
                        'symlink member is unsupported')
                expanded += member.file_size
                require(expanded <= MAX_EXPANDED, 'expanded evidence exceeds 1 GiB')
                names[member.filename] = member
            require(INDEX in names, 'evidence member index is missing')
            require(names[INDEX].file_size <= MAX_INDEX, 'index exceeds 4 MiB')
            rows = json.loads(archive.read(INDEX).decode('utf-8'),
                              object_pairs_hook=unique_object)
            require(isinstance(rows, list) and len(rows) == len(members) - 1,
                    'index must cover every evidence member exactly once')
            indexed = set()
            for row in rows:
                require(isinstance(row, dict) and set(row) == {'path', 'bytes', 'sha256'},
                        'invalid index row')
                name = row['path']
                valid_name(name)
                require(name != INDEX and name not in indexed and name in names,
                        'index references duplicate, missing or self member')
                require(type(row['bytes']) is int and 0 <= row['bytes'] <= MAX_EXPANDED,
                        'invalid indexed size')
                require(isinstance(row['sha256'], str) and SHA.fullmatch(row['sha256']),
                        'invalid indexed SHA-256')
                require(row['bytes'] == names[name].file_size, 'indexed size mismatch')
                with archive.open(names[name]) as stream:
                    require(digest(stream) == row['sha256'], 'evidence member SHA-256 mismatch')
                indexed.add(name)
            require(indexed == set(names) - {INDEX}, 'unindexed evidence member')
    return {'status': 'verified', 'sha256': actual_sha, 'archive_bytes': archive_bytes,
            'members': len(members), 'expanded_bytes': expanded,
            'crc_verified': True, 'member_hashes_verified': True,
            'scope': 'Integrity against supplied digest; does not establish runtime results or independent adoption'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive', type=Path)
    parser.add_argument('--sha256', required=True, help='Trusted digest from the completion seal')
    args = parser.parse_args()
    try:
        result = verify(args.archive, args.sha256)
    except (OSError, ValueError, KeyError, zipfile.BadZipFile, NotImplementedError,
            RuntimeError, EOFError, RecursionError, zlib.error):
        # Paths, member data and private exception values stay out of public output.
        print('Evidence verification failed: digest, archive or member index is invalid.', file=sys.stderr)
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == '__main__':
    sys.exit(main())
