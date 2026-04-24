<!--
  The Map PR template. Every field is required.
  PRs missing fields, failing schema validation, or lacking evidence of utility will be closed.
  Read map/README.md and CURATION.md before opening a PR.
-->

## Type of change

<!-- Check one. -->

- [ ] New entry
- [ ] Edit to existing entry (description, tags, category, URL)
- [ ] `last_verified` refresh (no content changes)
- [ ] Deprecation (tool moved to archived)

## Entry

<!--
  Paste the JSON object you added or edited, exactly as it appears in tools.json.
  If editing, paste the *new* version; the diff shows the before state.
-->

```json
{
  "cat": "",
  "name": "",
  "desc": "",
  "url": "",
  "tags": [],
  "edge": "",
  "contributor": "@",
  "added": "YYYY-MM-DD",
  "last_verified": "YYYY-MM-DD"
}
```

## Contributor handle

<!-- Your forum / GitHub handle, starting with @. Must match the entry's contributor field. -->

@

## Verification

<!--
  Confirm all three. An entry with unchecked boxes cannot be merged.
-->

- [ ] I have loaded the URL and confirmed the tool behaves as the `desc` field claims.
- [ ] `last_verified` is set to today's date (ISO `YYYY-MM-DD`).
- [ ] The entry meets all five criteria in `CURATION.md` § What Belongs (utility, verifiable, neutral description, non-redundant, appropriate category).

## Evidence of utility

<!--
  One or two sentences: who uses this, for what, and how you know.
  "Has stars" is not evidence. "Used in [paper/thread/post]" or "I used it for X" is evidence.
-->

## Conflict of interest

<!--
  Required. Pick one.
  If you have any material interest (financial, professional, or personal) in the tool being added,
  you must include a `coi` field in the entry and describe the interest in one sentence here.
  See GOVERNANCE.md § Conflict of Interest.
-->

- [ ] I have no material interest in this tool.
- [ ] I have a material interest in this tool. It is disclosed in the entry's `coi` field and described below:

<!-- If disclosing a COI, describe it here in one sentence. -->

## Non-redundancy check

<!--
  What makes this entry distinct from existing entries in the same category?
  If substantially equivalent to an existing entry, describe the specific functional difference.
-->

## Checklist

- [ ] I ran `python3 map/scripts/validate.py` locally and it passed.
- [ ] I ran `python3 landing/scripts/sync-map-embed.py` so `map.html` reflects the new entry.
- [ ] The description is under 200 characters and contains no marketing language.
- [ ] I have read `CURATION.md` and `CODE_OF_CONDUCT.md`.
- [ ] I understand this handle will be permanently attached to this entry in the public record.
