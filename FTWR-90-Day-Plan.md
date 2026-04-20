# FTWR -- 90-Day Marketing, Platform, and Content Plan

This is the week-by-week execution plan for launching FTWR from nothing. It assumes one person doing everything, so the pacing is deliberately conservative. Better to ship consistently at a sustainable pace than to burn out by week 6 and go silent.

The strategy plan covers the "what and why." This document covers the "when and how."

---

## Current State

Nothing is live. No accounts, no content, no repos. The domain ftwr.app is registered (or will be). The Discourse forum at ftwr.discourse.group exists but is unconfigured. Everything else starts from scratch.

---

## Phase 1: Foundation (Weeks 1-3)

The goal of Phase 1 is to build the infrastructure and stockpile enough content that when you go public, there's something real to find. Nobody should land on an empty GitHub org, an empty forum, or a blog with one post. The first impression needs to communicate that this is serious and already in motion.

### Week 1: Accounts and Infrastructure

**Platform setup (do all of this before posting anything publicly):**

- Register the GitHub org (ftwr-dev). Set the org bio, avatar, and a one-line description. Do not create repos yet.
- Register the X account. Set profile picture, banner, bio, and pinned tweet placeholder (don't start posting yet). Bio should read something like: "Sports data intelligence. Open source tooling. Going down the rabbit hole." Link to ftwr.app.
- Create the subreddit (r/ftwr or r/followthewhiterabbit). Write the sidebar description, set rules mirroring the community principles from the brand guide, add relevant flair categories (Analysis, Tool, Discussion, Down the Rabbit Hole). Don't promote it yet.
- Configure the Discourse forum: apply FTWR branding (light surface bg, teal accents per the brand guide), create the category structure (Announcements, The Rabbit Hole, Show Your Work, Models and Methods, Data Sources, Arbitrage, Code Help, Meta), write the welcome topic and community guidelines.

**Content production (not published yet, just stockpiled):**

- Write Blog Post 1: "What is FTWR?" -- a manifesto-style post explaining the project, the no-monetization stance, and what you're building. This becomes the canonical reference when people ask "what is this?"
- Begin drafting Blog Post 2: a technical tutorial. Pick whichever is closest to ready in your head -- Poisson modelling, EV calculation, odds API integration, whatever. It needs to include working code.

**Estimated time: 10-12 hours across the week.**

### Week 2: Code and Content Stockpile

**GitHub:**

- Create and push `ftwr-core` with real, working code. Even if it's small -- a clean Python package that pulls odds from a public API, calculates expected value, and runs a basic Poisson model. It has to actually work. Clean README with install instructions, a quickstart example, and a "contributing" section. MIT license. GitHub Actions CI running tests on push.
- Create `ftwr-models` with at least one fully documented model implementation (Poisson is the natural starting point). Theory explanation in the README, code that runs, example output.

**Content production:**

- Finish Blog Post 2 (technical tutorial).
- Write Blog Post 3: a case study or market analysis. Take a real upcoming fixture or event, run your model on it, show the output, explain where the model disagrees with the market and why. This is the "show your work" format that defines the brand.
- Draft 5-7 X posts/threads you can schedule for the first week of posting. Mix of: one analytical thread (5-10 posts walking through a model output), a few standalone data viz posts, a code snippet post linking to GitHub.

**Estimated time: 12-15 hours across the week.**

### Week 3: Blog Deploy and Content Buffer

**Blog:**

- Deploy the blog at blog.ftwr.app. Static site (Astro or Hugo), source in the ftwr-blog repo, deployed on Vercel or Netlify. The blog design must match the brand guide: light surface background, JetBrains Mono for code and headings, Inter for body, teal/magenta accents, 0px border radius on everything.
- Publish Blog Posts 1, 2, and 3. Having three posts live on day one means the blog looks established, not abandoned.
- Set up RSS feed so new blog posts can auto-post to the Discourse forum.

**Landing page:**

- Deploy the landing page at ftwr.app. (You mentioned handling website development separately, so this may happen on a different timeline. If the landing page isn't ready, a simple redirect to the blog is fine as a temporary measure.)

**Forum seeding:**

- Post 3-5 real discussion topics on the Discourse forum yourself. These should be genuine analysis, questions, or discussion starters -- not "welcome to the forum!" filler. Examples: a thread analyzing a specific market inefficiency, a question about model selection for a particular sport, a thread sharing a data source you've found useful. The forum should look like a place where real conversation already happens.

**Content buffer:**

- Write Blog Post 4 (publish next week).
- Draft another 5-7 X posts/threads for the following week.

**Estimated time: 10-12 hours across the week.**

---

## Phase 2: Soft Launch (Weeks 4-6)

Phase 2 is when you start posting publicly on X. The goal is to build a small audience of the right people -- analytics-minded, builder-oriented -- and start routing them toward the blog, GitHub, and eventually the forum.

### Week 4: Go Live on X

**X posting begins:**

- Start posting. Aim for one substantive post per day. "Substantive" means it contains data, code, analysis, or a genuine insight. Not "good morning sports twitter" filler.
- Publish your first analytical thread (the 5-10 post format walking through a model or market read). These threads are the highest-leverage content on X because they get shared and bookmarked.
- Pin a thread to your profile that explains what FTWR is, with links to the blog, GitHub, and forum.

**Content cadence from this point forward:**

- X: 1 substantive post per day, 5-7 days a week. Mix of standalone posts, threads, code snippets, and data viz. Engage in replies with other accounts in the sports analytics space.
- Blog: 1 post per week (published on a consistent day -- Tuesday or Wednesday tend to perform well for technical content).
- GitHub: at least one meaningful commit per week. Ship small, ship working. Each code update is also content (tweet it).
- Forum: 1-2 new topics or replies per week to keep it active while the audience is still small.

**Engagement strategy:**

- Find 15-20 accounts in the sports analytics, quant betting, and data science spaces. Follow them, engage with their posts with substantive replies (not "great thread!"), quote-tweet with data-driven counter-takes when you have something real to add.
- Do not @ people asking them to check out your project. Let the work speak. If your threads are good, the right people will find them.

**Publish Blog Post 4.**

**Estimated time: 8-10 hours per week from here on out (the ongoing baseline).**

### Week 5: Build Rhythm

**X:**

- Continue daily posting. By now you should have a feel for what gets engagement and what doesn't. Double down on whatever resonates.
- Post the first "Down the Rabbit Hole" thread -- the signature format from the brand guide. Start with a simple observation, pull on the thread, and end somewhere surprising. Tag it with a consistent identifier so people recognize the series.
- Share a code snippet from ftwr-core or ftwr-models with a "full code on GitHub" link. This is how you convert X followers into GitHub visitors.

**Blog:**

- Publish Blog Post 5. Ideally this is the strongest piece you've written -- something genuinely useful that could rank in search for a relevant query (e.g., "Poisson distribution football model Python," "expected value sports betting calculation," "odds API comparison").
- Check that blog posts are being picked up by Google. Submit the sitemap to Google Search Console if you haven't already.

**GitHub:**

- Ship an update to ftwr-core or ftwr-models. Tweet the changelog.
- Review any issues or stars. If someone has engaged with the repos, respond promptly. Early adopters remember how they were treated.

**Forum:**

- Add the forum link to your X bio (alongside the blog link).
- If any X followers have shown genuine interest (not just likes, but replies and questions), DM them an invitation to the forum. Personal invitations from the founder carry weight.

### Week 6: First Content Milestone

**Content checkpoint:**

By the end of week 6, you should have:

- 6+ blog posts published
- 30+ substantive X posts
- 2+ GitHub repos with real code and clean documentation
- 8-10 forum topics with genuine content
- At least 2 "Down the Rabbit Hole" threads on X

**If you're behind on any of these, this is the week to catch up before Phase 3.**

**Reddit:**

- Cross-post your best blog post to a relevant subreddit (r/sportsbook, r/datascience, or r/sportsbetting -- wherever the content fits most naturally). Do this once, see how it performs. If it gets traction, you can make this a regular thing. If it doesn't, don't force it.
- Post it to r/ftwr as well to start giving the subreddit some life.

---

## Phase 3: Community Activation (Weeks 7-12)

Phase 3 is where the project either becomes a real community or stays a personal blog with some GitHub repos. The goal is to get other people contributing -- posting on the forum, opening issues on GitHub, sharing their own work.

### Week 7-8: Invite Contribution

**GitHub:**

- Audit your repos and tag 3-5 issues as "good first issue." These should be genuinely approachable: documentation improvements, adding a new sport to an existing model, writing a test, fixing a clearly scoped bug. Not vague "build the whole feature" issues.
- Write a CONTRIBUTING.md if you haven't already. Make it clear how someone goes from "interested" to "first PR merged."
- Tweet about the good first issues. Frame it as an invitation: "If you've been curious about sports modelling, here are some ways to get your hands dirty."

**Forum:**

- Start a "Show Your Work" thread inviting people to share whatever they've been working on -- even if it's rough, even if it's just an idea. Lower the barrier. The first few people who post will set the tone.
- Respond to every forum post. At this stage, the community is small enough that personal engagement matters enormously. If someone posts analysis, give real feedback. If someone asks a question, answer it thoroughly.

**X:**

- Continue the daily cadence. Start weaving in community references: "someone on the forum pointed out..." or "a contributor just shipped this to ftwr-core..." -- even if the community is tiny, narrating its activity makes it feel alive from the outside.

**Blog:**

- Publish Blog Posts 7 and 8. One of these should be a piece that directly invites participation: "5 open problems in sports modelling" or "things I wish existed in the FTWR toolkit." Frame unsolved problems as opportunities, not complaints.

### Week 9-10: Run a Community Challenge

**The challenge:**

Run a simple, time-boxed challenge. Something like: "Build a model for [specific sport or league] using ftwr-core. Post your approach and results on the forum. Best write-up gets featured on the blog and X."

**Why this works:**

- It gives people a concrete reason to try the tooling.
- It generates forum content.
- It surfaces people who are genuinely interested in building, not just lurking.
- The "featured on the blog" reward costs you nothing but creates real incentive.

**How to run it:**

- Announce on X with a thread explaining the challenge, linking to the forum topic.
- Create a dedicated forum topic for challenge submissions.
- Cross-post to the subreddit.
- Run it for 2 weeks. At the end, write a blog post featuring the best submissions and what you learned from them.
- Be generous with credit. Name people, link to their work, highlight what was clever or novel about their approach.

**Blog:**

- Publish Blog Post 9 (could be the challenge announcement post itself).

### Week 11-12: Assess and Adjust

**Metrics review (be honest with yourself):**

GitHub:
- How many stars across repos? (Vanity, but directionally useful.)
- Has anyone outside the project opened an issue or submitted a PR? This is the signal that matters.
- Are the repos being cloned/forked? Check GitHub traffic analytics.

Forum:
- How many registered members? How many have posted?
- Are conversations happening that you didn't start? This is the critical milestone.
- Are the trust levels promoting anyone? If nobody has reached Level 2, the community isn't active enough yet.

Blog:
- What's the total traffic? What's organic search traffic specifically?
- Which posts get the most views? Which get the most time-on-page?
- Is anything ranking in search yet?

X:
- Follower count is a secondary metric. Primary: are people in the sports analytics niche engaging? Are you getting replies and quote tweets from accounts that matter?
- Are X posts driving traffic to the blog and GitHub? (Check referrer data.)

**Adjust based on what you find:**

- If X is working but the forum is dead: keep investing in X, reduce forum posting cadence, focus on converting X engagement into GitHub contributions instead.
- If blog posts are getting search traffic: double down on SEO-friendly technical tutorials. This is your long-term compounding asset.
- If GitHub is getting engagement but the blog isn't: your audience might be more developer than analyst. Lean into code-heavy content.
- If nothing is working: be honest about whether the content quality is high enough. Read your own posts from a stranger's perspective. Is the analysis original? Is the code useful? Would you follow this account if you didn't run it?

**Content:**

- Publish Blog Posts 10, 11 (and 12 if the challenge write-up is ready).
- Write a "State of FTWR" post for the blog and forum. Be transparent about where things stand, what's working, what isn't, what's next. This kind of honesty builds trust and invites people to shape the direction.

---

## Weekly Time Budget (Ongoing from Week 4)

This is what a sustainable solo week looks like. If it regularly takes more than 10 hours, something needs to be cut or simplified.

| Activity | Hours/Week | Notes |
|---|---|---|
| X posting and engagement | 3-4 | 1 post/day + replies. Batch-write posts on one day if possible. |
| Blog writing | 3-4 | 1 post/week. Write in 2 sessions: draft then edit. |
| GitHub (code + maintenance) | 2-3 | 1 meaningful commit/week. Review any issues/PRs. |
| Forum | 1 | Post 1-2 topics/replies. Respond to any activity. |
| Reddit | 0.5 | Cross-post the week's best content if relevant. |
| Total | ~10 | |

If you're spending more than 4 hours on X, you're over-investing in the broadcast channel relative to the assets that compound (blog, code). If you're spending less than 3 hours on the blog, the content engine will stall.

---

## Content Pipeline

### Blog Post Backlog (Suggested Topics for the First 12 Weeks)

These are suggestions, not assignments. Write whatever you're most interested in or whatever is closest to ready. The only rule is that every post should contain either working code, real data analysis, or both.

1. "What is FTWR?" -- manifesto, mission, why this exists
2. "Building a Poisson Model from Scratch" -- the canonical technical tutorial
3. Market analysis / case study -- pick a real event, run the model, show the output
4. "Expected Value Explained for Sports Bettors Who Can Code" -- foundational concept piece
5. "Comparing Odds APIs" -- practical guide to data sources, what's free, what's paid, how to pull data
6. "Introduction to Kelly Criterion" -- theory + code implementation
7. "5 Open Problems in Sports Modelling" -- invites participation
8. Data visualization walkthrough -- how to build the kind of charts FTWR uses, with code
9. Community challenge announcement (or challenge results write-up)
10. "Dixon-Coles: A Better Football Model" -- leveling up from basic Poisson
11. Case study: "Where the Market Got It Wrong" -- retrospective on a real misprint
12. "State of FTWR" -- transparency post on the first 90 days

### X Content Formats (Rotation)

Rotate through these formats to keep the feed varied. You don't need to plan every post in advance, but knowing the formats helps when you sit down to batch-write.

- **Analytical thread** (5-10 posts): walk through a model output, a market read, or a case study. Include charts/viz. 1-2 per week.
- **Code snippet**: screenshot or inline code showing a useful function, with "full code on GitHub" link. 1-2 per week.
- **Data visualization**: a chart, heatmap, or distribution that tells a story. Let the image do the work, keep the caption short. 1-2 per week.
- **Down the Rabbit Hole**: the signature long-form thread. Start simple, go deep. 1 per week or every other week.
- **Community highlight**: reshare something from the forum or a GitHub contribution. As needed once community activity starts.
- **Contrarian take**: where the model disagrees with the market or consensus. Short, specific, backed by data. As the opportunity arises.

### Forum Seeding Topics (First 3 Weeks, Before Community Arrives)

You need to seed the forum with real content so it doesn't look empty when people first visit. These should be actual discussion starters, not placeholder text.

- "Introducing FTWR -- what we're building and why" (pinned in Announcements)
- "Which odds APIs are you using? Pros, cons, and gotchas" (Data Sources)
- "Poisson vs Dixon-Coles for football: when does the complexity pay off?" (Models and Methods)
- "How do you handle model calibration over time?" (Models and Methods)
- "What's the most interesting arbitrage opportunity you've found recently?" (Arbitrage)
- "Share your setup: languages, tools, data sources, and workflow" (Show Your Work)

---

## Platform-Specific Launch Checklist

### X

- [ ] Account created
- [ ] Profile picture set (matches brand guide)
- [ ] Banner set (light, minimal, spectral gradient or data viz)
- [ ] Bio written (under 160 chars, includes ftwr.app link)
- [ ] Pinned thread written and posted (what is FTWR, links to blog/GitHub/forum)
- [ ] First 2 weeks of posts drafted or outlined

### GitHub

- [ ] Org created (ftwr-dev)
- [ ] Org avatar and description set
- [ ] ftwr-core repo created with working code, README, CI, license
- [ ] ftwr-models repo created with at least one documented model
- [ ] CONTRIBUTING.md in place
- [ ] Issue templates created

### Discourse Forum

- [ ] Branding applied (light mode, teal accents, FTWR wordmark)
- [ ] Categories created (all 8 from the category structure)
- [ ] Welcome topic written and pinned
- [ ] Community guidelines written and pinned
- [ ] 5+ real discussion topics posted
- [ ] GitHub webhook integration configured (optional, can be added later)
- [ ] RSS feed from blog configured to auto-post new articles

### Blog

- [ ] Site deployed at blog.ftwr.app
- [ ] Design matches brand guide (light mode, spectral palette, JetBrains Mono + Inter, 0px radius)
- [ ] 3+ posts published before going public
- [ ] RSS feed working
- [ ] Sitemap submitted to Google Search Console
- [ ] Analytics installed (Plausible or Umami -- privacy-respecting, no cookie banners needed)

### Reddit

- [ ] Subreddit created
- [ ] Sidebar written with description and links
- [ ] Rules set (mirrors community principles)
- [ ] Post flair created (Analysis, Tool, Discussion, Down the Rabbit Hole)
- [ ] 1-2 initial posts made

### Landing Page (ftwr.app)

- [ ] Deployed (or temporary redirect to blog in place)
- [ ] Links to blog, forum, GitHub all working
- [ ] Loads fast, matches brand guide

---

## What Success Looks Like at Day 90

Be realistic. At 90 days with one person, you're not going to have thousands of followers or a thriving community. Here's what you should actually aim for:

**Minimum viable success (the project is working):**
- 8-12 blog posts published, at least some getting organic search traffic
- 2-3 GitHub repos with real code that someone outside the project has cloned or starred
- A forum with 10-30 registered members and at least a few threads you didn't start
- An X account with a small but engaged following in the sports analytics niche (100-500 followers who actually interact)
- A consistent publishing rhythm that feels sustainable

**Strong success (ahead of pace):**
- Someone you've never met has submitted a PR to a FTWR repo
- Forum conversations are happening without you driving them
- A blog post is ranking on the first page of Google for a relevant search term
- Another account in the space has shared or referenced FTWR content unprompted
- You've run the community challenge and gotten at least 3-5 submissions

**The one metric that matters most:** is anyone building with this? If someone outside your immediate circle has used ftwr-core to do their own analysis, or posted their own model on the forum, or contributed code -- the project is real. Everything else is leading indicators.

---

*The rabbit hole doesn't build itself. But it only needs to go deep enough for the curious to follow.*
