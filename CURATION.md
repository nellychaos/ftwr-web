# Curation

This document is the editorial policy for The Map. It describes what belongs, what does not, how entries are reviewed, and how disputes are handled.

The Map is a curated public good, not a comprehensive index. Every entry is there because it solves a specific, verifiable problem for sports modellers -- data, odds, methods, edge measurement, arbitrage, execution, or tooling. The bar is: would a working practitioner reach for this?

## What Belongs

A Map entry qualifies if it meets **all** of the following:

### 1. Genuine utility

The tool, dataset, paper, or library solves a real, specific problem in sports modelling or adjacent work. "Utility" means a practitioner would use it, not just read about it.

### 2. Verifiable

The thing exists, is publicly accessible at the linked URL, and behaves as the entry describes. For code, the repository must contain substantive, working code. For commercial products, the URL must load and the feature set must be reachable without a sales call.

### 3. Neutral description

Descriptions are factual. Marketing language ("the best," "industry-leading," "most powerful") is grounds for rejection. A good description answers two questions in under 200 characters: **what does it do?** and **what are its constraints?**

### 4. Non-redundant

If a substantially equivalent entry already exists, a new submission needs a clear functional difference, not a different brand or URL. "Another API returning football fixtures" is not a differentiator; "the only free API covering the Thai Premier League with event-level timestamps" is.

### 5. Appropriate category

The entry fits into one of The Map sections (§01-§09). Submitters suggest a category; reviewers may reassign.

## What Does Not Belong

- Tools with no demonstrated use case in sports modelling or adjacent research
- Affiliate links or referral destinations submitted for traffic
- SaaS products with no meaningful free tier and no publicly documented API (pure sales-funnel landing pages)
- Personal portfolio projects with no external users or evidence of use
- Anything requiring personal data or account creation before the user can see what the product does
- Duplicate entries under rebranded or renamed versions of existing tools
- Content that exists primarily to sell picks, predictions, or "VIP" access
- Anything that violates `CODE_OF_CONDUCT.md`

## Commercial Entries

Commercial tools are listed if they fill a gap that has no adequate open-source equivalent and are genuinely used by practitioners. Being commercial is not a disqualifier.

Submitting a commercial tool in which the submitter holds a financial interest without disclosing that interest is grounds for permanent rejection of future submissions. See `GOVERNANCE.md` § Conflict of Interest.

The Map carries no sponsored entries, ever. No tool gets priority placement, bolded treatment, or preferential categorisation in exchange for anything.

## Entry Schema

Every Map entry carries:

| Field | Required | Description |
|---|---|---|
| `cat` | yes | Category ID (one of `data`, `odds`, `models`, `edge`, `arbitrage`, `markets`, `python`, `viz`, `community`) |
| `name` | yes | Tool or resource name as the project itself uses it |
| `desc` | yes | Neutral description, under 200 characters |
| `url` | yes | Canonical URL (homepage, repository, or primary documentation) |
| `tags` | yes | Array from the controlled tag vocabulary (see schema) |
| `edge` | yes | Which edge type it addresses (`data`, `model`, `market`, `execution`, `community`) |
| `contributor` | yes | Handle of the person who added or last substantively edited the entry |
| `added` | yes | ISO date the entry was first added (YYYY-MM-DD) |
| `last_verified` | yes | ISO date the entry was last confirmed to exist and behave as described |
| `license` | optional | For code: SPDX license identifier (e.g. `MIT`, `Apache-2.0`) |
| `coi` | optional | Conflict-of-interest disclosure if the contributor has a material interest |

The canonical schema lives in `ftwr-map/schema.json`. Entries failing validation are rejected automatically in CI.

## Review Process

1. **Submission.** A contributor opens a PR against `ftwr-map` adding or editing an entry. The PR template requires the contributor handle and the `last_verified` date.
2. **Automated validation.** CI runs the schema check, the link checker, and the duplicate detector. Failures must be addressed before human review.
3. **Human review.** A steward reviews for the criteria above. Expected turnaround: 5 business days. Reviewers may request description edits, ask for evidence of utility, or decline.
4. **Merge.** Accepted PRs are merged with no squash, so the contributor's handle is preserved in git history and in the entry's `contributor` field.
5. **Rejection.** Rejected PRs are closed with a written explanation. The contributor may revise and resubmit once, or escalate per the Disputes section below.

## Verification and Deprecation

Every entry has a `last_verified` date. An entry is considered stale if `last_verified` is more than 180 days old. Stale entries are flagged for re-verification in a monthly maintenance pass.

Verification means: the URL loads, the tool still does what the description says, and the licensing or pricing has not changed materially.

Deprecation happens when:

- The URL is dead or redirects to an unrelated destination
- The tool has been acquired and its behaviour has substantively changed (e.g. previously free, now paywalled)
- The project has been archived or abandoned by its maintainer for 12+ months
- A newer canonical version of the same tool exists at a different URL (in which case the entry is updated, not deprecated)

Deprecated entries are not deleted. They are moved to an `archived/` section with a `deprecated_on` date and a short note explaining why. This preserves the historical record and prevents repeat submissions of tools known to have degraded.

## Disputes

If a tool maintainer or contributor believes an entry has been incorrectly rejected, miscategorised, or unfairly described:

1. Open a thread in the forum's **Map** category. Not a DM, not an email.
2. Explain the disagreement with specifics (which entry, what criteria, what evidence).
3. A steward and at least one other contributor weigh in publicly.
4. If unresolved after 14 days, any party may escalate to an RFC proposing a policy change.

Stewards do not quietly reverse other stewards' decisions. Disputes are a public process or they are not a process at all.

## Takedown Requests

A tool maintainer may request removal of their own tool's entry. Requests are honoured unless doing so would materially harm the commons (e.g. the tool is widely referenced in RFCs and archive posts).

If honoured, the entry is moved to `archived/` with a `removed_at_request` note. The historical record is preserved, but the entry no longer appears in the live Map.

Takedown requests from parties other than the maintainer -- including legal threats, competitors, or third parties -- require steward rough consensus before action. The commons does not remove entries based on pressure alone.

## Amendments

This document is amended only through an RFC. Substantive changes are summarised in the Archive under the RFC digest that produced them.

---

*The Map is only as useful as the discipline behind its entries. Curate accordingly.*
