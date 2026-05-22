#!/usr/bin/env python3
"""auto‑rename‑duplicate‑detector (ARDD)

Detects duplicate files by content and renames the later copy with a short hash.

Usage: python ardd.py <directory>
"""
import argparse, hashlib, os, sys
from pathlib import Path

def file_hash(path: Path) -> str:
    """Return a hex SHA‑256 digest of *path* (streamed for large files)."""
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

def rename_duplicate(orig: Path, dup: Path, short_hash: str) -> None:
    new_name = dup.with_name(f"{dup.stem}-{short_hash}{dup.suffix}")
    counter = 1
    while new_name.exists():
        new_name = dup.with_name(f"{dup.stem}-{short_hash}_{counter}{dup.suffix}")
        counter += 1
    dup.rename(new_name)
    print(f"Renamed: {dup} → {new_name}")

def scan(dir_path: Path) -> None:
    if not dir_path.is_dir():
        sys.exit(f"Error: {dir_path} is not a directory")

    seen = {}  # hash → first occurrence Path
    duplicates = []

    for path in dir_path.rglob('*'):
        if path.is_file():
            h = file_hash(path)
            if h in seen:
                duplicates.append((seen[h], path, h[:8]))
            else:
                seen[h] = path

    for orig, dup, short in duplicates:
        rename_duplicate(orig, dup, short)

    print(f"Done. {len(duplicates)} duplicate(s) handled.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Auto‑rename duplicate files in a directory')
    parser.add_argument('directory', type=Path, help='Root folder to scan')
    args = parser.parse_args()
    scan(args.directory)
