# FTWR -- 90-Day Launch Plan

Week-by-week execution plan for bringing the commons online. Assumes one anonymous steward doing everything, so pacing is deliberately conservative. The failure mode to avoid is not "going slow" -- it is stockpiling burnout in weeks 1-6 and going silent in weeks 7-12.

The strategy plan covers the "what and why." This document covers the "when and how."

---

## Current State

Landing page at `ftwr.app` is live. The map at `ftwr.app/map.html` renders a 51-tool directory from `tools.json`. The blog scaffold exists at `blog/` (Astro) with one post in the commons voice. The Discourse forum exists at `ftwr.discourse.group`, unconfigured. No GitHub org repos are published yet. No Open Collective. No governance docs.

Everything else starts from scratch, but the seed assets (landing, map, tools.json, manifesto post) are enough to anchor the commons framing from day one.

---

## Phase 1: Foundation (Weeks 1-3)

The goal of Phase 1 is to stand up the commons infrastructure and seed enough content that the first visitor sees a credible institution, not a side project. Nobody should land on an empty map, an empty forum, or an undocumented governance structure.

The steward's job in Phase 1 is not to publish original analysis. It is to build the scaffolding that lets contributors publish theirs.

### Week 1: Governance and Registry

**Publish the governance layer:**

- Draft and commit `GOVERNANCE.md`, `CURATION.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, and `DISCLAIMER.md` at the `ftwr-dev` org level. These are short, plain-English documents that describe how decisions get made, how map entries are reviewed, how PRs are handled, and what the commons will and will not do.
- Draft RFC-0001: the RFC process itself. Number format, lifecycle (draft → discussion → accepted/rejected/withdrawn), where discussion happens (forum thread per RFC), and what rough consensus means. Merging RFC-0001 is the first self-documenting act of governance.
- Register the GitHub org (`ftwr-dev`). Set the org bio, avatar, and one-line description in the commons voice. Do not create proprietary repos -- there are none to create.

**Stand up The Map as a proper registry:**

- Spin out `tools.json` into a new repo `ftwr-map`. Define a JSON schema (or YAML-per-entry) that requires: category, name, description (neutral, under 200 chars), url, tags, contributor handle, last-verified date, and optional license/sport fields.
- Write a PR template for map entries that requires the contributor handle and last-verified date. CI validates entries against the schema on every PR.
- The landing map continues to load from The Map. Publishing The Map as its own repo lets PRs flow from contributors without touching the site repo.

**Forum and funding:**

- Move Discourse to `community.ftwr.app` on the paid plan. Apply the light-mode brand tokens. Create the category structure from the strategy plan: Announcements, The Rabbit Hole, Show Your Work, Map, Methods & Models, Data Sources, Arbitrage & Edge, RFCs, Code Help, Meta.
- Open a fiscal-host Open Collective at `opencollective.com/ftwr`. No donation drive yet -- just the infrastructure.
- Draft the `ledger.html` page for the landing, even if empty. Commit it.

**No public posting this week.** No X account yet, no announcements.

Estimated time: 10-12 hours.

### Week 2: Starters and Seed Content

**Publish the first Starter:**

- Create `ftwr-starters`. First entry: a Poisson goal model in under 100 lines of Python that runs on a sample dataset in under a minute. README cites the canonical Dixon-Coles paper and a reference implementation. The point is not to out-build anyone -- it is to lower activation energy for a new modeller to see a working example.
- CI runs the starter's test on every push.

**Seed the Archive:**

- The manifesto post (`what-is-ftwr.mdx`) is live. Draft Archive Post 2: "How The Map Works" -- a plain-language walkthrough of what The Map is, how entries are reviewed, what `last-verified` means, and how to submit a PR. This is the canonical link for every PR reviewer going forward.
- Draft Archive Post 3: a method walkthrough based on the first Starter. "Poisson goal models in fifty lines" -- theory, runnable code, citations, honest limitations.

**Seed the Forum:**

- Post 4-6 real discussion topics as the steward. Not "welcome to the forum" -- actual content. Examples:
  - "Map: which tools would you add to §03 Models & Methods?" (in Map)
  - "RFC-0001 is open for discussion. What's missing?" (in RFCs)
  - "Dixon-Coles vs base Poisson: when does the low-score correction matter?" (in Methods & Models)
  - "Share your odds-data workflow: APIs, scrapers, quality checks" (in Data Sources)
  - "What counts as a fair backtest?" (in Methods & Models, teed up for RFC-0002)

Estimated time: 10-12 hours.

### Week 3: Archive Launch and RFC-0001 Merge

**Archive goes live:**

- Deploy `blog.ftwr.app` with Posts 1-3 live on day one. A single-post archive reads as abandoned; three reads as established.
- RSS feed wired. Discourse configured to auto-post new archive entries as forum threads in Announcements.

**Governance lands:**

- Merge RFC-0001 after discussion settles. Write a short archive post digesting it. This is the first RFC digest in what will become a recurring format.
- Draft RFC-0002: backtest protocol standards. Open it on the forum for discussion. Do not rush to merge -- the process is the product.

**Landing refresh:**

- Confirm the hero is in commons voice (done). Confirm the four terminal links point to Map, Forum, Archive, Registry. Confirm the map loads without the empty-state bug (fixed).
- Add a "Ledger" nav link pointing to the placeholder page.

**Handles and accounts:**

- Register the X account under a neutral handle. No posting yet. Bio: "A commons for sports data modelling. Map, forum, archive, starters. MIT. Free." Link to `ftwr.app`.
- Create the subreddit outpost. Sidebar in institutional voice, rules mirroring `CODE_OF_CONDUCT.md`, flair categories aligned to map sections. No posting yet.

Estimated time: 8-10 hours.

---

## Phase 2: Soft Launch (Weeks 4-6)

Phase 2 opens the broadcast channels. The goal is not follower count -- it is discovering the first 20-30 people who recognise the commons for what it is and join the forum.

### Week 4: Go Live on X

**First public posts:**

- Pin a thread that explains what FTWR is in five posts: (1) commons framing, (2) The Map, (3) starters and RFCs, (4) governance and funding, (5) how to contribute. Link to landing, forum, map.
- Begin steady posting. Aim for 3-5 substantive posts per week, not daily. Institutional voice: "Map updated: 4 entries added to §02." "RFC-0002 is open for discussion." "Starter released: Poisson in fifty lines. Code and walkthrough in the Archive."
- Publish Archive Post 4: a tool comparison. "Three odds APIs, same weekend, same markets" -- neutral, data-driven, each provider linked to its map entry.

**Ongoing cadence from this point:**

- X: 3-5 posts/week, institutional voice, every post links to Map / Archive / Forum / RFC where relevant.
- Archive: 1 post/week, consistent day.
- Map: at least one PR merged per week (self-reviewed initially, community-reviewed as contributors arrive).
- Forum: 2-3 new topics or substantive replies per week. Respond to every post from a non-steward.
- Ledger: publish first transaction log, even if it is just "domain renewal: $15."

### Week 5: First Contributor Surfaces

- Publish Archive Post 5: "Open problems in sports modelling." Frame five unsolved questions as invitations. Each one could become an RFC draft, a starter, or a Map addition. Cross-post to r/sportsbook and r/datascience with a forum link for discussion.
- Merge RFC-0002 if discussion has settled. Publish the RFC digest as Archive Post 6.
- Reach out (via forum DM or X reply, never cold DM) to any non-steward who has posted something substantive. Invite them to open a PR against `ftwr-map` or draft an RFC.

### Week 6: Checkpoint

**By the end of week 6:**

- 6+ archive posts live
- Map has grown past the initial 51 entries (target: 60+) with at least one non-steward contributor
- 2 RFCs merged, 1 in discussion
- 1 starter published, second one drafted
- 10+ forum topics with non-placeholder content
- Ledger publicly showing at least the domain cost

If any of these are behind, this is the week to catch up before Phase 3. If the steward is behind because of time, cut X cadence first, then archive cadence. Never cut The Map or forum.

---

## Phase 3: Contribution Drive (Weeks 7-12)

Phase 3 is where the commons either begins to function as one or remains a well-dressed solo project. The goal is to get other people contributing: merging map PRs, drafting RFCs, posting on the forum, submitting starters.

### Weeks 7-8: Invite Contribution Explicitly

**Map:**

- Tag 5-10 "good first contribution" issues on `ftwr-map`: gaps in specific categories, entries that need their `last-verified` date refreshed, neutral descriptions that need a neutral rewrite.
- Publish Archive Post 7: "How to add to The Map" -- a step-by-step walkthrough of opening a PR. Screenshots, not prose. Link it from The Map README and the forum.

**Forum:**

- Open a Show Your Work thread inviting people to share their own analysis, models, or data pipelines. Tone: low barrier, even rough drafts welcome. The first three non-steward posters set the culture.
- Respond to every forum post personally but in institutional voice -- "the commons appreciates this contribution," not "I loved this."

**Starters:**

- Publish a second starter: Elo ratings in under 100 lines, cited to Glickman. Archive post walks through it.

### Weeks 9-10: First Community Drive

Run a time-boxed Map Drive. Two weeks. Goal: 20 new contributor-submitted map entries, each with an attribution and a verified date.

- Announce on X with a thread. Cross-post the announcement as a forum topic. Pin both.
- Feature contributors in a weekly Archive digest ("Map Drive, Week 1: 8 entries added, thanks to @handle-1, @handle-2, @handle-3").
- Do not promise any reward beyond attribution and a highlight in the Archive. A commons works when credit is the currency.

**Simultaneously:**

- Draft RFC-0003: map review cadence (how often entries get re-verified, how deprecations happen). Open for discussion.
- Publish Archive Post 9: a guest post from the first non-steward willing to write one. Byline is their handle. If nobody volunteers, the drive itself becomes the post.

### Weeks 11-12: Assess, Document, Adjust

**Honest metrics review:**

Map:
- How many PRs from non-steward contributors were merged?
- How many unique contributor handles now have at least one map entry?
- What percentage of entries have a `last-verified` date within the last 90 days?

Forum:
- How many non-steward posters in the last 30 days?
- Have any conversations happened between two non-steward accounts?
- Has anyone reached Discourse Trust Level 2?

RFCs:
- How many drafts exist? How many are merged? How many came from non-stewards?

Archive:
- Which posts got organic search traffic?
- Has anything been cited or linked by another site?

Ledger:
- Did Open Collective receive any donations? Even $5 is signal.
- Are running costs covered by donations, or subsidised by the steward?

**Document and adjust:**

- Publish Archive Post 12: "State of the Commons, Day 90." Be transparent. What worked, what did not, what gets dropped, what gets doubled down on. This post invites the community to shape the direction.
- If the ledger is funded, thank donors by handle on the Ledger page.
- If a second steward candidate has emerged -- someone who has contributed PRs, drafted or discussed RFCs, and engaged consistently on the forum -- open an RFC proposing their addition to the steward pool. If nobody has reached that threshold, that is fine. It is a three-month-old commons.

---

## Weekly Time Budget (Ongoing from Week 4)

The commons framing reduces sustained effort versus a builder persona, because there are no proprietary codebases to maintain. Target:

| Activity | Hours/Week | Notes |
|---|---|---|
| Map curation and PR review | 2 | Merge contributor PRs, refresh `last-verified` dates, categorise new entries |
| Archive writing | 2-3 | 1 post/week, 2 sessions (draft, edit) |
| Forum moderation and replies | 1-2 | Respond to everything, seed a new topic if quiet |
| RFC drafting and discussion | 1 | Avg across weeks -- some weeks zero, some weeks intense |
| X posting | 1 | 3-5 posts, batch-write Sunday |
| Starters maintenance | 0.5 | As needed, minimal |
| Ledger updates | 0.25 | When Open Collective receives a transaction |
| **Total** | **~8** | |

If the steward consistently spends more than 10 hours, something is wrong. Most likely culprit: over-investing in X. Cut X before anything else.

---

## Content Pipeline

### Archive Post Backlog (First 12 Weeks)

Every post teaches something or documents the commons. No picks, no first-person builder voice, no hype.

1. **What Is FTWR** -- manifesto (done, in commons voice)
2. **How The Map Works** -- curation, attribution, review
3. **Poisson Goal Models in Fifty Lines** -- first starter walkthrough
4. **Three Odds APIs, Same Weekend** -- neutral tool comparison
5. **Open Problems in Sports Modelling** -- invitation piece
6. **RFC-0002 Digest: Backtest Protocols** -- governance in action
7. **How to Add to The Map** -- step-by-step contribution guide
8. **Elo Ratings in Fifty Lines** -- second starter walkthrough
9. **Map Drive: Week 1 Digest** -- contributor highlights
10. **Guest Post** (first non-steward author, byline by handle)
11. **How the Ledger Works** -- transparency in action
12. **State of the Commons, Day 90** -- honest retrospective

### Forum Seeding Topics (First 3 Weeks)

Align to Map and RFC categories. No "what are you building" framing -- instead, neutral discussion starters that a commons would convene.

- "Map: what tools would you add to §03 Models & Methods?" (Map)
- "RFC-0001 is open -- what's missing from the RFC process?" (RFCs)
- "Dixon-Coles vs base Poisson: when does the low-score correction matter?" (Methods & Models)
- "Share your odds-data workflow: APIs, scrapers, quality checks" (Data Sources)
- "What counts as a fair backtest?" (Methods & Models, tees up RFC-0002)
- "Arbitrage detection: state of the open-source tooling" (Arbitrage & Edge)

### X Content Formats (Rotation)

Institutional voice. Every post links back to map, archive, forum, or RFC. No hot takes, no picks, no parasocial engagement.

- **Map update.** "4 tools added to §02 this week. Review by @handle. Browse: ftwr.app/map"
- **RFC announcement.** "RFC-0002 open for discussion. Topic: backtest protocol. Thread: community.ftwr.app/..."
- **Starter release.** "Starter released: Poisson in fifty lines, cited, tested. Code + walkthrough: blog.ftwr.app/..."
- **Archive post.** Standard link-with-summary.
- **Contributor highlight.** "This week The Map gained entries from @handle-1, @handle-2, @handle-3. Thanks."
- **Down the Rabbit Hole** (optional, no more than twice a month). Short institutional thread starting from one observation, pulling on it with references to map entries and archive posts.

---

## Launch Checklist

### GitHub Org (ftwr-dev)

- [ ] Org created, avatar and description in commons voice
- [ ] `GOVERNANCE.md`, `CURATION.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `DISCLAIMER.md` committed
- [ ] `ftwr-map` repo: schema, PR template, CI validation, initial entries migrated from `tools.json`
- [ ] `ftwr-starters` repo: at least one runnable starter with tests
- [ ] `ftwr-rfcs` repo: RFC template, RFC-0001 merged, RFC-0002 drafted

### Archive (blog.ftwr.app)

- [ ] Deployed, brand tokens applied, 0px radius enforced
- [ ] 3+ posts live at public launch
- [ ] RSS feed wired; Discourse auto-posts new entries as Announcements threads
- [ ] Sitemap submitted to search

### Forum (community.ftwr.app)

- [ ] Moved to paid Discourse hosting under `community.ftwr.app`
- [ ] Brand tokens applied
- [ ] Categories created (Announcements, The Rabbit Hole, Show Your Work, Map, Methods & Models, Data Sources, Arbitrage & Edge, RFCs, Code Help, Meta)
- [ ] Welcome topic in commons voice, linking to governance docs
- [ ] 4-6 seed topics posted, all substantive
- [ ] GitHub webhook integration (optional, can follow)

### Landing (ftwr.app)

- [ ] Hero in commons voice (done)
- [ ] Terminal links: Map, Forum, Archive, Registry (done)
- [ ] Map loads 51+ entries without errors (fixed)
- [ ] Ledger nav link present, page exists (even if minimal)

### Ledger (opencollective.com/ftwr)

- [ ] Fiscal host selected and application submitted
- [ ] Page live, even if balance is $0
- [ ] First expense logged (domain renewal)

### X

- [ ] Handle registered under neutral name
- [ ] Profile picture, banner, bio in commons voice
- [ ] Pinned thread explaining the commons (5 posts)

### Reddit

- [ ] Subreddit created, sidebar in commons voice
- [ ] Rules mirror `CODE_OF_CONDUCT.md`
- [ ] Flair categories aligned to map sections

---

## What Success Looks Like at Day 90

Realistic, not aspirational. A 90-day-old commons with one steward is a small thing. The question is whether it is a real thing.

**Minimum viable success (the commons is working):**

- Map has 70+ entries, at least 5 from non-steward contributors
- RFC-0001 and RFC-0002 merged; RFC-0003 in discussion
- 2 starters published with passing tests
- 12+ archive posts live, at least one getting organic search traffic
- Forum has 20+ registered members, 5+ non-steward posters, at least one conversation between two non-stewards
- Ledger shows at least one public donation cycle

**Strong success (ahead of pace):**

- A non-steward has drafted an RFC that was discussed and merged or shaped by discussion
- A guest post has been published in the Archive, credited by handle
- An archive post is ranking on page 1 of Google for a relevant search term
- At least one steward candidate has emerged (consistent PRs, RFC discussion, forum presence)
- Map entries have been cited or linked from outside FTWR

**The one signal that matters most:** has someone the steward has never met contributed to the commons? Map PR, starter contribution, RFC draft, or substantive forum answer -- any one of those, from a stranger, means FTWR is a commons. Zero of those after 90 days means it is still a well-designed solo project.

---

*The commons does not build itself, and it does not need to be deep to be real. It needs to be open enough that the curious can walk in without asking.*
