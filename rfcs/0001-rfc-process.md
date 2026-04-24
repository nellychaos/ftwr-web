---
rfc: 0001
title: "The RFC process"
author: "@founding-steward"
status: accepted
created: 2026-04-23
merged: 2026-04-23
discussion: "https://community.ftwr.app/t/rfc-0001-the-rfc-process"
supersedes: null
superseded_by: null
---

# RFC-0001: The RFC process

## Summary

FTWR adopts a lightweight RFC process for all decisions that change how the commons itself operates. RFCs are numbered, dated, publicly discussed on the forum, and merged into `ftwr-rfcs` with their final status recorded. This RFC is the first self-documenting artifact of that process.

## Motivation

A commons needs visible process. Without one, three failure modes are near-certain:

1. **Capture.** A single steward -- even an honest one -- accumulates undocumented decisions that are hard for new contributors to discover or challenge.
2. **Drift.** Policies change through informal consensus in DMs or forum threads that nobody can find later. Two years in, "why is this the rule" has no recoverable answer.
3. **Opacity.** Contributors cannot judge whether to invest effort in the commons without understanding how decisions get made. Opaque governance is indistinguishable, from outside, from arbitrary governance.

The RFC process is the smallest mechanism that addresses all three. It does not require voting infrastructure, membership rolls, or formal governance software. It requires only that structural decisions be written down, numbered, discussed in public, and merged with their outcome recorded.

FTWR draws on the Python PEP process, the Rust RFC process, and the IETF RFC tradition. The commons is smaller than any of those, so the process is correspondingly lighter.

## Proposal

### Scope

An RFC is required for:

- Changes to `GOVERNANCE.md`, `CURATION.md`, `CODE_OF_CONDUCT.md`, or `DISCLAIMER.md`
- Adding or removing Map categories
- Changes to curation criteria or review process
- Adding, removing, or promoting stewards
- Changes to the Ledger policy or funding rules
- New methodology standards (backtest protocols, data quality rules, model evaluation criteria)
- Structural changes to the Archive or Forum category layout
- Any other change that affects how the commons itself operates

An RFC is not required for:

- Individual Map entry additions, edits, or removals (normal PR process)
- New Starters (issue + PR)
- Archive posts (issue + PR)
- Forum answers, moderation calls on specific posts, routine verification refreshes, typo fixes, CI maintenance

Heuristic: if reasonable people could disagree about whether the change is the right policy for the commons, write an RFC.

### Numbering

RFCs are zero-padded four-digit numbers assigned at PR creation in monotonic order. Collisions on simultaneous PRs are resolved by stewards, who reassign the later PR to the next available number.

Numbers are never reused, even for rejected or withdrawn RFCs. The record includes failures.

### File format

One markdown file per RFC, named `NNNN-short-slug.md`, placed in the `ftwr-rfcs` repository (currently `/rfcs/` in the monorepo pending spin-out).

Each RFC starts with YAML frontmatter containing: `rfc`, `title`, `author` (handle), `status`, `created`, `merged`, `discussion` (forum thread URL), `supersedes`, and `superseded_by`. See `0000-template.md` for the canonical template.

### Lifecycle

1. **Idea (optional, recommended).** The author opens a thread in the forum's RFCs category describing the problem and sketching a proposal. This surfaces objections and prior art before a full draft is written.
2. **Draft.** The author opens a PR against `ftwr-rfcs` adding a new RFC file, using the template. The PR description links to the forum thread. Status: `draft`.
3. **Discussion.** A minimum of 7 days from PR opening. Substantive proposals (governance changes, major curation policy, steward additions) stay open longer -- typically 14-30 days. Discussion happens on the forum thread, not in PR comments, so it remains publicly searchable and indexable.
4. **Decision.** Active stewards post their position in the forum thread. Rough consensus means no unaddressed objections from active participants remain. If disagreement persists, the author may revise the proposal, narrow its scope, or withdraw it.
5. **Merge.** The RFC is merged with its final status:
   - `accepted`: policy is now in effect. Follow-up implementation actions proceed per the RFC's Adoption Plan.
   - `rejected`: policy is not adopted. The RFC is merged with a rationale so the reasoning is part of the record. A rejected RFC may be re-proposed later only with material new information.
   - `withdrawn`: the author pulled the RFC before a decision. Content preserved.

No RFC is closed without merging. The outcome is part of the public record.

### Authority

Decisions are made by rough consensus of active stewards. "Active" means stewards who have contributed to the commons (any merged PR, forum post, or RFC participation) in the 60 days prior to the decision.

Until the steward pool reaches two, the Founding Steward acts alone but is still bound by the process: draft in public, discuss for at least 7 days, merge with status recorded. Unilateral decisions are still documented decisions.

### Discussion venue

Forum threads in the **RFCs** category. One thread per RFC. PR comments are for code-level issues (typos, formatting, broken links); substantive discussion goes on the forum to stay public and searchable.

### Superseding

An RFC may supersede an earlier RFC. The superseding RFC references the prior by number in its `supersedes` frontmatter; the prior RFC is updated with `superseded_by` pointing to the new one. The prior RFC is not deleted or rewritten; the record is preserved.

### Amendments to this process

Amending the RFC process itself requires an RFC. This is deliberate: the rules change the same way any other rule changes.

## Rationale and Alternatives

### Why not Discord/chat for decisions?

Because Discord is where knowledge goes to die. Decisions made in a chat thread vanish into scroll. Two months later, nobody can cite the decision, and nobody can find the reasoning. The RFC process is deliberately anti-chat.

### Why not GitHub Discussions instead of Discourse?

GitHub Discussions are tied to a specific repository and do not index as well in search engines. Discourse provides category structure, trust levels, long-form formatting, and full-text search. It also survives GitHub's policies independently.

### Why not voting?

Voting requires a roll of eligible voters. A commons with anonymous contributors and rotating stewards cannot maintain such a roll without creating gatekeeping infrastructure that would itself corrupt the project. Rough consensus avoids the ballot problem and forces objections to be substantive -- a vocal objector with no reasoning is not a consensus blocker.

### Why require a minimum 7-day discussion window?

Shorter windows let urgent-feeling decisions bypass substantive review. Longer minimums (14+ days) create friction for low-stakes RFCs. Seven days is the smallest window that reliably catches objections from contributors who do not check the forum daily.

### Why preserve rejected RFCs?

Because rejection is a decision, and decisions are the commons' public record. A future contributor proposing a similar idea deserves to find the prior rejection and either address its reasoning or accept it. Silently closing rejected proposals loses institutional memory.

### What if stewards disagree?

The author may revise, narrow, or withdraw. If a proposal cannot achieve rough consensus after revision, it does not ship. This is working as intended: a commons is better served by inaction than by contested policy that half its stewards do not support.

## Prior Art

- **Python PEP process** (PEP-1, 2000): numbered, written proposals with a BDFL-delegate model. FTWR adopts the numbering and written-discussion discipline but not the delegated authority.
- **Rust RFC process** (2014): numbered RFCs with a discussion window and team-based decisions. FTWR adopts the lifecycle and public-discussion requirement.
- **IETF RFC tradition** (1969-): the original numbered technical proposal process. Even rejected IETF RFCs remain in the record.
- **Django governance** (DEP process, 2015): adopted many PEP conventions for a smaller project; demonstrates that the RFC model scales down.

FTWR is smaller than any of these. The process here is deliberately lighter than Python's PEPs or Rust's RFCs. It can become heavier via amendment if the commons outgrows the current form.

## Unresolved Questions

- **What counts as "active" steward participation for decision authority?** The current definition (any contribution in 60 days) is conservative. May need refinement via future RFC.
- **What happens if a rejected RFC is re-proposed?** Current policy: "only with material new information." "Material" is undefined. A future RFC may formalise a re-proposal process.
- **Can an accepted RFC be rolled back?** Yes, via a superseding RFC. But the mechanics of complicated rollbacks (e.g. an accepted RFC whose adoption plan was only partially executed) are not specified.

These are deferred to future RFCs once the commons has enough operational experience to answer them.

## Impact

**Contributors.** Anyone can draft an RFC. No prior contribution history is required. The process is a way to propose changes, not a reward for seniority.

**Stewards.** Stewards are obligated to engage with RFCs in their stated window. Ignoring an RFC is not an allowed response; posting "I have no objection" or "I object because X" is required.

**The Map, Starters, Archive, Forum.** No operational change for day-to-day work. The process only activates when a change affects how the commons itself operates.

**Existing governance documents.** `GOVERNANCE.md`, `CURATION.md`, `CODE_OF_CONDUCT.md`, and `DISCLAIMER.md` already reference the RFC process. This RFC formalises what they reference.

## Adoption Plan

On merge:

1. This RFC file is merged with `status: accepted`. (Done, by merging this PR.)
2. The `rfcs/README.md` index is updated to reference this RFC as accepted.
3. The next RFC (RFC-0002, drafted to propose backtest protocol standards) is opened for discussion using this process.
4. Any future change to `GOVERNANCE.md`, `CURATION.md`, `CODE_OF_CONDUCT.md`, or `DISCLAIMER.md` requires an RFC referencing this one.

No migration is required. No existing artifact is changed by this RFC.

## Decision

- **Status:** accepted
- **Decided by:** @founding-steward (acting alone per the bootstrap provision in `GOVERNANCE.md`)
- **Rationale:** The commons needs a written process before it needs a second steward. This RFC provides the smallest workable process that documents its own amendment procedure. Future stewards inherit a functioning mechanism rather than a list of undocumented conventions.
