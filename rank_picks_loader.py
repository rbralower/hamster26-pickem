#!/usr/bin/env python3
"""Load compressed rank_picks body and exec it."""
import base64
import zlib
from pathlib import Path

root = Path(__file__).resolve().parent
b64 = (root / "rank_picks.b64").read_text().strip()
code = zlib.decompress(base64.b64decode(b64))
exec(compile(code, str(root / "rank_picks.py"), "exec"), {"__name__": "__main__", "__file__": str(root / "rank_picks.py")})
