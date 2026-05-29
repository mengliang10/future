# Enhancement 01: CMS Overhaul

## Problem

Manual publishing via Jenkins is a bottleneck that does not scale. The current flow requires SSH access, a working Ruby/Jekyll environment, and manual `git push` to trigger a build. Errors surface late (post-push), file format support is limited to Markdown, and there is no editorial interface for non-technical contributors. As content becomes more granular: per-technology pages, per-stock pages, sector briefings: the publishing loop is the ceiling.

**Specific failure modes today:**
- A bad front-matter YAML silently breaks a page; only visible after deploy.
- No draft/preview mode: content is live or it does not exist.
- No multi-format ingestion (PDF, DOCX, structured JSON → page).
- No scheduled publishing.
- No diff/review step between DB change and live page.

---

## Full-Scale Vision

A headless CMS that acts as the editorial and publishing layer for the entire Martech platform: not just Future Trends. It decouples content authoring from the delivery layer, supports multiple front-ends (Jekyll, Next.js, mobile), validates content before publish, and exposes a GraphQL/REST API so the research pipeline can push content programmatically.

```mermaid
graph LR
    subgraph Ingestion
        PDF[PDF / DOCX]
        JSON[Structured JSON]
        URL[URL / Scrape]
        MD[Raw Markdown]
    end

    subgraph CMS["Headless CMS (e.g. Strapi / Decap / Payload)"]
        VALID[Schema Validation]
        DRAFT[Draft Stage]
        PREVIEW[Preview Renderer]
        SCHED[Scheduled Publish]
        API[Content API]
    end

    subgraph Delivery
        JEKYLL[Jekyll → GitHub Pages]
        NEXT[Next.js → Vercel]
        RSS[RSS / Feeds]
        EMAIL[Email Newsletter]
    end

    PDF --> CMS
    JSON --> CMS
    URL --> CMS
    MD --> CMS
    CMS --> VALID --> DRAFT --> PREVIEW --> SCHED
    API --> JEKYLL
    API --> NEXT
    API --> RSS
    API --> EMAIL
```

---

## Current State vs Target State

| Dimension | Current | Target |
|-----------|---------|--------|
| Authoring | Git + Markdown files | Web UI + API |
| Validation | None (post-push) | Pre-publish schema check |
| Preview | Local Jekyll serve | Hosted preview URL per draft |
| File formats | Markdown only | MD, JSON, PDF, DOCX, HTML |
| Publishing | Manual `git push` → Jenkins | One-click or API-triggered |
| Scheduling | None | Publish at UTC timestamp |
| Multi-site | Single repo | Multi-tenant via `site_id` |
| Rollback | Git revert | One-click version history |

---

## CMS Options Evaluation

```mermaid
quadrantChart
    title CMS Options: Complexity vs Capability
    x-axis Low Complexity --> High Complexity
    y-axis Low Capability --> High Capability
    quadrant-1 Best Fit
    quadrant-2 Overkill
    quadrant-3 Skip
    quadrant-4 Consider Later
    Decap CMS: [0.2, 0.45]
    Strapi: [0.55, 0.80]
    Payload CMS: [0.60, 0.85]
    Contentful: [0.35, 0.75]
    Sanity: [0.45, 0.78]
    Ghost: [0.30, 0.55]
    Directus: [0.50, 0.72]
```

**Recommended path:**
1. **Phase 1 (now):** Decap CMS: Git-backend, zero infra, drops directly into the existing Jekyll/GitHub Pages setup. Adds a web UI over the same Markdown files. No migration required.
2. **Phase 2 (platform scale):** Strapi or Payload CMS: self-hosted, full REST+GraphQL API, multi-site content types, role-based access. Migrates to a VPS alongside the domain migration.

---

## Phased Implementation

```mermaid
gantt
    title CMS Overhaul Phases
    dateFormat  YYYY-MM
    section Phase 1: Decap
    Install Decap CMS config        :p1a, 2026-06, 2w
    Define content schemas (_tech, _stocks, sectors) :p1b, after p1a, 2w
    Add GitHub OAuth provider       :p1c, after p1b, 1w
    Validate editorial preview flow :p1d, after p1c, 1w
    section Phase 2: API Pipeline
    Research pipeline → CMS API     :p2a, 2026-08, 3w
    Multi-format ingest connector   :p2b, after p2a, 3w
    Scheduled publish queue         :p2c, after p2b, 2w
    section Phase 3: Platform CMS
    Strapi / Payload evaluation     :p3a, 2026-11, 2w
    Multi-site content model        :p3b, after p3a, 4w
    Migrate Future Trends + Martech :p3c, after p3b, 4w
```

### Phase 1: Decap CMS (Quick Win)

Decap CMS (formerly Netlify CMS) is a React SPA that commits directly to GitHub. Install is a single HTML file + config YAML.

```yaml
# /admin/config.yml: Decap CMS schema example
backend:
  name: github
  repo: mengliang10/future
  branch: main

media_folder: assets/images
public_folder: /assets/images

collections:
  - name: tech
    label: Tech Nodes
    folder: _tech
    create: true
    slug: "{{slug}}"
    fields:
      - { label: Title, name: title, widget: string }
      - { label: Category, name: category, widget: string }
      - { label: Stage, name: stage, widget: select, options: [mass_production, early_commercial, pilot, proof_of_concept, basic_research, prototype] }
      - { label: Confidence Label, name: confidence_label, widget: string }
      - { label: Horizon, name: horizon, widget: string }
      - { label: Body, name: body, widget: markdown }
```

### Phase 2: Research Pipeline → CMS API

The existing Python research pipeline writes directly to `_tech/*.md` files. In Phase 2 it instead `POST`s to the CMS API, which handles validation, versioning, and publish scheduling.

```mermaid
sequenceDiagram
    participant DB as tech_graph.db
    participant REGEN as regen_tech_pages.py
    participant CMS as CMS API
    participant REPO as GitHub Repo
    participant SITE as Live Site

    DB->>REGEN: node.src_count >= 1
    REGEN->>CMS: POST /api/content/tech {node data}
    CMS->>CMS: Validate schema
    CMS->>CMS: Check diff vs current draft
    CMS->>REPO: Commit _tech/node-id.md
    REPO->>SITE: GitHub Actions build
```

---

## Error Checking Architecture

```mermaid
flowchart TD
    IN[Content Input] --> S1{Schema Valid?}
    S1 -- No --> ERR1[Return validation errors\nwith field-level detail]
    S1 -- Yes --> S2{Front-matter complete?}
    S2 -- No --> ERR2[Flag missing required fields\ne.g. permalink, category]
    S2 -- Yes --> S3{Broken internal links?}
    S3 -- Yes --> WARN[Warn: link /tech/X/ has no target page]
    S3 -- No --> S4{Duplicate slug?}
    S4 -- Yes --> ERR3[Reject: slug conflict with existing page]
    S4 -- No --> DRAFT[Save as Draft]
    DRAFT --> PREVIEW[Generate Preview URL]
    PREVIEW --> APPROVE{Approved?}
    APPROVE -- Yes --> PUBLISH[Trigger build]
    APPROVE -- No --> DRAFT
```

---

## Success Metrics

| Metric | Baseline | Target |
|--------|----------|--------|
| Time from DB update to live page | ~15 min (manual) | <2 min (automated) |
| Publishing errors caught pre-deploy | 0% | >95% |
| Content formats supported | 1 (Markdown) | 5+ |
| Non-technical contributors able to publish | 0 | Yes |
| Sites on same CMS | 1 | 3+ |

---

## Open Questions

- Decap CMS requires GitHub OAuth: does the org allow that app installation?
- Strapi self-host: VPS cost vs Strapi Cloud pricing at platform scale?
- Should the research pipeline remain a direct file writer in Phase 1, or go through CMS API from day one?
