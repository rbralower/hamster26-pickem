#!/usr/bin/env python3
"""Load rank_picks.py from disk, or from the compressed blob if missing."""
from __future__ import annotations

import base64
import zlib
from pathlib import Path

root = Path(__file__).resolve().parent
target = root / "rank_picks.py"


def _load_source() -> str:
    if target.exists() and target.stat().st_size > 1000:
        return target.read_text()
    blob = (root / "rank_picks.b64").read_text().strip()
    code = zlib.decompress(base64.b64decode("".join(blob.split())))
    target.write_bytes(code)
    return code.decode()


src = _load_source()
exec(
    compile(src, str(target), "exec"),
    {"__name__": "__main__", "__file__": str(target)},
)
