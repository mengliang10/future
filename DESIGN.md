# Chirping reference redesign

Reference: https://aneejian.com/chirping-astro/
Source theme: https://github.com/kannansuresh/chirping-astro (MIT; licence retained at `public/licenses/chirping-astro-MIT.txt`).

Inspected the live HTML, stylesheet, theme layout source, Firecrawl branding output and an actual 1440×1000 screenshot saved in `reference/chirping/desktop.png` on 16 November 2026. Third-party branding guesses about framework/components were not used as authoritative: the source identifies Astro/Tailwind/daisyUI.

## Observed patterns

- Desktop: fixed 260px left sidebar (300px at very wide widths), circular avatar, name/tagline, icon-led vertical navigation and bottom utility buttons.
- Light grey page surface, white cards, thin grey borders, small corner radius, restrained blue links.
- Source Sans 3 for reading, headings around 25px in the article feed, understated metadata around 12px.
- Compact top bar with location and rounded search field; article stream in the centre; 220–240px supporting links/tags panel on the right.
- Long-form pages use readable typography and restrained section spacing rather than promotional hero typography.

## Implementation

`Site.astro` now provides the left sidebar, top bar, centre content column and right reading panel. `chirping.css` applies the reference's structure and typographic hierarchy to the existing research pages, collection tools and detail pages. The homepage is a post-card feed. The previous large marketing headline, count strip and green feature panels are removed from the homepage.

Self-hosted Source Sans 3 regular/semibold/bold files were retrieved from the supplied reference; its OFL licence is retained. The logo/avatar is a new simple FT orbital mark, not the theme mascot. Brand text, research data and briefing content remain this project's own.

Extracted colour evidence: reference branding reports background #F4F5F6, body #5A5C60 and primary/link #2D509F. Implementation uses those roles and related grey borders. Sidebar widths come from source theme CSS; avatar sizing, right-panel spacing and responsive composition are adapted to this content.

Custom functional adaptations: local theme toggle, / keyboard shortcut to search, mobile sidebar with Escape/overlay close, existing data search/filtering and preserved Astro page transitions. No language menu or comments service was added because this project has no translated content or configured comment backend.

The Reveal.js deck renderer and data-update hooks are preserved; this change concerns the research website's presentation and browsing layout. Before-change source layout, styles and homepage are in `source/design-backups/before-chirping/`.

## Visual discovery layer
Sector colours connect category cards, catalogue rows, record headings and briefing previews. The homepage includes an original orbital illustration, counts from collections, six horizon bins and linked research cards. The Roadmaps page is a filterable sector-by-horizon count matrix with 12 results per page, shareable URL filters and a full-record no-JavaScript fallback. Colour intensity encodes record count only. Year bins use imported estimateYear values; missing years remain a separate group. The sidebar maturity donut groups source stage labels, not independently verified commercial progress. Dark mode and reduced-motion preferences are supported.
