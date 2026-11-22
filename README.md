# The Future Tomorrow

**Technology intelligence for business, strategy and investment.**

Explore emerging technologies, their commercial implications, company exposure and source-labelled research. Browse the interactive atlas or open executive-ready slide briefings.

### [Open the live website → https://mengliang10.github.io/future/](https://mengliang10.github.io/future/)

| Explore | Direct link |
| --- | --- |
| **Presentation Studio** — sector briefings and slide decks | [Open presentations](https://mengliang10.github.io/future/presentations/) |
| **Technology Explorer** — search and filter emerging technology records | [Explore technologies](https://mengliang10.github.io/future/explore/) |
| **Future Tech Sectors** — research organised by engineering domain | [Browse sectors](https://mengliang10.github.io/future/sectors/) |
| **Technology Roadmaps** — explore source-estimated horizons | [View roadmaps](https://mengliang10.github.io/future/roadmaps/) |
| **Company Atlas** — listed and private company research | [Explore companies](https://mengliang10.github.io/future/companies/) |
| **Research & Methodology** — evidence, provenance and limitations | [Read methodology](https://mengliang10.github.io/future/research/) |

> **Research caveat:** Most records are migrated research snapshots, **not** live market intelligence or independently verified forecasts. Timing, confidence, valuation and financial observations must be checked against current primary sources before use. This is not investment advice.

## Inside the platform

- **972 technology records** and **567 company records** in the imported/current content set.
- **17 technology categories** for discovery, plus source-stage and horizon filters.
- **11 official market-sector briefings** within **54 deck manifests** (776 rendered slides in the documented build).
- Responsive 16:9 presentations with reading, fullscreen and print/PDF modes.
- Shared content records underpinning multiple pages and evergreen presentations. Fixed snapshots preserve historical versions where configured.

Numbers describe the documented repository build, not live-refreshing datasets.

## Run locally

Requires Node.js **22.12+**.

```bash
git clone https://github.com/mengliang10/future.git
cd future
npm ci
npm run dev
```

Local development: `http://127.0.0.1:4330/` (**local only; not the public site**).

Production build:

```bash
npm run build
npm run preview
```

## Quality checks

```bash
npm run build
npm run audit
npm run qa
```

The build validates structured data. The static audit checks generated internal URLs, assets and original-source downloads; browser QA covers layout and interaction. External websites may change or block automated requests, so external links require separate checking.

## Publishing

GitHub Actions deploys the static Astro build from `main` to **https://mengliang10.github.io/future/**. Configuration is in [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml); the Astro base path is `/future`.

## Repository guide

| Path | Purpose |
| --- | --- |
| [`src/content/`](src/content/) | Structured research, sector records, articles and decks |
| [`src/pages/`](src/pages/) | Page routes and presentation pages |
| [`src/components/`](src/components/) | Reusable research and slide visuals |
| [`src/styles/`](src/styles/) | Website and briefing design |
| [`scripts/`](scripts/) | Validation, QA, updates and import utilities |
| [`AUTHORING.md`](AUTHORING.md) | Content authoring and bulk updates |
| [`MIGRATION.md`](MIGRATION.md) | Source provenance and migration constraints |
| [`DESIGN.md`](DESIGN.md) | Design decisions and reference attribution |

The source import and original Markdown are preserved for provenance. No server-side database, paid API, or runtime backend is required for the published static research experience.

---

**[Visit the website](https://mengliang10.github.io/future/)** · **[Presentation Studio](https://mengliang10.github.io/future/presentations/)** · **[Explore the research](https://mengliang10.github.io/future/explore/)**
