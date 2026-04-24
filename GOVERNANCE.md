# Governance

FTWR is a community-stewarded commons. This document describes how decisions get made, who makes them, and how the commons outlives any individual steward.

Governance is short on purpose. A commons this size does not need a constitution. It needs just enough process to stay legitimate, transferable, and resistant to capture.

## Principles

- **Transparency over trust.** Every decision that shapes the commons happens in public through RFCs, PRs, and forum threads. No backchannels.
- **Attribution over authority.** Contributors are credited by handle on every artifact they touch. Authority accrues to handles that consistently show up, not to whoever claims it loudest.
- **Process over personality.** The commons should survive any steward walking away. Every process documented here can be executed by a new steward pool from a cold start.
- **Rough consensus, not votes.** Decisions are made when objections have been heard and addressed, not when a majority has clicked a button. Silence is not consent; an actively engaged contributor who disagrees is a blocker until addressed.

## Roles

### Contributors

Anyone who opens a PR, drafts an RFC, reviews an entry, or posts substantively on the forum. No application required. Credit accrues to the handle used on GitHub and the forum.

### Stewards

A small pool (target: 2-5) of handles with commit access to the `ftwr-dev` organisation and moderation rights on `community.ftwr.app`. Stewards:

- Merge PRs against `ftwr-map`, `ftwr-starters`, `ftwr-rfcs`, and `ftwr-site`
- Shepherd RFCs through the lifecycle
- Moderate the forum per `CODE_OF_CONDUCT.md`
- Maintain the Ledger and publish quarterly transparency summaries
- Cover infrastructure tasks (domain renewal, Discourse upgrades, CI maintenance)

Stewards are anonymous, rotating, and listed publicly on `ftwr.app/stewards` with handle, join date, and areas of focus.

### The Founding Steward

Until a second steward joins, a single Founding Steward holds all steward responsibilities. The Founding Steward commits in advance to:

- Ship the governance documents, the Map schema, and RFC-0001 before opening contribution
- Propose a second steward via RFC as soon as a qualified contributor emerges
- Step aside gracefully if and when the steward pool votes to replace them

Until a second steward joins, the Founding Steward's decisions are unilateral by necessity but must still be documented publicly (RFCs, PR descriptions, forum posts).

## Decision-Making

### Everyday decisions (PRs, forum moderation)

Any steward can merge, close, or moderate. Disagreement between stewards is resolved by opening a forum thread in Meta and seeking rough consensus.

### Structural decisions (RFCs)

Anything that changes how the commons itself operates -- Map categories, curation policy, funding rules, steward additions, infrastructure changes -- goes through an RFC. See `ftwr-rfcs/README.md` or RFC-0001.

RFC lifecycle:

1. **Draft.** Any contributor opens a PR to `ftwr-rfcs` with a new numbered RFC. A forum thread in RFCs is opened for discussion.
2. **Discussion.** Minimum 7 days open for public comment. Longer for substantive changes.
3. **Decision.** Rough consensus of active stewards, taking the forum discussion into account. "Accepted" if no unaddressed objections remain; "rejected" or "withdrawn" otherwise.
4. **Merge.** Accepted RFCs are merged with their final status; rejected RFCs are merged with their rejection rationale (the record matters as much as the outcome).

### Disputes

If a steward and a contributor disagree on a Map entry, a PR, or a forum moderation call:

1. Move the discussion to a forum thread in Meta.
2. Invite other stewards and engaged contributors to weigh in.
3. If unresolved after 14 days, a steward may escalate to an RFC for a binding policy update.

No steward unilaterally reverses another steward's decision without going through this process.

## Steward Additions and Removals

### Adding a steward

Proposed via RFC. The proposal names the candidate handle and summarises their contribution history (merged PRs, RFCs authored or discussed, forum presence). Existing stewards decide by rough consensus, with the forum thread visible throughout.

A candidate is typically eligible after 60+ days of consistent contribution across at least two of: Map PRs, RFCs, forum moderation, archive writing.

### Stepping down

A steward may step down at any time by announcing it in a forum thread in Meta. Their handle is moved to an "Alumni" section on `ftwr.app/stewards`. No ceremony required.

### Removing a steward

Proposed via RFC only in cases of: extended absence (60+ days with no contribution and no communication), violation of `CODE_OF_CONDUCT.md`, or actions that meaningfully damage the commons. Requires rough consensus of the remaining stewards.

## Conflict of Interest

Stewards and contributors must disclose any material interest in a Map entry or an RFC outcome. Examples:

- You build or maintain a tool being proposed for The Map
- You are paid by a vendor whose tool is in The Map
- You are affiliated with an entity that would benefit from an RFC outcome

Disclosure goes in the PR description or RFC preamble. Disclosed interests do not automatically disqualify participation, but they are weighed in review. Undisclosed interests that come to light are grounds for removal of the affected entry or RFC, and for sanctions up to and including steward removal.

## Infrastructure and Funds

All funds flow through Open Collective at `opencollective.com/ftwr` under a fiscal host. No individual steward holds funds directly. Stewards have spend authority up to amounts set via RFC (current policy: any single expense over $100 requires prior disclosure in Meta).

The Ledger on `ftwr.app/ledger` is updated monthly and reconciled against Open Collective quarterly.

Infrastructure keys (domain registrar, Vercel, Discourse admin, Open Collective admin) are held by at least two stewards once the steward pool reaches two. Until then, the Founding Steward holds them alone and publishes a recovery plan in a private note to the fiscal host.

## Handover

If all stewards become unreachable for 60+ consecutive days, the fiscal host and Open Collective Foundation are authorised to:

1. Announce the dormancy publicly via the forum and Archive
2. Accept applications from new stewards via an open call
3. Restore steward access after a 30-day public comment period

Infrastructure is deliberately kept portable: The Map is a git repo, the archive is a static site in git, the forum exports cleanly, Open Collective is platform-agnostic. A new steward pool can pick up from the artifacts alone.

## Amendments

This document is amended only through an RFC. All prior versions remain in git history. Substantive changes are summarised in the Archive under the RFC digest that produced them.

---

*Governance is the promise that the commons is more than its current stewards.*
