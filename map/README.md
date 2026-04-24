# The Map

The Map is FTWR's curated directory of tools, datasets, papers, and libraries relevant to sports data modelling. Every entry solves a specific, verifiable problem. Every entry is attributed, dated, and periodically re-verified.

This directory will be spun out into its own repository (`ftwr-map`) once the commons has a second steward. Until then, The Map lives alongside the other governance artifacts in the monorepo, and the canonical data file is `landing/tools.json` at the root of this repo.

## What this directory contains

| File | Purpose |
|---|---|
| [`schema.json`](schema.json) | JSON Schema describing the contract every entry must satisfy. Enforced in CI. |
| [`PULL_REQUEST_TEMPLATE.md`](PULL_REQUEST_TEMPLATE.md) | Template used when opening a Map PR. Every field is required. |
| [`scripts/validate.py`](scripts/validate.py) | Validator that checks The Map against the schema, detects duplicates, and reports staleness. |

The editorial policy for what belongs in The Map and what does not lives in [`../CURATION.md`](../CURATION.md). Read it before submitting.

## How to contribute

1. Read [`../CURATION.md`](../CURATION.md) and confirm the entry meets the five inclusion tests (utility, verifiable, neutral, non-redundant, categorised).
2. Edit `landing/tools.json` adding your entry under the `tools` array. Match the field order used by existing entries.
3. Regenerate the inline embed in `landing/map.html`:
   ```sh
   python3 landing/scripts/sync-map-embed.py
   ```
   The Map page loads its data from an inline `<script type="application/json" id="map-data">` block so it works from any URL scheme (file://, offline, any static host). `tools.json` stays the single source of truth; CI fails PRs where the two have drifted.
4. Open a PR using the [Map PR template](PULL_REQUEST_TEMPLATE.md). Every field in the template is required.
5. CI runs `map/scripts/validate.py` and the embed drift check automatically. If either fails, fix and re-push.
6. A steward reviews within 5 business days. Expect questions, description edits, or category reassignment.

## Entry contract

Every entry is a JSON object with the following required fields:

```json
{
  "cat": "data",
  "name": "example-tool",
  "desc": "Neutral description under 200 characters: what it does, what its constraints are.",
  "url": "https://example.com",
  "tags": ["football", "free", "api"],
  "edge": "data",
  "contributor": "@handle",
  "added": "2026-04-23",
  "last_verified": "2026-04-23"
}
```

Optional fields:

- `license` — SPDX identifier for code entries.
- `coi` — conflict-of-interest disclosure, required whenever a material interest exists.
- `sport` — when sport-specific.
- `featured` — boolean. If true, the entry is surfaced in the "Start Here" strip at the top of The Map. Set by stewards only; use sparingly.
- `featured_note` — short caption (10-120 chars) shown under a featured card. Required when `featured: true`.

The authoritative schema is [`schema.json`](schema.json). If the schema and this README disagree, the schema wins.

## Local validation

Run both checks before opening a PR:

```sh
python3 map/scripts/validate.py
python3 landing/scripts/sync-map-embed.py --check
```

The validator checks:

- Every entry matches the JSON Schema contract
- No duplicate `name` across entries (duplicate `url` surfaces as a warning — one repo can legitimately expose multiple methods)
- `last_verified` is not in the future
- `added` is not after `last_verified`
- Entries with `last_verified` older than 180 days are reported as stale (warning, not failure)

The embed sync check verifies that `landing/map.html`'s inline `<script type="application/json" id="map-data">` block matches `tools.json` byte-for-byte. Regenerate with `python3 landing/scripts/sync-map-embed.py` (no flag) after editing `tools.json`.

Exit code 0 means valid. Non-zero means at least one check failed; CI will block the PR.

## Verification cadence

Every entry carries a `last_verified` date. Entries older than 180 days are flagged in the monthly maintenance pass. Verification means the URL still loads, the tool still behaves as described, and licensing or pricing has not changed materially. See [`../CURATION.md`](../CURATION.md) § Verification and Deprecation.

## Deprecation

Deprecated entries are not deleted. They are moved to an `archived/` section with a `deprecated_on` date and a short note. This preserves the record and prevents repeat submissions of known-degraded tools.

## Controlled vocabularies

Categories, edges, and tags are fixed vocabularies defined in [`schema.json`](schema.json). Adding a new value requires an RFC or steward approval. The current vocabularies:

- **Categories:** `data`, `odds`, `models`, `edge`, `arbitrage`, `markets`, `python`, `viz`, `community`
- **Edges:** `data`, `model`, `market`, `execution`, `community`
- **Tags:** `api`, `basketball`, `commercial`, `football`, `free`, `ftwr`, `multi-sport`, `open-source`, `python`, `r`, `tennis`

## Amendments

The Map's schema and policy are amended only through an RFC. See [`../rfcs/`](../rfcs/).
