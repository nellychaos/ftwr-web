# Follow The White Rabbit (FTWR) -- Strategy Plan

## What This Is

FTWR is an online persona and open source developer community built around sports data intelligence, analytics, modelling, and arbitrage. The brand is rooted in the idea of seeing what others miss -- going down the rabbit hole, being early, and looking at the world through a different lens. The public persona shares tips, insights, and trades. The deeper layer is a builder community where people share tools, models, and code in the open.

The brand is sport-agnostic. The edge is in the methods, not the market. The tools and thinking should transfer across football, basketball, tennis, esports, or anything with a data trail and a price.

---

## Brand Identity

### Core Concept

"Follow the white rabbit" is a call to curiosity. It borrows from The Matrix -- the idea that most people see the surface, but there's a deeper reality underneath for those willing to look. In this context, that means: the line is wrong, the model is stale, the market hasn't adjusted, the data tells a different story. FTWR is for the people who want to find out why.

### Brand Pillars

1. **The Hidden Edge** -- Everything we do is about finding signal in noise. Whether that's a mispriced line, an undertrained model, or an overlooked data source, we're always asking "what is the market missing?"

2. **Show Your Work** -- This isn't a tips account. We publish the reasoning, the code, the data, the methodology. If someone follows a trade, they should understand why it exists. If someone uses a model, they should be able to read the source.

3. **Build Together** -- The long-term play is an open source community. Individual edges erode. Collective intelligence and shared tooling compound. The community is the moat.

4. **Sport-Agnostic Methods** -- We care about Poisson distributions, not Premier League fixtures specifically. The methods should work across any sport with quantifiable outcomes and a market to trade against.

### Tone and Voice

- Confident but not arrogant. We share what we see, acknowledge what we don't know.
- Technical but accessible. Code and stats are central, but the writing shouldn't read like an academic paper.
- Contrarian when warranted. Not contrarian for the sake of it -- but willing to publicly disagree with consensus when the data supports it.
- No hype, no "guaranteed winners," no selling dreams. The persona should feel like talking to the smartest person in the room who also happens to bet on sports.
- Slightly mysterious. The rabbit hole metaphor should carry through. Breadcrumbs, not billboards.

### Visual Identity

See FTWR-Brand-Guide.md for the full specification. Summary:

- **Color palette:** Light mode. Warm off-white surfaces (#fcf9f8), near-black text (#1c1b1b), teal (#006875) and magenta (#a900a9) spectral accent palette, cyan (#00daf3) tertiary accent. Spectral gradient (teal to magenta) for hero elements.
- **Typography:** JetBrains Mono for headings, code, data, and labels (uppercase, tracking-widest for labels). Inter for body text.
- **Logo concept:** Minimal rabbit silhouette or abstract rabbit form integrated with a data motif. Must work in single-color (teal on light, near-black on light, white on teal). Recognizable at 32x32.
- **Aesthetic:** Clinical research terminal. Scientific instruments, spectral analysis displays. Precise and intentional. 0px border radius everywhere. Not dark mode, not hacker aesthetic.

---

## Platform Strategy

### Why Not Discord

Discord was considered and rejected. It is where knowledge goes to die. Conversations vanish into infinite scroll, nothing is indexed by search engines, and the entire history of a community becomes unsearchable noise. For a project built on "show your work" and open knowledge development, that is a fundamental mismatch. Forums are slower, but they build a permanent, searchable knowledge base. That compounds over time in a way Discord never can.

### GitHub -- The Center of Gravity

This is where the "open source developer community" claim becomes real. Without active, useful repos, the brand is just another tips account with better aesthetics. GitHub is also where permissionless contribution happens -- anyone can fork, anyone can submit a PR, and quality is enforced through code review. GitHub profiles serve as natural reputation: you can see exactly what someone has shipped.

**Organization:** Create a GitHub org (e.g., `ftwr-dev` or `follow-the-white-rabbit`)

**Initial repositories to seed:**

1. **ftwr-core** -- A Python/TypeScript toolkit for sports data collection, odds comparison, and expected value calculation. This is the anchor repo. It should be genuinely useful on day one, even if small.

2. **ftwr-models** -- A collection of statistical models (Poisson, Elo, Bradley-Terry, etc.) implemented cleanly with documentation explaining the theory behind each one. Sport-agnostic by design.

3. **ftwr-data-streams** -- Tools and examples for connecting to live data feeds, odds APIs, and building real-time pipelines. Kafka, WebSockets, whatever the stack looks like.

4. **ftwr-arbitrage** -- Arbitrage detection tooling. Cross-market scanning, sure-bet identification, value-bet flagging. This will get attention fast because people want it and most implementations are closed-source.

5. **ftwr-blog** -- The source for the blog/website, built in public. Astro, Next.js, or Hugo -- whatever fits. The point is the blog itself is open source.

**Repo standards from day one:**
- Clean READMEs with actual examples, not placeholder text
- MIT or Apache 2.0 license
- Contributing guidelines that make it clear newcomers are welcome
- GitHub Actions CI on every repo
- Issue templates that invite contribution
- A project board visible to the community

**Key principle:** Every repo should solve a real problem. Don't create empty repos as placeholders. Ship small, ship working, iterate in public.

### Discourse Forum -- The Community Home

Discourse is the primary community platform. It is open source, fully indexed by search engines, and has a built-in trust level system that automatically identifies and elevates quality contributors -- exactly what FTWR needs.

**Why Discourse specifically:**
- Every post is indexed by Google. Community knowledge becomes discoverable to the wider internet, which compounds over time and drives organic growth.
- The trust level system (Levels 0-4) automatically promotes members based on reading, posting, and receiving positive engagement. New users start with some restrictions. Sustained quality participation earns expanded privileges. Your best contributors become visible without any manual curation.
- Long-form, structured discussion. Threads stay coherent. People can edit and improve their posts. Topics can be tagged, categorized, and searched.
- Open source software. If you ever want to self-host, you can export everything and run it on your own infrastructure. No vendor lock-in.

**Hosting approach:** Start with Discourse managed hosting (~$25-50/month) to avoid ops overhead. Migrate to self-hosted on a VPS ($15-20/month) once the community is established and the cost/control tradeoff shifts.

**Category structure:**

- **Announcements** -- New releases, blog posts, community updates
- **The Rabbit Hole** -- Deep-dive discussions on specific edges, methodologies, or market anomalies. The signature category.
- **Show Your Work** -- Members post their own analysis, models, or findings for feedback. The most important category for community quality.
- **Models and Methods** -- Statistical modelling discussion, backtesting results, methodology debate
- **Data Sources** -- Shared knowledge about APIs, datasets, scrapers, and feeds
- **Arbitrage** -- Cross-market scanning, sure-bet identification, value-bet discussion
- **Code Help** -- Technical support for people working with FTWR tools or building their own
- **Meta** -- Community governance, feature requests, how FTWR itself operates

**Trust levels and contributor recognition:**
- Level 0 (New): Can post topics and replies in most categories. Some rate limits.
- Level 1 (Basic): Earned by reading and light participation. Full posting access.
- Level 2 (Member): Earned by sustained quality participation over weeks. Can recategorize topics, edit wikis.
- Level 3 (Regular): The quality contributors. Earned automatically through consistent valuable participation. Can edit titles, recategorize, access a private "regulars" lounge for meta-discussion about the community.
- Level 4 (Leader): Manually granted to maintainers. Moderation capabilities.

This maps cleanly to the GitHub contributor model: someone's Discourse trust level and their GitHub commit history together paint a picture of who they are in the community, without needing any manual badging or approval system.

**Integrations to set up:**
- GitHub webhook integration so new PRs, issues, and releases post to the forum automatically
- SSO via GitHub (optional) to link forum identity to code contributions
- RSS feeds from the blog auto-posting new articles as discussion topics

### Blog/Website -- The Knowledge Base

The blog is where the deepest, most polished content lives. Forum posts compound; blog posts compound harder because they rank better in search and represent the curated best of FTWR's thinking.

**Domain:** `blog.ftwr.app`

**Content types:**

- **Technical tutorials** -- "How to build a Poisson model for football from scratch," "Real-time odds streaming with Python and WebSockets," "Detecting arbitrage opportunities programmatically"
- **Case studies** -- Deep retrospectives on specific edges that were found, traded, and resolved. What worked, what didn't, what the market eventually corrected.
- **Model documentation** -- Detailed write-ups of every model in the ftwr-models repo. Theory, implementation, backtesting results, known limitations.
- **Market analysis** -- Longer-form versions of the X threads. Data-heavy breakdowns of specific markets or events.
- **Community spotlights** -- Featuring work from community members. This incentivizes contribution and makes people feel ownership.

**Publishing cadence:** 1-2 posts per week. Consistency matters more than volume. A backlog of 4-6 posts before "launch" would help.

**Technical setup:** Static site generator (Astro or Hugo), deployed on Vercel or Netlify, source code in the ftwr-blog repo. Markdown-based so community members can submit posts via PR.

### X (Twitter) -- The Public Face

X is the broadcast channel. It drives discovery and funnels people toward the forum and GitHub where real participation happens.

**Account purpose:** Build reputation, share insights, attract builders to the community.

**Content types:**

- **Live market reads** -- Short posts calling out mispriced lines, value spots, or model outputs before events. Timestamped and public, which builds credibility over time.
- **Thread breakdowns** -- Deeper analytical threads (5-15 posts) walking through a methodology, a model's output, or a case study of where the market got it wrong.
- **Code snippets** -- Screenshots or short code blocks showing how to pull data, run a model, or calculate expected value. Always with a "full code on GitHub" link.
- **Data visualizations** -- Charts, heatmaps, probability distributions. Visual content that stops the scroll.
- **Community highlights** -- Reposting and crediting work from community members.
- **"Down the rabbit hole" series** -- Recurring posts that start with a simple observation and unravel into something deeper. The signature content format.

**Posting cadence (initial):** 1-2 substantive posts per day, with engagement/replies throughout. Quality over volume. No filler.

**Growth mechanics:**
- Quote-tweet popular sports/betting accounts with a data-driven counter-take
- Engage genuinely with other analytics accounts -- don't just broadcast
- Pin a thread that explains what FTWR is and links to GitHub/forum/blog
- Use the "rabbit hole" format as a recognizable signature that people associate with the brand

### Reddit -- Discovery Outpost (Optional)

A subreddit (r/followthewhiterabbit or r/ftwr) is worth creating early as a low-cost discovery channel. Sports analytics people already hang out on Reddit. But it is an outpost, not the home.

**How to use it:**
- Cross-post interesting forum threads and blog posts for reach
- Link back to the Discourse forum for deeper discussion
- Use it as a place to share FTWR tooling in relevant subreddits (r/sportsbook, r/sportsbetting, r/datascience, r/machinelearning) when genuinely relevant -- not spam
- Let Reddit's upvote/downvote system do its own quality sorting

**What to avoid:**
- Do not try to build the community on Reddit. You do not own the platform, Reddit's API and moderation decisions are unpredictable, and the audience skews more casual than builder-oriented.
- Do not duplicate the forum on Reddit. The subreddit is a pointer, not a destination.

---

## Content Strategy -- The First 90 Days

### Weeks 1-2: Foundation

- Register handles across all platforms (X, GitHub, Reddit)
- Secure domain (ftwr.dev or similar)
- Set up the GitHub org with at least `ftwr-core` containing real, working code
- Set up Discourse forum with category structure and trust levels configured
- Design and deploy a minimal blog/landing page
- Write 3-4 blog posts as a backlog (don't publish yet)
- Create the subreddit and write the sidebar/rules
- Design profile images, banners, and visual assets

### Weeks 3-4: Soft Launch on X

- Start posting daily. Lead with data and analysis, not "hey I'm new follow me"
- Publish the first 2 blog posts and link from X
- Push initial code to GitHub repos with clean READMEs
- Post the first few discussion topics on the Discourse forum yourself to seed it with real content (not placeholder threads -- actual analysis or questions)
- Don't actively promote the forum yet -- let X build some gravity first

### Weeks 5-8: Build Momentum

- Increase X engagement -- reply to other accounts, share contrarian takes backed by data
- Publish 1-2 blog posts per week
- Add forum link to X bio and blog, start inviting engaged followers to participate in discussions
- Ship meaningful updates to GitHub repos -- each update is content (tweet the changelog)
- Start the "Down the rabbit hole" recurring series on X
- Cross-post interesting content to relevant subreddits for discovery
- Engage with any early forum members personally. First 20-30 members set the culture.
- Set up GitHub webhook integration so repo activity flows into the forum automatically

### Weeks 9-12: Community Activation

- Tag "good first issue" on GitHub repos to invite contributions
- Run a community challenge (e.g., "build a model for X sport using ftwr-core, share your results on the forum")
- Feature community work on the blog and X
- Assess what content formats are getting traction and double down
- Review Discourse trust level promotions -- are quality contributors being recognized automatically?
- Begin tracking growth metrics: GitHub contributors, forum active users, blog search traffic

---

## Technical Architecture (High Level)

This is the stack that both powers the content and becomes the open source offering:

```
Data Layer
  - Sports data APIs (odds providers, stats providers, live feeds)
  - Web scrapers for data not available via API
  - PostgreSQL or TimescaleDB for historical storage
  - Redis for real-time caching

Processing Layer
  - Python for modelling and analysis (pandas, scipy, scikit-learn)
  - TypeScript/Node for real-time streaming and tooling
  - Apache Kafka or Redis Streams for event processing
  - Scheduled jobs for model runs and data collection

Model Layer
  - Statistical models (Poisson, Elo, Bradley-Terry, Dixon-Coles)
  - Machine learning models where appropriate (but stats-first philosophy)
  - Backtesting framework for validating model performance
  - Expected value and Kelly criterion calculators

Output Layer
  - Landing page at ftwr.app (static, minimal)
  - Blog at blog.ftwr.app (static site, markdown-based)
  - Forum at ftwr.discourse.group (Discourse, free plan)
  - X posts (manual initially, potential for automation later)
  - Dashboard (optional, later -- a web app showing live model outputs)
```

---

## Why This Will Never Be Monetized

This is worth stating plainly: FTWR will not be monetized. No paid tiers, no premium channels, no courses, no affiliate links, no sponsored content, no consulting funnel. The entire point is to build something genuinely useful with people who care about the same problems.

The sports analytics space is flooded with people selling picks, selling courses on how to sell picks, and selling "VIP" access to information that should be free. FTWR exists as the opposite of that. The moment money enters the equation, incentives shift. You start optimizing for subscriber retention instead of honest analysis. You start gatekeeping code that should be open. You start attracting people who want to be sold to instead of people who want to build.

The value of FTWR is the community itself -- the shared tooling, the collective knowledge, the conversations between people who think carefully about these problems. That value compounds when it's open and free. It dies the moment you put a price on it.

If the project needs infrastructure funding down the line (server costs, API subscriptions for shared data), that's a community conversation, not a business model. GitHub Sponsors or Open Collective could cover operational costs transparently. But the work itself -- the code, the content, the community -- stays free and open. Full stop.

---

## Key Risks and How to Manage Them

1. **"Just another tips account" perception** -- Mitigated by always showing the work. Code, data, methodology. The GitHub repos are the differentiator. If someone looks at FTWR and sees tips without substance, the brand has failed.

2. **Open sourcing edges destroys them** -- Partially true. Individual edges do erode when shared. But the FTWR thesis is that the ability to find edges is more valuable than any single edge. The community compounds the rate of edge discovery. Also, most "edges" in retail sports betting are execution advantages (speed, access, bankroll management) not just information advantages.

3. **Community stays small** -- This is fine for a long time. 50 active builders who ship code and share analysis is worth more than 10,000 passive followers. Optimize for quality of community members, not quantity.

4. **Burnout from content treadmill** -- The slow burn approach helps. The open source model helps too -- as the community grows, content generation becomes distributed. Community members write blog posts, ship code, and share analysis. The persona curates and amplifies rather than producing everything solo.

5. **Legal/regulatory risk** -- Sports betting legality varies by jurisdiction. The persona should focus on analysis and methodology, not "place this bet." The code is educational/analytical tooling. This isn't legal advice, but the framing matters.

---

## Success Metrics (6-Month Checkpoints)

Follower counts are vanity metrics. The things that actually matter are whether people are building, whether conversations are happening without you driving them, and whether the tooling is being used in the real world.

**Month 3:**
- GitHub: 3+ repos with real, working code that someone outside the project has actually used
- Forum: A core group (even if it's 10 people) having substantive technical conversations on Discourse
- Blog: 8+ published posts with at least some organic search traffic arriving
- X: Genuine engagement on posts -- replies and quote tweets from people in the space, not just likes

**Month 6:**
- GitHub: External contributors have submitted and merged PRs. Someone has built something with FTWR tooling that you didn't anticipate.
- Forum: Conversations happen when you're not online. People are answering each other's questions. Trust levels are promoting the right people.
- Blog: Posts are ranking for sports analytics search terms. People are referencing FTWR content in their own work.
- X: Recognized enough in the niche that other analytics accounts engage naturally

The single best signal at month 6: has anyone you've never met shipped code to a FTWR repo or shared original analysis on the forum? If yes, the community is real. If no, it's still just a personal project with an audience.

---

## Domain Architecture

```
ftwr.app                    -- Landing page (static, Vercel/Netlify)
blog.ftwr.app               -- Blog (Astro/Hugo, Vercel/Netlify)
ftwr.discourse.group         -- Community forum (Discourse free plan)
github.com/ftwr-dev          -- Code (GitHub org)
```

The root domain is a thin landing page that explains what FTWR is and routes people to the right place. It is the front door -- minimal, on-brand, fast. The blog gets its own subdomain so it can grow independently and rank in search. The forum stays at the Discourse-provided URL on the free plan; if the project moves to paid Discourse hosting later, `community.ftwr.app` can point to it. GitHub is GitHub.

## Tooling Stack Summary

| Layer | Tool | Cost | Notes |
|---|---|---|---|
| Domain | ftwr.app | ~$15/year | Root domain, subdomains for blog |
| Landing | Static page on Vercel/Netlify | Free | Thin intro page at ftwr.app |
| Code | GitHub (org: ftwr-dev) | Free | Center of gravity for all code, PRs, issues |
| Community | Discourse (free plan) | Free | Forum at ftwr.discourse.group, trust levels, searchable |
| Blog | Astro or Hugo on Vercel/Netlify | Free | Static site at blog.ftwr.app, markdown-based, source in GitHub |
| Broadcast | X (Twitter) | Free | Public face, discovery, short-form content |
| Discovery | Reddit (subreddit) | Free | Outpost for reach, not the home |

Total day-one cost: a domain registration. Everything else is free. No vendor lock-in on any critical piece. Discourse data is exportable. Blog is static files in a git repo. Code is on GitHub. If any platform dies or changes terms, you can move.

---

## Immediate Next Steps

1. Register `ftwr.app` domain.
2. Register handles: @ftwr or @ftwr_ across X, GitHub (org: ftwr-dev), Reddit (r/ftwr or r/followthewhiterabbit).
3. Configure the Discourse forum at `ftwr.discourse.group`: categories, color palette, branding, community guidelines, welcome topic.
4. Design the visual identity (logo, color scheme, profile/banner images).
5. Build and deploy the landing page at `ftwr.app`.
6. Set up the GitHub org and seed the first repo with real, working code.
7. Set up the blog infrastructure at `blog.ftwr.app` (repo, Astro/Hugo, deployment).
8. Write the first 3 blog posts as backlog content.
9. Create the X account and start posting.
10. Create the subreddit with sidebar, rules, and initial posts.

---

*"How deep does the rabbit hole go? Only one way to find out."*
