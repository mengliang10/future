# The Future Tomorrow

A local Astro research site for technology, business and investment readers, migrated from `mengliang10/future`.

## Local preview

```sh
npm ci
npm run build
npm run preview
```

Default address: http://127.0.0.1:4330/

Development: `npm run dev`. The website is static and can later be hosted on GitHub Pages. Nothing in this project automatically publishes or changes the live source repository.

## What is included

- 972 technology records and 567 company records, including newer private future-tech companies alongside the imported source set.
- 15 normalised sectors, with original category labels retained in each record.
- Search/filter/pagination explorers, roadmap views, linked companies and original research pages.
- 54 briefing manifests generating 776 slides, including 11 official sector decks at 17 slides each, plus one example fixed snapshot.
- A common 16:9 Reveal.js slide renderer with generated SVG diagrams (actors, risk, funnel, portfolio map, technology anatomy), responsive reading mode, browser Print/PDF and shared source hooks.
- Original repository with Git history in `source/original`, original Markdown downloads under `public/source`, and machine-readable import manifest in `qa/import-manifest.json`.

The records are imported research. Claims, timelines, confidence scores, financial data and source counts have **not** been independently revalidated. The site labels this status and does not describe the market snapshot as live data. A rebuild is not a research review.

## File structure

```text
src/content/technologies/    canonical structured technology data + preserved notes
src/content/companies/      company records
src/content/sectors/        consistent aliases and business/investor questions
src/content/blocks/         reusable slide framework text
src/content/decks/          ordered references to records and blocks
src/content/articles/       preserved original narrative pages
src/components/Slide.astro  one slide template shared by every briefing
src/styles/slides.css       shared slide theme
src/styles/site.css         shared website theme
scripts/update-record.mjs   targeted changes + dependency impact + backups
scripts/snapshot-deck.mjs   fixed historical deck data
scripts/dependencies.mjs    machine-readable dependency map
```

See [AUTHORING.md](AUTHORING.md) for mass updates and [MIGRATION.md](MIGRATION.md) for provenance and limitations.

## Checks

```sh
npm run build
npm run qa
node scripts/dependencies.mjs
```

Browser QA covers desktop/tablet/mobile layouts, filters, navigation, no-JavaScript fallback and every generated slide for content/footer overlap. The update propagation test makes a temporary edit, checks all evergreen consumers, verifies snapshot stability, restores the original record and rebuilds:

```sh
node scripts/verify-shared-update.mjs
```

The preview uses no analytics or live contact submission. Original contact details remain in the preserved source pages. Existing market-fetch scripts remain archived in `source/original/scripts`; no scheduled tasks were installed.

## Current visual design

The research website now follows the supplied Chirping Astro reference: fixed left sidebar, a compact search/location top bar, a white article-card stream on grey, a right supporting-links panel, Source Sans typography and restrained blue links. Mobile uses an overlay sidebar. Dark mode persists locally, and `/` focuses search. See [DESIGN.md](DESIGN.md) for reference evidence and implementation details. Existing content IDs, deck manifests and batch-update hooks are unchanged. Original before-redesign files are in `source/design-backups/before-chirping`.
