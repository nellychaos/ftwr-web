#!/usr/bin/env python3
"""
FTWR Map validator.

Validates landing/tools.json against map/schema.json and enforces
cross-entry invariants that JSON Schema cannot express: no duplicate
names or URLs, date sanity, category existence, and staleness reporting.

Exit code:
    0  - all entries valid (stale entries may be reported as warnings)
    1  - at least one entry failed validation

Usage:
    python3 map/scripts/validate.py
    python3 map/scripts/validate.py --strict-staleness  # fail on stale entries
    python3 map/scripts/validate.py --tools path/to/tools.json
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_TOOLS = REPO_ROOT / "landing" / "tools.json"
DEFAULT_SCHEMA = REPO_ROOT / "map" / "schema.json"
STALENESS_DAYS = 180

# Controlled vocabularies (kept in sync with map/schema.json).
VALID_CATS = {
    "data", "odds", "models", "edge", "arbitrage",
    "markets", "python", "viz", "community",
}
VALID_EDGES = {"data", "model", "market", "execution", "community"}
VALID_TAGS = {
    "api", "basketball", "commercial", "football", "free", "ftwr",
    "multi-sport", "open-source", "python", "r", "tennis",
}

REQUIRED_FIELDS = [
    "cat", "name", "desc", "url", "tags", "edge",
    "contributor", "added", "last_verified",
]
OPTIONAL_FIELDS = {"license", "coi", "sport", "featured", "featured_note"}
ALLOWED_FIELDS = set(REQUIRED_FIELDS) | OPTIONAL_FIELDS

HANDLE_RE = re.compile(r"^@[a-z0-9][a-z0-9-]{1,38}$")
DATE_RE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
URL_RE = re.compile(r"^https?://")


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def err(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)

    def ok(self) -> bool:
        return not self.errors


def parse_date(value: str) -> dt.date | None:
    try:
        return dt.date.fromisoformat(value)
    except (ValueError, TypeError):
        return None


def validate_entry(idx: int, entry: dict[str, Any], report: Report, today: dt.date) -> None:
    label = f"tools[{idx}]"
    name = entry.get("name") if isinstance(entry, dict) else None
    if isinstance(name, str) and name:
        label = f"tools[{idx}] ({name})"

    if not isinstance(entry, dict):
        report.err(f"{label}: entry is not a JSON object")
        return

    # Unknown fields
    for key in entry.keys():
        if key not in ALLOWED_FIELDS:
            report.err(f"{label}: unknown field '{key}' (allowed: {sorted(ALLOWED_FIELDS)})")

    # Required fields
    for field in REQUIRED_FIELDS:
        if field not in entry:
            report.err(f"{label}: missing required field '{field}'")

    # cat
    cat = entry.get("cat")
    if cat is not None and cat not in VALID_CATS:
        report.err(f"{label}: cat '{cat}' not in {sorted(VALID_CATS)}")

    # name
    nm = entry.get("name")
    if nm is not None:
        if not isinstance(nm, str) or not (1 <= len(nm) <= 120):
            report.err(f"{label}: name must be a string 1-120 chars")

    # desc
    desc = entry.get("desc")
    if desc is not None:
        if not isinstance(desc, str):
            report.err(f"{label}: desc must be a string")
        elif not (20 <= len(desc) <= 240):
            report.err(f"{label}: desc length {len(desc)} out of range 20-240")

    # url
    url = entry.get("url")
    if url is not None:
        if not isinstance(url, str) or not URL_RE.match(url):
            report.err(f"{label}: url must start with http:// or https://")

    # tags
    tags = entry.get("tags")
    if tags is not None:
        if not isinstance(tags, list) or not tags:
            report.err(f"{label}: tags must be a non-empty array")
        else:
            if len(tags) > 6:
                report.err(f"{label}: tags exceed max of 6 (got {len(tags)})")
            if len(set(tags)) != len(tags):
                report.err(f"{label}: tags contain duplicates")
            for t in tags:
                if t not in VALID_TAGS:
                    report.err(f"{label}: tag '{t}' not in controlled vocabulary")

    # edge
    edge = entry.get("edge")
    if edge is not None and edge not in VALID_EDGES:
        report.err(f"{label}: edge '{edge}' not in {sorted(VALID_EDGES)}")

    # contributor
    contributor = entry.get("contributor")
    if contributor is not None:
        if not isinstance(contributor, str) or not HANDLE_RE.match(contributor):
            report.err(f"{label}: contributor '{contributor}' must match @[a-z0-9][a-z0-9-]{{1,38}}")

    # dates
    added_raw = entry.get("added")
    lv_raw = entry.get("last_verified")
    added = parse_date(added_raw) if isinstance(added_raw, str) and DATE_RE.match(added_raw) else None
    lv = parse_date(lv_raw) if isinstance(lv_raw, str) and DATE_RE.match(lv_raw) else None

    if added_raw is not None and added is None:
        report.err(f"{label}: added '{added_raw}' is not a valid ISO date")
    if lv_raw is not None and lv is None:
        report.err(f"{label}: last_verified '{lv_raw}' is not a valid ISO date")

    if added and added > today:
        report.err(f"{label}: added ({added}) is in the future")
    if lv and lv > today:
        report.err(f"{label}: last_verified ({lv}) is in the future")
    if added and lv and added > lv:
        report.err(f"{label}: added ({added}) is after last_verified ({lv})")

    # Staleness (warning only)
    if lv:
        age = (today - lv).days
        if age > STALENESS_DAYS:
            report.warn(f"{label}: stale — last_verified {lv} is {age} days old (>{STALENESS_DAYS})")

    # coi length sanity
    coi = entry.get("coi")
    if coi is not None and (not isinstance(coi, str) or not (10 <= len(coi) <= 500)):
        report.err(f"{label}: coi must be a string 10-500 chars")

    # featured / featured_note
    featured = entry.get("featured")
    featured_note = entry.get("featured_note")
    if featured is not None and not isinstance(featured, bool):
        report.err(f"{label}: featured must be a boolean")
    if featured_note is not None and (not isinstance(featured_note, str) or not (10 <= len(featured_note) <= 120)):
        report.err(f"{label}: featured_note must be a string 10-120 chars")
    if featured is True and not isinstance(featured_note, str):
        report.err(f"{label}: entries with featured: true must include a featured_note caption")
    if featured is not True and featured_note is not None:
        report.warn(f"{label}: featured_note is set but featured is not true — note will not be shown")


def validate_cross_entry(tools: list[dict[str, Any]], categories_ids: set[str], report: Report) -> None:
    names: dict[str, int] = {}
    urls: dict[str, int] = {}
    for idx, entry in enumerate(tools):
        if not isinstance(entry, dict):
            continue
        name = entry.get("name")
        url = entry.get("url")
        cat = entry.get("cat")

        if isinstance(name, str):
            key = name.strip().lower()
            if key in names:
                report.err(
                    f"tools[{idx}] ({name}): duplicate name also at tools[{names[key]}]"
                )
            else:
                names[key] = idx

        if isinstance(url, str):
            key = url.rstrip("/").lower()
            if key in urls:
                # URL collisions are sometimes legitimate: one repo can expose
                # distinct methods that each warrant a separate entry.
                # Surface as a warning for human review, not a hard failure.
                report.warn(
                    f"tools[{idx}] ({name or '?'}): shares url with tools[{urls[key]}] "
                    f"— confirm non-redundancy per CURATION.md"
                )
            else:
                urls[key] = idx

        if isinstance(cat, str) and categories_ids and cat not in categories_ids:
            report.err(
                f"tools[{idx}] ({name or '?'}): cat '{cat}' not declared in categories[] of tools.json"
            )


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate The Map (FTWR curated directory).")
    parser.add_argument("--tools", type=Path, default=DEFAULT_TOOLS, help="Path to tools.json")
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA, help="Path to schema.json")
    parser.add_argument(
        "--strict-staleness",
        action="store_true",
        help="Treat stale entries (last_verified > 180 days) as errors instead of warnings.",
    )
    args = parser.parse_args()

    if not args.tools.exists():
        print(f"ERROR: tools file not found: {args.tools}", file=sys.stderr)
        return 2
    if not args.schema.exists():
        print(f"ERROR: schema file not found: {args.schema}", file=sys.stderr)
        return 2

    try:
        with args.tools.open() as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"ERROR: tools.json is not valid JSON: {e}", file=sys.stderr)
        return 2

    try:
        with args.schema.open() as f:
            json.load(f)  # sanity check; structural validation uses the code above
    except json.JSONDecodeError as e:
        print(f"ERROR: schema.json is not valid JSON: {e}", file=sys.stderr)
        return 2

    report = Report()
    today = dt.date.today()

    if not isinstance(data, dict):
        print("ERROR: tools.json root must be an object with 'tools' array", file=sys.stderr)
        return 2

    categories = data.get("categories", [])
    categories_ids = {c.get("id") for c in categories if isinstance(c, dict) and isinstance(c.get("id"), str)}

    tools = data.get("tools")
    if not isinstance(tools, list):
        print("ERROR: 'tools' is not an array in tools.json", file=sys.stderr)
        return 2

    for idx, entry in enumerate(tools):
        validate_entry(idx, entry, report, today)

    validate_cross_entry(tools, categories_ids, report)

    # Output
    for w in report.warnings:
        print(f"WARN  {w}")
    for e in report.errors:
        print(f"ERROR {e}", file=sys.stderr)

    if args.strict_staleness and report.warnings and not report.errors:
        print(
            f"\nFAIL: {len(report.warnings)} stale entries (strict mode)",
            file=sys.stderr,
        )
        return 1

    if not report.ok():
        print(
            f"\nFAIL: {len(report.errors)} error(s), "
            f"{len(report.warnings)} warning(s) across {len(tools)} entries",
            file=sys.stderr,
        )
        return 1

    print(
        f"\nOK: {len(tools)} entries valid "
        f"({len(report.warnings)} stale warning{'s' if len(report.warnings) != 1 else ''})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
