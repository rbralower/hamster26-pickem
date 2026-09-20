#!/usr/bin/env python3
"""Assemble rank_picks.py from rank_picks_part*.py, else from rank_picks.b64."""
from __future__ import annotations
import base64
import zlib
from pathlib import Path

root = Path(__file__).resolve().parent
target = root / "rank_picks.py"


def _from_parts():
    parts = sorted(root.glob("rank_picks_part*.py"))
    if not parts:
        return None
    src = "".join(p.read_text() for p in parts)
    if len(src) < 1000:
        return None
    target.write_text(src)
    return src


def _from_file():
    if target.exists() and target.stat().st_size > 1000:
        return target.read_text()
    return None


def _from_b64():
    blob = (root / "rank_picks.b64").read_text().strip()
    code = zlib.decompress(base64.b64decode("".join(blob.split())))
    target.write_bytes(code)
    return code.decode()


src = _from_parts() or _from_file() or _from_b64()
exec(compile(src, str(target), "exec"), {"__name__": "__main__", "__file__": str(target)})
