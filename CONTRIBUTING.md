# Contributing to FTWR

FTWR is an open source community project. The most direct way to contribute is by suggesting a tool for The Map, writing a blog post, or opening a pull request on one of the community repositories.

## Suggesting a tool for The Map

The Map is a curated directory, not a comprehensive index. Every entry is there because it provides a genuine, specific utility for sports analytics work -- data acquisition, modelling, edge measurement, or execution. The bar for inclusion is: would a practitioner reach for this?

### Open an issue

Use the [Tool Suggestion](https://github.com/nellychaos/ftwr-web/issues/new?template=tool-suggestion.yml) issue template. Fill in every field. Incomplete submissions will be closed without review.

### Inclusion criteria

A tool is considered if it meets all of the following:

**1. Genuine utility**
The tool solves a real, specific problem in sports analytics, modelling, or prediction market research. "Utility" means a practitioner would use it in actual work, not just in theory.

**2. Verifiable**
The tool exists, is publicly accessible, and functions as described. For open source projects, the repository must be real and contain substantive code. For commercial products, a working URL and clear description of what the product does is required.

**3. Honest description**
The description submitted must be factual and neutral. Marketing language ("the best", "industry-leading", "most powerful") is grounds for rejection. The description should answer: what does it do, and what are its constraints?

**4. Not redundant**
If a substantially equivalent tool is already listed, the new entry needs a clear functional difference -- not just a different brand or interface.

**5. Appropriate category**
The tool fits into one of the existing categories. Suggest the most appropriate one; the maintainer may reassign it.

### What is not listed

- Tools with no demonstrated use case in sports analytics
- Affiliate link destinations or referral schemes submitted purely for traffic
- SaaS products with no meaningful free tier and no publicly documented API (pure sales-funnel landing pages)
- Personal portfolio projects with no external users or evidence of use
- Anything requiring the user to submit personal data before seeing what the product does
- Duplicate submissions of tools already listed under a different name

### Commercial tools

Commercial tools are listed if they provide a function that has no adequate open source equivalent and they are genuinely used by practitioners. Being commercial is not a disqualifier. Submitting a commercial tool you have a financial interest in without disclosing that relationship is grounds for permanent rejection of future submissions.

### Review process

Submissions are reviewed by the maintainer. There is no automated approval. Expect a response within a few days. The maintainer may ask clarifying questions, request a revised description, or decline without detailed explanation if the tool does not meet the criteria above.

If a submission is declined, you are welcome to revise and resubmit once if you believe the criteria are met and can demonstrate it.

---

## Writing for the blog

Blog posts live in `blog/src/content/blog/`. Each post is an MDX file with the following frontmatter:

```yaml
---
title: 'Post title here'
description: 'One sentence description for the index and SEO'
publishedDate: 2026-04-20
author: 'Your name or handle'
tags: [tag-one, tag-two]
category: technical-tutorial
draft: false
---
```

Valid categories: `technical-tutorial`, `case-study`, `model-documentation`, `market-analysis`, `community-spotlight`, `meta`.

Write the post in MDX below the frontmatter. Open a pull request against `main`. Posts go through the same editorial standard as tool descriptions: factual, no hype, grounded in actual work.

---

## Pull requests on community repositories

The FTWR community repositories (`ftwr-core`, `ftwr-models`, `ftwr-data-streams`, `ftwr-arbitrage`) each have their own contributing guidelines. Check the `CONTRIBUTING.md` in each repository before opening a PR.

General standards that apply across all repositories:

- No dependencies added without discussion in an issue first
- Functions and modules should have docstrings
- New functionality requires at least one test
- Code should run without error on Python 3.10+
- No placeholder implementations -- if a function is not ready, mark it clearly as `NotImplemented` and explain why in the PR

---

## Code of conduct

This is a technical community. Contributions are evaluated on their technical merit. Personal attacks, harassment, and bad-faith submissions are grounds for being blocked from the project.
