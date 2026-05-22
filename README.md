# auto‑rename‑duplicate‑detector

A **single‑file** Python utility that:

1. Recursively walks a target directory.
2. Computes a SHA‑256 hash for every file.
3. Detects duplicates and renames the later copy to `filename‑<hash>.ext`.
4. Is safe‑guarded against name collisions and works cross‑platform.

## Installation
```bash
git clone https://github.com/your‑user/auto‑rename‑duplicate‑detector.git
cd auto‑rename‑duplicate‑detector
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Usage
```bash
python ardd.py /path/to/scan
```
The script prints a short summary of actions taken.

## CI
The repository ships a lightweight GitHub Actions workflow that runs `flake8` and the test suite on every push.

---
*Designed for quick prototyping, auto‑rename, and proactive duplicate detection.*