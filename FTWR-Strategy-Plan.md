# Follow The White Rabbit (FTWR) -- Strategy Plan

## What This Is

FTWR is a community commons for sports data modelling. It curates tools, convenes discussion, and documents shared methods as public goods -- non-rival, non-excludable, MIT-licensed, anonymously stewarded. It is a map and a meeting hall, not a lab or a persona.

The premise is simple. Sports modelling knowledge is fragmented across private Discords, dead blogs, paywalled courses, and a handful of academic papers that never get implemented. Good tools are scattered across GitHub with no index. New modellers waste weeks finding what a community with shared memory could surface in minutes. FTWR is the shared memory.

The brand is sport-agnostic. The commons is about methods, not fixtures. Poisson distributions, Elo ratings, expected-value calculation, backtesting discipline -- these transfer across football, basketball, tennis, esports, or anything with a data trail and a price.

---

## Why a Commons

Individual edges erode. A model you build alone hits a ceiling set by your own time and blind spots. But the ability to *find* edges compounds when knowledge is pooled. Better indexes surface better tools. Better tools lower the activation energy for new modellers. More new modellers produce more analysis, more critique, more methods -- which improves the index again.

This loop only works if the commons stays open. The moment any layer becomes proprietary -- a paywalled tutorial, a "VIP" forum, a gated scanner -- the compounding stops and the incentives invert. Contributors stop contributing when someone else is capturing the value. Readers become customers. The commons becomes a funnel.

FTWR is explicitly built to avoid that failure mode. No paid tiers, no courses, no affiliate links, no sponsored entries in The Map, no consulting. Infrastructure costs are funded transparently through donations with a public ledger. The work itself stays free and open, forever.

---

## Brand Identity

### Brand Pillars

1. **The Commons** -- Tools, methods, and knowledge are public goods. FTWR curates and convenes; it does not hoard, gate, or resell. Every artifact is MIT-licensed, every entry is attributed, every decision is auditable.

2. **Show Your Work** -- No tips, no "trust me." Every claim has a reference. Every tool entry has a reviewer and a last-verified date. Every method has a runnable implementation or a link to one. Opacity is the enemy.

3. **Sharpen Together** -- Individual edges erode; collective literacy compounds. The community teaches the community. A good answer on the forum is worth more than a good post on the blog, because it creates the next answerer.

4. **Sport-Agnostic Methods** -- The Map is organised by technique, not by league. Poisson, Elo, Bradley-Terry, Dixon-Coles work wherever there are outcomes and prices. The commons is portable.

5. **Stewardship, Not Ownership** -- FTWR is stewarded, not owned. Maintainers are anonymous, rotating, and accountable through visible governance. Contributors get credit; nobody gets a crown. The project should be able to survive any single steward walking away.

### Tone and Voice

- **Curator, not builder.** The voice is the voice of a field guide or an observatory log -- precise, attributed, timestamped. "Added to The Map." "Reviewed by @handle." "Last verified 2026-04-23." Not "we built this cool thing."
- **Technical but accessible.** Code and stats are central, but writing reads like a well-kept wiki, not an academic paper and not a Twitter thread.
- **Confident through citation.** Authority comes from references, not from claims. If FTWR says a method has known limitations, the post links to the paper that establishes them.
- **Institutional reticence.** No hype, no guarantees, no first-person heroics. The rabbit-hole metaphor carries through as a call to curiosity, not as a mystique around any individual.
- **Contrarian only with evidence.** Willing to publicly disagree with consensus when the data supports it. Never contrarian for the aesthetic.

### Visual Identity

See `FTWR-Brand-Guide.md` for the full specification. The aesthetic is deliberately institutional -- research terminal, field guide, spectral observatory. Lean into it further:

- **Dewey-style numbering.** Map sections are §01 through §09. RFCs are RFC-0001, RFC-0002. Issues are referenced by number. Every durable artifact has an index.
- **Timestamps everywhere.** `last-reviewed`, `entry-added`, `rfc-status` dates are first-class UI, not footnotes. A commons proves it is alive through dates.
- **Contributor attribution as primary UI.** Every tool card shows who added it and who last reviewed it. Handles link to forum profiles. Credit is the currency.
- **Section names as nouns, not verbs.** Map. Archive. Ledger. Observatory. Index. Not "Tools / Blog / About."
- **Spectral gradient as the signature.** Teal to magenta (#006875 → #a900a9) is the one visual flourish. Everything else stays quiet.
- **0px border radius, JetBrains Mono for structure, Inter for prose, light mode only.** Unchanged. The discipline is the brand.

---

## The Public Goods We Produce

FTWR ships six artifacts, each with a clear role. None of them are proprietary. All of them are owned by the commons.

### 1. The Map -- Curated Directory

Repo: `ftwr-map`. The flagship artifact. A structured, versioned, PR-driven directory of tools, datasets, papers, and models relevant to sports analytics. Every entry has:

- A category (§01 Data Sources, §02 Odds & Markets, §03 Models & Methods, etc.)
- A one-paragraph neutral description
- A contributor handle
- A `last-verified` date
- Tags for sport, license, and use case
- A link to the canonical source

The Map is the most durable output of the project. It answers the question every new modeller asks -- "where do I even start?" -- in a way that compounds with every PR merged. `tools.json` in the current landing repo is the seed; The Map formalises it.

### 2. The Starters -- Reference Implementations

Repo: `ftwr-starters`. Minimal, runnable starter implementations of canonical methods -- Poisson goal models in 50 lines, Elo in 50 lines, closing-line-value calculation, Kelly sizing, bootstrap backtests. Each starter points to the canonical academic or industry implementation it is teaching.

The starters are not FTWR's proprietary tools. They are educational scaffolds. The point is lowering the activation energy for a new modeller to go from "I read about Dixon-Coles once" to "I have it running on real data in ten minutes."

### 3. The RFCs -- Methodology Proposals

Repo: `ftwr-rfcs`. A numbered, dated, public RFC process for methodology. Backtest protocols, data quality standards, model evaluation criteria, ethical guidelines for what counts as a fair comparison. RFCs are drafted by any contributor, discussed on the forum, and merged when rough consensus emerges.

This is the intellectual spine of the commons. Over time it becomes a citable body of shared standards -- "we backtested per RFC-0007" -- that no single operator could produce alone.

### 4. The Archive -- Blog

Repo: `ftwr-site` (this repo). The blog at `blog.ftwr.app` is the long-form archive. Content types:

- **Tool explainers.** Neutral, comparative walkthroughs of Map entries. "Five ways to fit a Dixon-Coles." "Comparing three odds APIs on the same weekend."
- **Method explainers.** Theory and runnable code for a specific technique. Linked to the corresponding starter.
- **RFC summaries.** When an RFC lands, a digest explains what changed and why.
- **Down the rabbit hole.** Digests of the most substantive forum threads from the week, credited to their participants.
- **Guest posts.** Community members publishing original analysis. Credited by handle. This is the real product.

The byline is never a real name. It is `Curator: @handle` or `Contributors: @handle, @handle`. The voice is institutional.

### 5. The Forum -- Meeting Hall

`community.ftwr.app` on paid Discourse hosting from day one. The forum is Tier 1, not a satellite. It is where the commons actually happens: questions get answered, RFCs get debated, new contributors meet reviewers. Categories align with The Map sections, plus Meta for governance and Announcements for releases.

Trust levels do the work of promoting quality contributors without manual curation. Level 3 (Regular) is earned, not granted. Level 4 (Leader) is the maintainer pool and is explicitly rotating.

### 6. The Ledger -- Public Accounting

Page at `ftwr.app/ledger`. Every dollar that comes into FTWR through Open Collective and every dollar that goes out is published. Discourse hosting, domain renewal, any shared data API subscription the community votes to fund -- all visible. This is how a commons funds itself without becoming a business: transparency substitutes for trust.

---

## Platform Strategy

### The Forum is Tier 1

Discourse is the home. This is the one place where the commons genuinely lives and breathes. Every other surface points here.

Why Discourse specifically:
- Indexed by Google. Answers to real questions become permanent public infrastructure. A good forum thread is worth more than a good blog post because it compounds in search and invites follow-up.
- Trust levels auto-promote quality contributors. Anonymity plus earned trust is exactly the governance model FTWR needs.
- Open source, exportable. No vendor lock-in.

Host on `community.ftwr.app` on the paid plan from day one. Splitting to `ftwr.discourse.group` signals "side project" and splits the domain's search equity.

**Category structure** (aligned to Map sections):

- **Announcements** -- Releases, RFC promotions, community updates
- **The Rabbit Hole** -- Open-ended deep dives on markets, methods, or anomalies
- **Show Your Work** -- Members post analysis, models, or findings for feedback. The culture-setting category.
- **Map** -- Proposals for new entries, deprecations, review disputes
- **Methods & Models** -- §03 discussion: statistical modelling, backtesting
- **Data Sources** -- §01 discussion: APIs, datasets, scrapers, quality issues
- **Arbitrage & Edge** -- §04/§05 discussion
- **RFCs** -- Active methodology proposals, one thread per RFC
- **Code Help** -- Technical support
- **Meta** -- Governance, ledger, how FTWR itself operates

### GitHub -- The Commons Registry

Organisation: `ftwr-dev`. Hosts the six artifacts above and nothing else. No personal projects, no speculative repos, no empty placeholders. Standards from day one:

- MIT license on everything
- Issue and PR templates that invite contribution and require attribution
- GitHub Actions CI on every repo (Map entries are schema-validated, starters run their tests, RFCs lint their frontmatter)
- `CONTRIBUTING.md`, `GOVERNANCE.md`, `CURATION.md`, and `CODE_OF_CONDUCT.md` on the org profile
- A public project board showing what is being worked on

### Blog -- The Archive

`blog.ftwr.app`. Astro, static, source in `ftwr-site`. Publishing cadence: one post per week, sustainable forever. Markdown-based so community members can submit posts via PR. Every post has a contributor handle in the byline, a `last-reviewed` date, and links to any Map entries or RFCs it references.

### X (Twitter) -- Discovery Outpost

Tier 3. The account is the public face of the commons, not of any individual. Content is institutional:

- Map updates ("5 tools added to §02 this week")
- RFC announcements
- Guest-post amplification
- Method threads that link to the corresponding starter and archive post
- Occasional "down the rabbit hole" threads highlighting forum activity

No hot takes, no picks, no parasocial engagement. Posting cadence is 3-5 substantive posts per week, not daily. The goal is to route the right people to the forum and archive, not to build a follower count.

### Reddit -- Secondary Discovery

Tier 3. A subreddit exists as an outpost for reach into r/sportsbook, r/sportsbetting, r/datascience. Cross-post archive content and link back to the forum. Do not try to build the community here.

---

## Anonymity and Stewardship

FTWR is anonymously stewarded as a matter of design, not convenience.

**Why anonymous:**
- A commons does not need a face. Wikipedia does not have a founder's headshot on the homepage.
- Anonymity forces the work to speak. If The Map is bad, no personal reputation insulates it. If it is good, no personal reputation captures the credit.
- It protects contributors in jurisdictions where sports-betting analysis is sensitive.
- It makes stewardship transferable. The project can outlive any individual steward.

**How stewardship works:**
- Maintainers operate under rotating handles (e.g. `curator-01`, `curator-02`). Each handle has a forum profile and a GitHub identity. Handles are not tied to real names and can be retired and replaced.
- The current steward pool is published on `ftwr.app/stewards` with handles, responsibilities, and join dates.
- New maintainers are proposed via RFC and added by rough consensus of existing maintainers.
- Decisions that affect the commons -- adding categories, changing the curation policy, accepting or refusing funding -- happen in public through RFCs. No backchannels.
- The project is legally anchored in an open collective fiscal host (Open Collective Foundation or similar) so donations can flow and infrastructure can be paid for without any individual holding the keys.

Anonymity without documented process is opaque. Anonymity with documented process is institutional. FTWR is the second thing.

---

## Funding as a Public Good

FTWR runs on Open Collective with a fiscal host. Every transaction is public.

**What donations pay for:**
- Domain renewals
- Discourse paid hosting
- Blog/landing hosting (likely free on Vercel indefinitely)
- Shared data API subscriptions the community votes to fund
- Occasional bounties for specific map work (proposed and approved via RFC)

**What donations never pay for:**
- Anyone's salary
- Promoted entries in The Map
- Advertising
- Closed-source infrastructure

**What FTWR does not take:**
- Sponsorship of Map entries
- Affiliate links anywhere on any surface
- Paid placement in the archive or forum
- Any money from sportsbooks, data vendors, or tipsters

The public ledger is the answer to every "how do we know?" question. Transparency is cheaper than trust and more durable.

---

## What FTWR Is Not

Worth stating plainly:

- **Not a tips service.** No picks, no plays, no "our model says bet this." The archive and forum discuss methods and market structure, not specific wagers.
- **Not a proprietary toolmaker.** FTWR does not publish an original scanner, an original model, or an original edge. It indexes and teaches; it does not compete with the tools in The Map.
- **Not a persona.** There is no founder to follow. Follow the work.
- **Not a business.** No revenue, no growth targets, no fundraising. Success is measured in contributors, not users.
- **Not a Discord replacement.** Not a chatroom, not a real-time community, not a vibes-based hangout. Asynchronous, indexed, archival.

---

## Risks and Mitigations

1. **Free-rider problem.** Public goods under-produce because readers outnumber contributors. Mitigate by making contribution low-friction (well-templated PRs to The Map), visible (every entry credits a contributor), and reciprocal (contributors get forum trust, archive bylines, and eventually maintainer consideration).

2. **Single-operator burnout.** The commons framing reduces this risk significantly compared to a builder persona -- a curator doing one review PR and one forum post per week is sustainable. But early on, before contributors arrive, the steward still carries most weight. Mitigate by ruthlessly scoping early artifacts and by seeding the forum with questions, not answers.

3. **Map disputes.** A tool vendor may dispute a review. A community member may push a low-quality entry. Mitigate with a documented `CURATION.md` policy: neutral descriptions, evidence-based reviews, public appeal via RFC, clear deprecation criteria. The process is the product.

4. **Legal and regulatory exposure.** Sports-betting legality varies by jurisdiction. Mitigate by keeping the framing strictly educational -- methods, tools, analysis -- and by never publishing specific wagers or directing users to place bets. A clear `DISCLAIMER.md` and geofencing-aware copy on the landing protect the commons.

5. **Capture by a single contributor's agenda.** A high-volume contributor could bend The Map or RFCs toward their own tools or methods. Mitigate with rotating maintainers, public review, and an explicit conflict-of-interest disclosure in `GOVERNANCE.md`.

6. **Commons collapse if stewards vanish.** Mitigate by keeping the infrastructure portable (static site, exportable forum, MIT repos, fiscal host) and by documenting handover procedures in `GOVERNANCE.md` so a new steward pool can pick up cleanly.

---

## Success Signals

Follower counts and traffic are vanity metrics. The things that prove the commons is working:

**Month 3:**
- The Map has 50+ entries, each with a named contributor and a verified date
- At least one RFC has been drafted and merged
- The forum has 5+ substantive threads started by people other than the steward
- One guest post has been published in the archive

**Month 6:**
- External contributors have merged PRs to `ftwr-map` or `ftwr-starters`
- A second steward has been added via RFC
- Forum conversations happen when the steward is offline
- The ledger shows at least one donation cycle and publishes its first quarterly summary
- Archive posts are ranking for sports-analytics search terms and getting cited elsewhere

**Month 12:**
- The steward pool has rotated at least once
- An RFC has been proposed by someone other than the original steward and merged
- The Map is being linked to from outside the FTWR surface (other blogs, forum posts, academic references)
- The project could survive the original steward leaving

The single best signal, at any point: has someone you have never met contributed to the commons? If yes, it is real.

---

## Technical Architecture (Lightweight)

FTWR does not run a data pipeline. It runs a directory, a forum, an archive, and a ledger. The stack is deliberately small.

```
ftwr.app                    -- Landing page (static, Vercel)
blog.ftwr.app               -- Archive (Astro static site, Vercel)
community.ftwr.app          -- Forum (Discourse paid hosting)
github.com/ftwr-dev         -- Commons registry (map, starters, RFCs, site)
opencollective.com/ftwr     -- Ledger (fiscal host)
```

Validation and automation:
- Map entries are JSON/YAML validated against a schema in CI
- Starter repos run their tests on every push
- RFCs lint their frontmatter (status, number, date, authors)
- GitHub webhooks post new issues, PRs, and releases to the forum automatically
- Blog RSS auto-posts to the forum as discussion threads
- Open Collective webhooks post new transactions to the ledger page

---

## Tooling Stack Summary

| Layer | Tool | Cost | Notes |
|---|---|---|---|
| Domain | ftwr.app | ~$15/year | Root domain, all subdomains routed from here |
| Landing | Static on Vercel | Free | `ftwr.app` -- the front door |
| Archive | Astro on Vercel | Free | `blog.ftwr.app` -- static site, markdown in `ftwr-site` |
| Forum | Discourse paid hosting | ~$50/mo | `community.ftwr.app` -- Tier 1, the meeting hall |
| Registry | GitHub org `ftwr-dev` | Free | Map, starters, RFCs, site repos |
| Ledger | Open Collective | Free + % fees | Public accounting, donation processing |
| Broadcast | X (Twitter) | Free | Discovery outpost, institutional voice |
| Discovery | Reddit subreddit | Free | Secondary outpost |

Approximate annual running cost once the forum is on paid hosting: ~$600-800. Donations from a small number of contributors cover this comfortably; if they do not, the project is not yet ready for paid hosting and should stay on the free tier.

---

## Immediate Next Steps

1. Publish `GOVERNANCE.md`, `CURATION.md`, `CONTRIBUTING.md`, and `CODE_OF_CONDUCT.md` at the org level.
2. Spin out `tools.json` into a proper `ftwr-map` repo with a JSON schema, a PR template that requires attribution and a verified date, and CI validation.
3. Create `ftwr-starters` with one reference implementation (Poisson goal model is the natural first) that runs in under a minute on sample data.
4. Draft RFC-0001: the RFC process itself. Merge it as the first piece of self-documenting governance.
5. Move Discourse to `community.ftwr.app` on the paid plan. Apply the category structure above. Write the welcome topic as a description of the commons, not an introduction of a founder.
6. Rewrite the archive's first post (`what-is-ftwr`) to match this framing: no first-person builder voice, institutional tone, reference to the governance docs.
7. Update the landing hero copy to read as a commons, not a project.
8. Register the Open Collective and publish the ledger page.
9. Seed the forum with three to five real questions or observations, not placeholder posts.
10. Only then start posting on X, and only in the institutional voice.

---

*"How deep does the rabbit hole go? Only one way to find out -- together."*
