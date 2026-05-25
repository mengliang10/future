# Enhancement 05 — Martech Platform Consolidation

## Problem

Two projects currently exist in separate directories with separate repositories, Jekyll configurations, and development workflows:

- `/Projects/future/` — Future Trends site (live, 212 tech pages, research pipeline, stocks)
- `/Projects/Martech/` — Martech Directory platform (planning phase, Phase 1 not yet shipped)

They share: the same Jekyll stack, the same SQLite/Python research pipeline approach, the same target audience (investors, technologists, marketers), and the same eventual monetisation model. Running them as independent silos means duplicated infrastructure, split attention, and missed cross-linking opportunities. The consolidation decision is: **one platform, two (or more) content verticals**.

---

## Full-Scale Vision

A single Martech Platform that hosts multiple content verticals under one codebase, one CMS, one analytics stack, one ad server, and one domain. Each vertical (Future Trends, Martech Directory, and future additions) is a sub-site with its own URL path, design skin, and content pipeline — but shares all infrastructure.

```mermaid
graph TD
    subgraph Platform["Martech Platform — Single Repo"]
        INFRA[Shared Infrastructure\nJekyll / CMS / Pipeline / DB]
        ADS[Ad Server]
        ANA[Analytics]
        SEO_ENGINE[SEO + GEO Engine]
    end

    subgraph Verticals["Content Verticals"]
        FT["Future Trends\n/future/ → futuretrends.io"]
        MT["Martech Directory\n/martech/ → martech.io"]
        V3["Vertical 3\nTBD"]
    end

    subgraph Revenue["Revenue"]
        ADSENSE[AdSense]
        DIRECT[Direct Campaigns]
        SAAS[Platform SaaS]
        DATA[Data Products]
    end

    INFRA --> FT
    INFRA --> MT
    INFRA --> V3
    FT --> ADS --> ADSENSE
    MT --> ADS --> DIRECT
    Platform --> SEO_ENGINE
    Platform --> ANA
    ANA --> DATA
    Platform --> SAAS
```

---

## Current State — Two Separate Repos

```mermaid
graph LR
    subgraph RepoA["/Projects/future (live)"]
        A_SITE[Jekyll site\n212 tech pages\n77 stocks]
        A_PIPE[Research pipeline\ntech_graph.db\nstocks.db]
        A_GH[GitHub Pages\nmengliang10/future]
    end

    subgraph RepoB["/Projects/Martech (planning)"]
        B_SITE[Jekyll site\nPhase 1 not shipped]
        B_PIPE[Python pipeline\nPlanned]
        B_GH[No live site yet]
    end

    A_SITE -.->|Duplicated Jekyll setup| B_SITE
    A_PIPE -.->|No shared DB| B_PIPE
```

**Pain points:**
- `_config.yml`, layouts, and CSS maintained in two places.
- Martech has a separate `REQUIREMENTS.md`, `DEVELOPMENT.md` — no shared backlog.
- No cross-linking between Future Trends tech nodes and Martech tool pages.
- Two separate CI/CD pipelines once Martech ships.

---

## Consolidation Options

```mermaid
flowchart TD
    DECISION{Consolidation approach?} --> OPT1
    DECISION --> OPT2
    DECISION --> OPT3

    OPT1["Option A: Monorepo\nBoth sites in one repo\nShared _layouts, _includes, _plugins\nSeparate _config per site"] --> A_PROS["✓ Single CI/CD\n✓ Shared components\n✗ Build time increases\n✗ GitHub Pages multi-site constraints"]

    OPT2["Option B: Shared Gem / Theme\nCommon Jekyll theme as Ruby gem\nEach site installs it as dependency"] --> B_PROS["✓ Clean separation\n✓ Independent deploys\n✗ Gem release overhead\n✗ Complex for solo dev"]

    OPT3["Option C: Platform Monorepo\n+ Separate deploy targets\nShared pipeline + DB\nTwo GitHub Pages or one VPS with nginx routing"] --> C_PROS["✓ Best of both — unified pipeline\n✓ Independent URLs and themes\n✓ Scales to N verticals\n★ Recommended"]
```

**Recommendation: Option C** — shared pipeline and DB infrastructure in one repo, separate Jekyll configs deployed to separate paths or domains, unified via Nginx on a VPS (links to Enhancement 06 — Domain Migration).

---

## Target Architecture (Post-Consolidation)

```mermaid
graph TD
    subgraph Repo["mengliang10/platform (monorepo)"]
        subgraph Shared["shared/"]
            PIPELINE[research_pipeline/\ntech_graph.db, entity_stock.db]
            LAYOUTS[_layouts/ + _includes/]
            SCRIPTS[scripts/ — generate_site.py, regen_pages.py]
            STYLES[assets/css/ — design tokens]
        end

        subgraph SiteFT["sites/future-trends/"]
            FT_CONFIG[_config.yml]
            FT_TECH[_tech/*.md]
            FT_STOCKS[_stocks/*.md]
            FT_SECTORS[sectors/*.md]
        end

        subgraph SiteMT["sites/martech/"]
            MT_CONFIG[_config.yml]
            MT_TOOLS[_tools/*.md]
            MT_STACKS[_stacks/*.md]
            MT_GUIDES[guides/*.md]
        end
    end

    subgraph Deploy["Deploy Targets"]
        FT_DOMAIN[futuretrends.io]
        MT_DOMAIN[martech.io]
    end

    SiteFT --> FT_DOMAIN
    SiteMT --> MT_DOMAIN
    Shared --> SiteFT
    Shared --> SiteMT
```

---

## Cross-Linking Value

The highest immediate value of consolidation is bidirectional cross-linking:

| Future Trends Page | Links to Martech Page |
|--------------------|----------------------|
| /tech/marketing-ai-automation/ | /martech/tools/jasper-ai/, /martech/stacks/content-marketing/ |
| /tech/customer-data-platforms/ | /martech/tools/segment/, /martech/tools/rudderstack/ |
| /tech/programmatic-advertising/ | /martech/tools/gam/, /martech/stacks/adtech/ |
| /sectors/marketing/ | /martech/ (directory index) |

This creates a content flywheel: Future Trends attracts research-intent traffic → Martech Directory captures implementation-intent traffic → both monetise via ads and platform.

```mermaid
flowchart LR
    USER[Research User] -->|Searches: "CDP technology 2026"| FT[Future Trends\n/tech/customer-data-platforms/]
    FT -->|"See CDP tools →"| MT[Martech Directory\n/martech/tools/cdp/]
    MT -->|"Build your CDP stack →"| BUILDER[Stack Builder\nLead gen / SaaS]
    BUILDER -->|Conversion| REVENUE[Platform Revenue]
```

---

## Martech Project Status (Current)

From `DEVELOPMENT.md` review:

| Phase | Status | Key Deliverables |
|-------|--------|-----------------|
| 1 — Content Foundation | Planning | 100+ tool pages, directory |
| 2 — Stack Builder | Planning | Interactive builder, plan generator |
| 3 — Research Pipeline | Planning | Automated scraping → DB → YAML |
| 4 — Monetization | Future | Accounts, AI plans, payments |

**Recommendation:** Halt independent Martech development. Invest the Phase 1 effort into the consolidated platform repo. The Martech site ships under the unified platform infrastructure — no separate Jekyll config, no separate pipeline.

---

## Migration Plan

```mermaid
gantt
    title Martech Consolidation Timeline
    dateFormat YYYY-MM
    section Prep
    Audit both repos for shared components   :m1, 2026-06, 1w
    Define monorepo directory structure       :m2, after m1, 1w
    section Migration
    Move shared layouts + CSS to shared/     :m3, after m2, 2w
    Migrate Future Trends to sites/future/   :m4, after m3, 2w
    Bootstrap sites/martech/ with Phase 1    :m5, after m4, 3w
    section Integration
    Shared pipeline reads → both sites       :m6, after m5, 2w
    Cross-linking injection in templates     :m7, after m6, 1w
    Unified CI/CD (GitHub Actions matrix)   :m8, after m7, 1w
```

---

## Success Metrics

| Metric | Baseline | Target |
|--------|----------|--------|
| Separate repos to maintain | 2 | 1 |
| Shared layout components | 0 | 100% |
| Cross-links between verticals | 0 | 50+ |
| CI/CD pipelines | 1 (future only) | 1 (both sites) |
| Time to launch new vertical | Weeks | Days |

---

## Open Questions

- GitHub Pages supports only one Pages site per repo at the free tier — does consolidation require a move to a custom domain + VPS? (Yes — see Enhancement 06.)
- Should the research pipeline DB live in the shared monorepo or remain in `/Trading/Research/`? The Trading pipeline has broader scope; keep it separate but add a sync/export step to the platform repo.
- Martech tool data (tool names, pricing, integrations) is a different schema from tech node data — does a shared CMS accommodate both cleanly, or do they need separate collections?
