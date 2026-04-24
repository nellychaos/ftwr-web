# Contributing to the Commons

FTWR is a community commons for sports data modelling. The commons is made by its contributors. This document describes the five ways to contribute and what to expect from each.

Before contributing, read:

- [`GOVERNANCE.md`](GOVERNANCE.md) -- how decisions are made
- [`CURATION.md`](CURATION.md) -- editorial policy for The Map
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) -- expected conduct
- [`DISCLAIMER.md`](DISCLAIMER.md) -- scope and responsibility

## 1. Add to The Map

The Map is a curated directory of tools, datasets, papers, and libraries relevant to sports modelling. Contributions to The Map are the most common and most valued form of participation.

**To add an entry:**

1. Open a PR against `ftwr-map` adding a new entry. Use the PR template -- every field is required.
2. Confirm the entry meets the criteria in `CURATION.md`: genuine utility, verifiable, neutrally described, non-redundant, appropriately categorised.
3. Disclose any material interest in the tool being added (see `GOVERNANCE.md` § Conflict of Interest).
4. Wait for CI to validate the schema. If validation fails, fix the entry and re-push.
5. A steward will review within 5 business days. Expect questions, description edits, or category reassignment.
6. On merge, your handle becomes the entry's `contributor` field, permanently part of the commons' public record.

**To edit an existing entry:**

Same process. Common edits: refreshing the `last_verified` date after confirming the tool still behaves as described; improving a neutral description; correcting a broken URL; adjusting tags. Substantive changes (re-categorising, rewriting descriptions) are reviewed the same as new entries.

## 2. Ship a Starter

The Starters are minimal runnable reference implementations of canonical methods. A Starter is not a proprietary tool; it is an educational scaffold that points to the canonical academic or industry implementation it is teaching.

**A good Starter:**

- Implements one canonical method (Poisson goal model, Elo, Dixon-Coles, Kelly, closing-line value, etc.)
- Runs in under a minute on sample data included in the repo
- Is under ~150 lines of code for the core method (READMEs, tests, and utilities do not count)
- Cites the canonical paper or industry source it is teaching
- Includes at least one passing test and CI configured to run it
- Declares its license explicitly (MIT unless there is a reason otherwise)

**To propose a new Starter:**

1. Open an issue on `ftwr-starters` proposing the method, the canonical reference, and a sketch of what the scaffold will demonstrate. A steward will respond confirming fit or suggesting adjustments.
2. Once greenlit, open a PR with the Starter. Include a `README.md` walkthrough and at least one test.
3. After merge, the steward will ping the Archive maintainer about pairing the Starter with an explainer post, credited to your handle.

## 3. Draft an RFC

RFCs are numbered, dated methodology proposals. They are how the commons evolves its own practices -- backtest protocols, data quality standards, curation rules, governance changes.

**A good RFC:**

- Addresses a real gap, not a hypothetical concern
- States the problem before proposing the solution
- References prior art (papers, existing RFCs, prior forum discussion)
- Names trade-offs honestly -- what the proposal costs, not only what it gains
- Proposes something specific enough to merge as policy

**To draft an RFC:**

1. Review existing RFCs in `ftwr-rfcs` to understand the format.
2. Open a thread in the forum's **RFCs** category describing the problem and sketching your proposal. Solicit early feedback before writing the full draft.
3. Open a PR against `ftwr-rfcs` with the draft. Use the next available RFC number (stewards will reassign if there is a collision).
4. The draft is open for discussion for a minimum of 7 days. Longer for substantive changes.
5. Stewards decide by rough consensus. Accepted RFCs are merged with status `accepted`; rejected RFCs are merged with status `rejected` and a rationale. The record matters as much as the outcome.

Any contributor can draft an RFC. Steward participation is not required for submission.

## 4. Answer on the Forum

The single highest-leverage contribution is a good answer to a stranger's real question. Forum threads are indexed by search engines. A good answer becomes permanent public infrastructure for modellers who will find the thread months or years from now.

**How to contribute:**

- Read before you post. Many questions have been answered already; link rather than re-answer.
- Quote the specific claim or question you are responding to. Long threads drift without anchors.
- Show your work. A claim without reasoning is not an argument.
- Credit prior discussion and prior contributors when building on their ideas.
- Respond to your own threads. If you got an answer that helped, say what you ended up doing.

Forum contribution builds Discourse trust level, which promotes quality contributors automatically. Consistent forum presence is one of the paths to being considered for steward status.

## 5. Write for the Archive

The Archive is the long-form record. Tool explainers, method walkthroughs, RFC digests, tool comparisons, case studies, State-of-the-Commons retrospectives.

**Guest posts are welcomed.** The bylines are handles, not real names. Contributions are credited in the post frontmatter and visible on the archive index.

**Archive post standards:**

- No first-person builder voice ("I built X"). Institutional voice ("the commons now indexes X in §03").
- No hype, no guarantees, no selling. See `CURATION.md` § Neutral Description -- the same discipline applies to Archive prose.
- Every claim has a reference, a link, or a worked example.
- Acknowledge limitations honestly.
- Code blocks run. Data cited is real. No fabrication.

**To submit a post:**

1. Open an issue on `ftwr-site` proposing the topic, your planned structure, and any Map entries or RFCs it will reference. A steward will confirm fit.
2. Open a PR adding your MDX file under `blog/src/content/blog/`. Use the frontmatter template (see existing posts). Set `author` to your handle.
3. Editorial review focuses on accuracy, neutrality, and alignment with `CURATION.md` standards. Expect edits.
4. On merge, your post is live. Your handle appears on the byline, and the archive index credits you.

## Pull Request Etiquette

Applies across all `ftwr-dev` repositories:

- One logical change per PR. Map entries are the exception -- batching related additions is fine.
- PR descriptions explain the why, not just the what.
- Respond to review comments within a week. PRs with no response for 30+ days may be closed as stale (you can always reopen).
- Do not resubmit a closed or rejected PR without addressing the reason it was closed.
- No dependencies added without an issue discussion first.
- No placeholder or stub implementations. If something is not ready, explain why in the PR.

## Recognition

Contributors are credited in three visible places:

- **The Map.** Every entry carries the contributor handle who added or last edited it.
- **The Archive.** Every post has a byline by handle. Contributor pages list all posts by that handle.
- **The RFCs.** Every RFC preamble names its author(s).

There are no badges, no leaderboards, no gamified ranks. The credit is the credit. Over time, a handle's contribution history across the commons is itself a reputation -- one that compounds without needing any centralised promotion system.

## Steward Path

A contributor consistently active across at least two of (Map PRs, RFCs, forum moderation, Archive writing) for 60+ days may be proposed as a steward via RFC. See `GOVERNANCE.md` § Steward Additions.

Stewardship is not a reward for contribution volume. It is an ongoing responsibility for the commons. A contributor can be highly valued without ever becoming a steward, and most contributors will be.

## Questions

If anything in this document or the commons is unclear, open a thread in the forum's **Meta** category. Clarifications often become amendments to this document via RFC.

---

*The commons is built by the PRs that get merged, the RFCs that get debated, and the forum answers that help the next person. Thank you for contributing.*
