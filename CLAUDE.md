# FTWR (Follow the White Rabbit)

## What This Is

FTWR is an open source developer community and online persona around sports data intelligence, analytics, modelling, and arbitrage. The website is the public-facing front door at ftwr.app.

## Project Documents

Read these before doing any design or development work:

- `FTWR-Brand-Guide.md` -- full visual identity spec, color tokens, typography, platform guidelines
- `FTWR-Strategy-Plan.md` -- brand pillars, platform strategy, technical architecture
- `FTWR-90-Day-Plan.md` -- marketing, content, and platform launch plan

## Domain Architecture

```
ftwr.app                    -- Landing page (static, this repo)
blog.ftwr.app               -- Blog (Astro/Hugo, separate repo)
ftwr.discourse.group        -- Community forum (Discourse free plan)
github.com/ftwr-dev         -- GitHub org
```

## Design System

### Colors

Light mode only. No dark mode.

| Token | Hex | Usage |
|---|---|---|
| Surface | #fcf9f8 | Page background |
| Surface Container | #f3f0ef | Cards, panels |
| Surface Container High | #ede9e8 | Active/selected states |
| On Surface | #1c1b1b | Primary text (never use pure #000000) |
| On Surface Variant | #474747 | Secondary text |
| Outline | #777777 | Borders, axis labels |
| Outline Variant | #c6c6c6 | Subtle borders |
| Secondary (Teal) | #006875 | Primary accent, links, key data |
| Tertiary (Magenta) | #a900a9 | Secondary accent, highlights |
| Cyan | #00daf3 | Tertiary accent, sparklines |
| Error | #ba1a1a | Negative signals, errors |
| Spectral Gradient | #006875 to #a900a9 | Hero accents, decorative. `linear-gradient(90deg, #006875 0%, #a900a9 100%)` |

### Typography

- **Headings, code, data, labels:** JetBrains Mono
- **Body text:** Inter
- **Labels/metadata:** JetBrains Mono, uppercase, letter-spacing 0.1em
- Google Fonts: `families=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500;700;800`

### Spacing and Shape

- Border radius: 0px everywhere. No rounding on anything.
- Sharp corners on all elements: buttons, cards, inputs, chart bars, tooltips.

## Existing Landing Page

`index.html` is a complete single-file landing page with:
- Nav bar with FTWR wordmark and terminal command links
- Hero section: "FOLLOW THE WHITE RABBIT." with command-prompt style navigation
- Data visualization demo section with real Poisson distribution calculations
- Grouped bar charts, sparklines, heatmap, league edge bars, match table
- All vanilla HTML/CSS/JS, no build step, no dependencies beyond Google Fonts
- CSS custom properties match the design system tokens above

## Code Conventions

- No em dashes, no emojis in content or comments
- No mock or placeholder data -- all visualizations use real calculations
- Single-file HTML for landing page (CSS and JS inline)
- Vanilla JS preferred for the landing page; no framework required
- Semantic HTML, accessible markup
- Mobile responsive

## What NOT to Do

- Do not add dark mode
- Do not add border radius to anything
- Do not use pure black (#000000) for text
- Do not add build tools or bundlers to the landing page
- Do not create separate CSS/JS files for the landing page (keep it single-file)
- Do not use placeholder or lorem ipsum text
- Do not add monetization, pricing, or premium tier language anywhere
