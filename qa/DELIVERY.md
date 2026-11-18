# Local delivery — 16 November 2026

Preview: http://127.0.0.1:4330/
Presentations: http://127.0.0.1:4330/presentations/

Local directory: `/media/ml/Storage/The Future Tomorrow/`

- Astro build: 1,199 pages.
- Migrated records: 913 technologies, 137 companies, 15 normalised sectors, 39 reference pages.
- Presentations: 85 evergreen briefings and 1 example fixed snapshot, 1,183 rendered slides.
- Browser checks: 32 route/viewport combinations, plus all 86 decks and 1,183 slide layouts. No detected slide/footer overlap, horizontal page overflow or runtime errors in the checked views.
- Search, sector/category aliases, company type filtering, mobile menu, page transitions and no-JavaScript browsing passed.
- Central-update verification: one shared block edit propagated to all 85 evergreen decks; the pinned snapshot retained its original content. Test restored the original content and rebuilt.
- Internal-link audit: no missing internal target paths.
- Source preservation audit: original Markdown downloads match source manifest hashes.

See `browser-report.json`, `shared-update-verification.json`, `site-audit.json`, `validation.json` and `dependencies.json` for evidence.

Limitations: the inherited technology/company claims were not independently fact-checked. The briefings are generated from imported records, with business/investment questions, rather than newly researched investment recommendations. Market data is an imported snapshot. One missing source company relationship (`nrg`) is explicitly reported rather than fabricated. No live site was changed or published.

## Chirping-format redesign

The research site now follows the supplied Chirping Astro layout: fixed left navigation, circular FT avatar, compact location/search bar, white article cards, light grey background, blue links, Source Sans typography and a supporting right panel. All research pages share this visual system. Mobile uses an overlay sidebar. Dark mode persists between pages; `/` focuses site search.

Latest checks: 32 route/viewport checks, 86 decks and 1,183 slide layouts passed; no runtime errors, no broken internal paths and no original Markdown hash mismatches. Font/image loading, theme toggle/persistence and search shortcut were also checked. The presentation renderer and batch-update hooks are preserved. See DESIGN.md for reference evidence and adaptations.
