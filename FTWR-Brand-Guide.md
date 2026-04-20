# FTWR Brand Guide

**Follow the White Rabbit**
Version 1.0 // April 2026

---

## 1. Brand Overview

### What FTWR Is

FTWR (Follow the White Rabbit) is an open source developer community and online persona built around sports data intelligence, analytics, modelling, and arbitrage. The brand exists to attract curious, technically-minded people who want to find edges that others miss, and to give them the tools, methods, and community to do it together.

The name references going down the rabbit hole. Seeing the world differently. Being early. Questioning the consensus. It is a call to curiosity aimed at builders, analysts, and anyone who believes the interesting answers are found by looking deeper than the surface.

### What FTWR Is Not

FTWR is not a tips service. It is not a paid community, a course, a premium Discord, or a monetization vehicle of any kind. There is no financial incentive behind this project. The only thing being optimized for is the quality of the community and the usefulness of the work.

The moment money enters the picture, incentives shift. FTWR stays free, open, and community-owned. If infrastructure costs arise, they are covered transparently through community mechanisms like GitHub Sponsors or Open Collective, never through gated content or premium tiers.

### Brand Pillars

**The Hidden Edge** -- Everything we do is about finding signal in noise. A mispriced line, an undertrained model, an overlooked data source. We are always asking: what is the market missing?

**Show Your Work** -- Code, data, methodology. If someone follows a trade, they understand why it exists. If someone uses a model, they can read the source. Transparency is not optional.

**Build Together** -- Individual edges erode. Collective intelligence and shared tooling compound. The community is the product. Everything we build is open source, and contributions from anyone are welcome.

**Sport-Agnostic Methods** -- We care about Poisson distributions, not Premier League fixtures. The methods should transfer across any sport with quantifiable outcomes and a market to trade against.

---

## 2. Voice and Tone

The FTWR voice should feel like talking to the sharpest person in the room who happens to bet on sports and write code. It is direct, technically grounded, and never condescending. The tone shifts slightly depending on context, but these principles hold everywhere.

### Core Voice Attributes

**Confident, Not Arrogant** -- State what the data shows. Acknowledge what you do not know. Never oversell a finding or claim certainty where there is none. The strength is in the analysis, not in the bravado.

**Technical, But Accessible** -- Code and statistics are central to everything FTWR produces. But the writing should not read like an academic paper. Explain the reasoning. Use plain language when it works. Save the jargon for when precision requires it.

**Contrarian When Warranted** -- If the data disagrees with the consensus, say so. But never be contrarian for its own sake. Every counter-take must be backed by evidence. The goal is accuracy, not attention.

**No Hype** -- No "guaranteed winners." No "lock of the day." No selling dreams. If a model output looks promising, present it with the confidence interval and the caveats, not with fireworks.

**Slightly Mysterious** -- The rabbit hole metaphor carries through. Breadcrumbs, not billboards. Tease the depth. Let people discover the layers. The best content makes the reader feel like they found something, not like it was pushed on them.

### Do and Do Not

| DO | DO NOT |
|---|---|
| "Model gives 62% probability on the over. Market has it at 55%. That is a +EV spot." | "LOCK OF THE DAY. Smash the over." |
| "The data suggests X, though sample size is limited. Worth monitoring." | "Trust me, this is going to hit." |
| "Here is the code. Run it yourself. Tell me if you see something I missed." | "I have a system. You would not understand it." |
| "Interesting edge in the Croatian second division. Thread below." | "Only real ones know about this play." |
| "We were wrong about X. Here is what the model missed and what we changed." | "Market got lucky. Model was right, variance just went against us." |

---

## 3. Visual Identity

### Color Palette

The FTWR palette is light mode, clinical, and research-terminal in feel. The aesthetic draws from scientific instruments, spectral analysis displays, and medical imaging interfaces. Everything should feel precise and intentional -- a research lab, not a hacker's basement. The color system is built around a spectral gradient running from teal to magenta, used sparingly as an accent against warm neutral surfaces.

#### Surface Colors

| Color | Hex | Usage |
|---|---|---|
| Surface | `#fcf9f8` | Primary background for all digital surfaces |
| On Surface | `#1c1b1b` | Primary text, headings, body copy |
| Surface Container | `#f3f0ef` | Cards, panels, elevated containers |
| Surface Container High | `#ede9e8` | Active states, selected items, prominent cards |

#### Accent Colors (Spectral Palette)

| Color | Hex | Usage |
|---|---|---|
| Teal | `#006875` | Primary accent. Links, interactive elements, key data series |
| Magenta | `#a900a9` | Secondary accent. Highlights, secondary data series, emphasis |
| Cyan | `#00daf3` | Tertiary accent. Sparklines, supporting visualizations, hover states |
| Spectral Gradient | `#006875 to #a900a9` | Hero elements, progress bars, decorative accents. Applied as `linear-gradient(90deg, #006875 0%, #a900a9 100%)` |

#### Signal Colors

| Color | Hex | Usage |
|---|---|---|
| Positive | `#006875` | Positive signals, gains, edges (uses teal) |
| Negative | `#ba1a1a` | Negative signals, errors, loss indicators |
| Warning | `#7d5700` | Thresholds, warnings, caution states |

#### Neutral Colors

| Color | Hex | Usage |
|---|---|---|
| Muted Text | `#49454f` | Secondary text, metadata, captions |
| Outline | `#7a757f` | Borders, dividers, axis labels, gridlines |
| Outline Variant | `#cac4cf` | Subtle borders, section dividers, inactive states |

### Color Usage Rules

- Light backgrounds (`#fcf9f8`) are the default for all digital surfaces
- Teal (`#006875`) is the primary accent -- use it for links, interactive elements, and the most important data series
- Magenta (`#a900a9`) is the secondary accent -- use it to create contrast against teal, not as a competitor to it
- The spectral gradient (teal to magenta) is reserved for hero-level elements and decorative accents. Do not overuse it.
- On Surface (`#1c1b1b`) is for all primary text. Never use pure black (`#000000`).
- All borders use 0px radius. Sharp corners throughout -- no rounding anywhere.
- Signal colors (positive, negative, warning) are semantic and should not be used decoratively

---

## 4. Typography

### Type System

FTWR uses a two-font system that mirrors the dual nature of the brand: analytical precision and human communication.

**Primary: Monospace**
`JetBrains Mono / Fira Code / Courier New (fallback)`

Used for: the FTWR wordmark, code blocks, data displays, technical labels, terminal-style content, and anywhere the brand needs to feel like it came from a command line.

**Secondary: Sans-Serif**
Inter / Helvetica Neue / Arial (fallback)

Used for: body text, longer-form content, blog posts, forum posts, and anywhere readability over extended passages matters. Clean and neutral. Does not compete with the monospace elements.

### Type Hierarchy

| Element | Font | Size | Notes |
|---|---|---|---|
| Display / Title | JetBrains Mono | 36-48px | FTWR wordmark, page titles |
| Heading 1 | JetBrains Mono | 28-32px | Section headers |
| Heading 2 | Inter | 22-26px | Subsections |
| Body | Inter | 16-18px | Blog, docs, long-form |
| Labels / Metadata | JetBrains Mono | 11-13px | Uppercase, letter-spacing 0.1em (tracking-widest). Used for section labels, categories, timestamps, tags. |
| Code / Data | JetBrains Mono | 14-16px | Inline code, data values, axis text |
| Caption | Inter | 12-14px | Image captions, footnotes |

### Typography Rules

- Never use decorative or script fonts anywhere in the brand
- Monospace text should feel intentional, not accidental -- if something is in monospace, it should be because it is code, data, or a brand element
- Line height for body text: 1.6-1.8 for readability
- Line height for code blocks: 1.4-1.5
- Letter spacing on the FTWR wordmark: slightly expanded (0.05-0.1em) for presence at large sizes

---

## 5. Logo and Wordmark

### The Wordmark

The primary brand identifier is the wordmark `FTWR` set in monospace, always uppercase, always bold.

The full name `FOLLOW THE WHITE RABBIT` is secondary and used when space allows or when introducing the brand to new audiences.

**Primary Wordmark:** `FTWR`
Always monospace. Always uppercase. Always bold.

**Extended Wordmark:** `FOLLOW THE WHITE RABBIT`
Used for introductions and contexts where the abbreviation is not yet established.

### Logo Mark (Direction)

The logo mark should be developed by a designer. The brief:

- A minimal rabbit silhouette or abstract rabbit form integrated with a data motif
- Possible directions: rabbit silhouette formed by a probability distribution curve, rabbit ears emerging from a candlestick chart, geometric rabbit icon
- Must work in single-color (teal on light, near-black on light, white on teal)
- Must be recognizable at 32x32 pixels (favicons, profile pictures)
- Should feel technical and precise, not cute or cartoonish

### Clear Space and Minimum Size

- Minimum clear space around the wordmark: the height of the "F" in FTWR on all sides
- Minimum wordmark size: 24px for digital, 8mm for print
- Minimum logo mark size: 16px for digital, 5mm for print
- Never stretch, rotate, or apply effects to either mark

### Incorrect Usage

- Do not set the wordmark in a non-monospace font
- Do not use lowercase ("ftwr" or "Ftwr")
- Do not add gradients, shadows, or 3D effects
- Do not place the wordmark on a busy background without a solid backing
- Do not change the color of individual letters
- Do not add taglines or other text directly adjacent to the wordmark

---

## 6. Imagery and Data Visualization

### Photography

FTWR does not rely heavily on photography. When images are used, they should feel clinical and precise rather than atmospheric or moody. Clean environments, data on bright screens, the look of a research interface. Never use stock photos of people cheering at a game or holding phones showing betting apps. That is the aesthetic of the industry FTWR is deliberately positioned against.

### Data Visualization Style

Data visualization is the primary visual language of FTWR. Charts, distributions, heatmaps, and plots are how the brand communicates visually.

**Rules for Charts and Visualizations:**

- Light background (`#fcf9f8` or `#f3f0ef` for cards) is default for all charts
- Teal (`#006875`) for primary data series and positive indicators
- Magenta (`#a900a9`) for secondary data series and comparisons
- Cyan (`#00daf3`) for tertiary data series, sparklines, and supporting detail
- Negative red (`#ba1a1a`) for negative values and loss
- Warning amber (`#7d5700`) for thresholds and warnings
- Axis labels and gridlines in Outline (`#7a757f`), subtle and non-competing
- JetBrains Mono for all data labels, axis text, and numeric values
- Inter for chart titles and annotations
- 0px border radius on all chart elements -- bars, containers, tooltips, legends
- Minimize chartjunk -- no 3D effects, no unnecessary gridlines, no decorative elements
- Always label axes, always include units, always cite the data source
- The spectral gradient may be used for heatmaps and continuous data ranges

### Screenshot Style

Screenshots of code, terminals, or dashboards are core content. Use a light theme consistent with the brand palette. If sharing code, use syntax highlighting that maps to the FTWR color system (teal for strings, magenta for keywords, red for errors) on a light background. Include meaningful code, not lorem ipsum or placeholder data.

---

## 7. Platform-Specific Guidelines

### X (Twitter)

- **Profile picture:** logo mark on light background (`#fcf9f8`) or teal background (`#006875`)
- **Banner:** light, minimal. Subtle data visualization or the extended wordmark with spectral gradient. No busy imagery.
- **Display name:** FTWR
- **Bio:** concise. Something like "Sports data intelligence. Open source tooling. Going down the rabbit hole." Include a link to the blog or GitHub.
- **Pinned post:** an explainer thread about what FTWR is, with links to GitHub/forum/blog
- No hashtag spam. 0-2 relevant hashtags maximum, only when they add discoverability.

### GitHub

- **Organization avatar:** logo mark on light background (`#fcf9f8`) or teal background (`#006875`)
- **Organization bio:** one line explaining the mission
- **README files:** clean, well-structured, with real code examples. No placeholder text. No walls of badges.
- **Repository descriptions:** specific and functional, not marketing language
- Use GitHub Discussions for community conversation within repos

### Discourse Forum

- **Logo:** FTWR wordmark or logo mark on light background
- **Color scheme:** Use Discourse's theme customization to apply the FTWR palette -- light surface background, teal accents, near-black text
- **Category descriptions:** brief, functional, written plainly
- **Pinned topics:** keep to a minimum. One welcome/intro topic, one community guidelines topic. Do not pin aggressively.
- **User badges/flair:** let the trust level system do the work. Do not create excessive custom badges. If custom badges are used, they should reflect real contributions (e.g., "First PR Merged," "Published Author") not vanity metrics.

### Reddit

- **Subreddit icon:** logo mark on light background or teal background
- **Banner:** consistent with X and forum branding
- **Sidebar:** concise explanation of what FTWR is, links to GitHub, forum, and blog
- **Post flair:** use sparingly. Categories like "Analysis," "Tool," "Discussion," "Down the Rabbit Hole" are enough.
- **Rules:** mirror the community principles. No tips without reasoning, no affiliate links, show your work.

### Blog

**Domain:** `blog.ftwr.app`

The blog should be the most complete expression of the FTWR visual identity. Light background, clean typography, excellent code highlighting on light surfaces, well-designed data visualizations with the teal/magenta spectral palette embedded inline. The reading experience should feel like the best technical blogs (Stripe Engineering, Julia Evans) transplanted into the FTWR clinical research aesthetic.

### Landing Page (ftwr.app)

The root domain is a thin, single-page introduction to FTWR. It should load fast, look sharp, and route people to the right destination: blog, forum, GitHub. No fluff, no multi-section marketing page. A terminal-style hero with the FTWR wordmark, a one-line description, and clear command-prompt links out to the properties that matter. Below the fold, a data visualization demo that shows the brand's analytical character. Light background, spectral accents, consistent with all other FTWR surfaces.

---

## 8. Signature Content Format: "Down the Rabbit Hole"

This is the signature FTWR content format. A recurring series that follows a consistent structure: start with a simple, specific observation, then pull the thread until something interesting falls out. Each installment should feel like a small investigation.

### Structure

1. **The Hook** -- a single, specific observation. A number that looks wrong. A line that moved unexpectedly. A dataset that shows something nobody is talking about.

2. **The Dig** -- pull the thread. What does the data actually say? What model explains this? What is the market assuming, and is that assumption correct?

3. **The Finding** -- what did we learn? Is there an edge here? A tool to build? A method to share? Or did the rabbit hole lead to a dead end (which is also worth documenting)?

4. **The Code** -- always end with something tangible. A script, a notebook, a link to the repo. The reader should be able to reproduce what you found.

This format works across all platforms: as an X thread, as a blog post, as a Discord discussion starter. The key is that it always shows the journey, not just the conclusion.

---

## 9. Community Principles

These are not just rules for a Discord server. They are the operating principles of the entire FTWR project. They shape how every piece of content is created and every interaction is handled.

**Transparency Over Mystique** -- The "mystery" in the FTWR brand is about the rabbit hole being deep, not about hiding information. Findings, methods, and code are always shared openly. The persona is mysterious in its aesthetic, not in its substance.

**Newcomers Are Welcome** -- Everyone started somewhere. If someone asks a basic question, they get a helpful answer, not condescension. The barrier to entry should be curiosity, not credentials.

**Accountability** -- When a model is wrong, we say so. When a trade loses, we document why. The FTWR persona does not delete losing calls or quietly move on from bad predictions. The track record is public and honest, including the losses.

**No Gatekeeping** -- The tools are open source. The methods are documented. The community is open. If someone takes FTWR tooling and builds something better with it, that is a success, not a threat.

**Quality Over Activity** -- One well-researched analysis per week is worth more than daily hot takes. One clean, tested PR is worth more than ten rushed commits. The community should reward depth, not volume.

---

## 10. Quick Reference

| Element | Specification |
|---|---|
| Brand Name | FTWR (Follow the White Rabbit) |
| Wordmark Font | JetBrains Mono / Fira Code / Courier New |
| Body Font | Inter / Helvetica Neue / Arial |
| Primary Background | `#fcf9f8` (Warm Off-White) |
| Primary Accent | `#006875` (Teal) |
| Secondary Accent | `#a900a9` (Magenta) |
| Tertiary Accent | `#00daf3` (Cyan) |
| Spectral Gradient | `#006875` to `#a900a9` (Teal to Magenta) |
| Primary Text | `#1c1b1b` (Near Black) |
| Muted Text | `#49454f` |
| Border Radius | 0px everywhere |
| Wordmark Style | Monospace, uppercase, bold, always |
| Label Style | Monospace, uppercase, tracking-widest |
| License | MIT or Apache 2.0 for all code |
| Monetization | None. Free and open. Full stop. |

---

*"The edge is in the method, not the market."*
