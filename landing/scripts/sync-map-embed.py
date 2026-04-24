#!/usr/bin/env python3
"""
Sync the map data embedded in landing/map.html from landing/tools.json.

map.html inlines the map data so the page works without a network fetch
(file://, offline, or any host). tools.json remains the canonical single
source of truth. This script rewrites the embedded <script type="application/json"
id="map-data"> block so the two stay bit-identical.

Usage:
    python3 landing/scripts/sync-map-embed.py          # rewrite in place
    python3 landing/scripts/sync-map-embed.py --check  # exit 1 if drifted

CI invokes --check on every PR to prevent drift.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOLS_PATH = REPO_ROOT / "landing" / "tools.json"
MAP_PATH = REPO_ROOT / "landing" / "map.html"

START_MARKER = '<script type="application/json" id="map-data">'
END_MARKER = "</script>"
BLOCK_RE = re.compile(
    r'<script type="application/json" id="map-data">.*?</script>',
    re.DOTALL,
)


def canonical_json(data: object) -> str:
    """Stable, human-readable JSON for the embed. Matches tools.json format."""
    return json.dumps(data, indent=2, ensure_ascii=False)


def build_block(data: object) -> str:
    body = canonical_json(data)
    return f"{START_MARKER}\n{body}\n{END_MARKER}"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--check",
        action="store_true",
        help="Verify the embedded block matches tools.json. Exit 1 if drifted.",
    )
    args = ap.parse_args()

    if not TOOLS_PATH.exists():
        print(f"ERROR: {TOOLS_PATH} not found", file=sys.stderr)
        return 2
    if not MAP_PATH.exists():
        print(f"ERROR: {MAP_PATH} not found", file=sys.stderr)
        return 2

    with TOOLS_PATH.open() as f:
        data = json.load(f)

    html = MAP_PATH.read_text()
    desired_block = build_block(data)

    if not BLOCK_RE.search(html):
        if args.check:
            print(
                f"ERROR: no map-data block found in {MAP_PATH.name}. "
                f"Run: python3 landing/scripts/sync-map-embed.py",
                file=sys.stderr,
            )
            return 1
        print(
            f"ERROR: no map-data block found in {MAP_PATH.name}. "
            "Add a placeholder <script type=\"application/json\" id=\"map-data\"></script> "
            "to map.html first.",
            file=sys.stderr,
        )
        return 2

    new_html = BLOCK_RE.sub(lambda _m: desired_block, html, count=1)

    if new_html == html:
        print(f"OK: {MAP_PATH.name} is in sync with {TOOLS_PATH.name}")
        return 0

    if args.check:
        print(
            f"FAIL: embedded map data in {MAP_PATH.name} has drifted from {TOOLS_PATH.name}. "
            f"Run: python3 landing/scripts/sync-map-embed.py",
            file=sys.stderr,
        )
        return 1

    MAP_PATH.write_text(new_html)
    tools_count = len(data.get("tools", []))
    print(f"UPDATED: rewrote map-data block in {MAP_PATH.name} ({tools_count} entries)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
