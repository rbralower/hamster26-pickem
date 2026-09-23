#!/usr/bin/env python3
"""Assemble rank_picks.py from ALL rank_picks_part*.py files, else b64."""
from __future__ import annotations
import base64
import sys
import zlib
from pathlib import Path

root = Path(__file__).resolve().parent
target = root / "rank_picks.py"
EXPECTED_PARTS = 5


def _ok_src(src):
    return (
        src.lstrip().startswith("#!/usr/bin/env python3")
        and "def main(" in src
        and "if __name__" in src
        and len(src) > 20000
    )


def _from_parts():
    parts = sorted(root.glob("rank_picks_part*.py"))
    print("loader parts:", [p.name for p in parts], file=sys.stderr)
    if len(parts) < EXPECTED_PARTS:
        return None
    src = "".join(p.read_text() for p in parts)
    if not _ok_src(src):
        print("loader: joined parts failed sanity check", file=sys.stderr)
        return None
    target.write_text(src)
    return src


def _from_file():
    if target.exists() and target.stat().st_size > 20000:
        src = target.read_text()
        if _ok_src(src):
            return src
    return None


def _from_b64():
    path = root / "rank_picks.b64"
    if not path.exists():
        return None
    blob = path.read_text().strip()
    try:
        code = zlib.decompress(base64.b64decode("".join(blob.split())))
    except Exception as exc:
        print("loader: b64 decompress failed:", exc, file=sys.stderr)
        return None
    src = code.decode()
    if not _ok_src(src):
        print("loader: b64 payload failed sanity check", file=sys.stderr)
        return None
    target.write_text(src)
    return src


src = _from_parts() or _from_file() or _from_b64()
if not src:
    listing = "\n".join(
        f"  {p.name} {p.stat().st_size}" for p in sorted(root.iterdir()) if p.is_file()
    )
    sys.stderr.write(
        "FATAL: cannot assemble rank_picks.py. Need rank_picks_part1.py through "
        "rank_picks_part5.py on GitHub, or a working rank_picks.b64.\n" + listing + "\n"
    )
    raise SystemExit(2)
exec(compile(src, str(target), "exec"), {"__name__": "__main__", "__file__": str(target)})
