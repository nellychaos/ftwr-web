# RFCs

FTWR RFCs (Requests for Comment) are numbered, dated methodology proposals. They are how the commons evolves its own practices -- backtest protocols, data quality standards, curation rules, governance changes, anything that affects how the commons operates.

This directory will be spun out into its own repository (`ftwr-rfcs`) once the commons has a second steward. Until then, RFCs live alongside the other governance artifacts in the monorepo.

## Quick reference

| Field | Value |
|---|---|
| Numbering | Zero-padded four digits (RFC-0001, RFC-0042, RFC-0100) |
| File format | Markdown, one file per RFC, named `NNNN-short-slug.md` |
| Discussion venue | Forum thread in the **RFCs** category, one thread per RFC |
| Minimum discussion window | 7 days from draft PR opening |
| Decision authority | Rough consensus of active stewards, visible in the thread |
| Template | [`0000-template.md`](0000-template.md) |

## Lifecycle

1. **Idea.** A contributor opens a thread in the forum's RFCs category describing a problem and sketching a proposal. Optional but strongly encouraged -- it surfaces objections before a full draft is written.
2. **Draft.** The contributor opens a PR against this directory with a new RFC file using the template. The PR description links to the forum thread.
3. **Discussion.** Minimum 7 days. Substantive proposals stay open longer. Comments happen on the forum thread (not in PR comments) so the discussion is publicly searchable.
4. **Decision.** Active stewards post their position in the forum thread. Rough consensus means no unaddressed objections from active participants remain. If disagreement persists, stewards work with the author to revise, narrow, or withdraw.
5. **Merge.**
   - **Accepted:** the RFC file is merged with frontmatter `status: accepted` and the merge date recorded.
   - **Rejected:** merged with `status: rejected` and a brief rationale in the RFC body.
   - **Withdrawn:** merged with `status: withdrawn` if the author pulls it; content preserved for the record.

No RFC is simply closed without merging. The outcome, even if "rejected," is part of the public record and informs future proposals.

## What needs an RFC

- Adding or removing Map categories
- Changes to curation criteria in `CURATION.md`
- Changes to `GOVERNANCE.md`, `CODE_OF_CONDUCT.md`, or `DISCLAIMER.md`
- Adding, removing, or promoting stewards
- Changes to the Ledger or funding policy
- New methodology standards (backtest protocols, data quality rules, model evaluation criteria)
- Structural changes to the Archive or Forum category layout
- Anything else that changes how the commons itself operates

## What does not need an RFC

- Adding or editing individual Map entries (normal PR process)
- Adding new Starters (issue + PR)
- Writing Archive posts (issue + PR)
- Answering forum questions
- Fixing typos, broken links, or CI configuration
- Routine `last_verified` date refreshes

When in doubt: if reasonable people could disagree about whether the change is the right policy for the commons, write an RFC.

## Index

| RFC | Title | Status | Author | Merged |
|---|---|---|---|---|
| [0001](0001-rfc-process.md) | The RFC process | accepted | @founding-steward | 2026-04-23 |

## Authoring tips

- Keep it short. An RFC that requires 40 pages to defend is probably not yet a coherent proposal.
- State the problem before proposing the solution. If the problem is not widely recognised, spend time describing it before moving to the fix.
- Reference prior art: prior RFCs, academic papers, prior forum discussion, how other commons (Python PEPs, Rust RFCs, IETF RFCs) have handled similar questions.
- Name trade-offs honestly. Every policy costs something. If the draft reads as unambiguously good, it is hiding a trade-off.
- Write for the contributor who will read this two years from now, not only for the stewards deciding next week.

## Amendments

This README is amended only through an RFC. (Yes, amending the RFC process requires an RFC. That is the point.)
