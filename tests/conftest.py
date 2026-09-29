"""Make tools/ and notes/ importable from the tests (the repository is not an installed package)."""
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
for sub in ("tools", "notes"):
    p = str(REPO / sub)
    if p not in sys.path:
        sys.path.insert(0, p)
