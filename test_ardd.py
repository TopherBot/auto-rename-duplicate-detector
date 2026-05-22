import os, shutil
from pathlib import Path
import subprocess

# Helper to create a file with given content

def make_file(path: Path, content: bytes):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)


def test_duplicate_renaming(tmp_path: Path):
    # Create two identical files in different subfolders
    f1 = tmp_path / "a" / "file.txt"
    f2 = tmp_path / "b" / "file.txt"
    make_file(f1, b"duplicate content")
    make_file(f2, b"duplicate content")

    # Run the script
    result = subprocess.run([sys.executable, "ardd.py", str(tmp_path)], capture_output=True, text=True)
    assert result.returncode == 0
    # The second file should be renamed
    renamed = list((tmp_path / "b").glob("file-????????.txt"))
    assert len(renamed) == 1
    # Ensure original file remains unchanged
    assert f1.read_bytes() == b"duplicate content"
    # Clean up
    shutil.rmtree(tmp_path)
