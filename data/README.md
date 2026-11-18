# Local Databases for The Future Tomorrow

This directory contains two dedicated, high-performance SQLite databases running locally on your laptop:

1. **`site_graph.db`**: The complete knowledge graph, URL map, and link topology of the entire site.
2. **`ingest_queue.db`**: An asynchronous staging database to ingest, triage, and queue incoming signals, research notes, proposed entity relationships, and cross-page links before publishing.

---

## 1. `site_graph.db` (Site Topology & Knowledge Graph)

Generated automatically by `python3 scripts/build-site-graph.py`. It inspects all generated static HTML pages in `dist/` and structured entity JSON files in `src/content/`.

### Schema Overview:
* **`pages`**: All 1,199 site pages (`url_path`, `title`, `page_type`, `in_degree`, `out_degree`, `is_orphan`).
* **`links`**: 50,108+ indexed hyperlinks (`source_url`, `target_url`, `raw_href`, `anchor_text`, `link_type`, `is_broken`, `error_reason`).
* **`entities`**: 1,151 structured entities (`technology`, `company`, `sector`, `deck`).
* **`entity_connections`**: 1,956 relational graph edges (`belongs_to_sector`, `linked_company`, `includes_technology`).
* **`graph_summary`**: High-level telemetry and status metrics.

### Useful CLI Commands:
```bash
# View overall site link summary & health
python3 scripts/query-graph.py summary

# Verify that zero broken or dead links exist
python3 scripts/query-graph.py dead-links

# Find all pages linking to a specific page or company (e.g. Nvidia)
python3 scripts/query-graph.py backlinks /companies/nvda/

# Inspect outgoing links on any page
python3 scripts/query-graph.py outbound /roadmaps/

# Explore connected technologies, companies, and decks for an entity
python3 scripts/query-graph.py entity nvda

# View the top 20 most connected hub pages
python3 scripts/query-graph.py top-hubs

# Check for orphan pages (pages unreachable from navigation)
python3 scripts/query-graph.py orphans
```

---

## 2. `ingest_queue.db` (Research Ingest & Connection Queue)

Managed by `python3 scripts/queue.py`. Use this database to store raw notes, links, papers, and proposed connections as you research throughout the day, without modifying production files directly.

### Schema Overview:
* **`inbox_items`**: Queued raw notes, URLs, summaries, suggested sectors, and priority tags (`1=urgent` to `5=low`).
* **`proposed_connections`**: Graph edges between technologies, companies, and sectors (`supplies`, `enables`, `competes_with`, `invested_in`) with confidence scores and evidence citations.
* **`proposed_links`**: Suggested cross-links between pages (`source_url_path` -> `target_url_path`) with proposed anchor text and context.
* **`sources_catalog`**: Monitored publications (arXiv, USPTO, SEC EDGAR, industry analysis) and feeds.
* **`queue_logs`**: Full audit log of triage actions.

### Useful CLI Commands:
```bash
# View queue status and pending items
python3 scripts/queue.py status

# List queued research items
python3 scripts/queue.py list

# Add a new research item or article to the queue
python3 scripts/queue.py add "Optical Switching for AI Datacenters" \
  --url "https://example.com/optical-breakthrough" \
  --sector "semiconductors" \
  --techs "photonic-interconnects,gpu-compute-cluster" \
  --companies "tsm,nvda" \
  --priority 1 \
  --content "New 200Gbps per lane co-packaged optics demonstration."

# Propose an entity connection
python3 scripts/queue.py connect \
  --from-id "tsm" --from-type "company" \
  --to-id "gpu-compute-cluster" --to-type "technology" \
  --rel "supplies" \
  --evidence "Key packaging partner for Blackwell and future optical clusters"

# Propose an internal link between pages
python3 scripts/queue.py link \
  --source "/companies/tsm/" \
  --target "/tech/gpu-compute-cluster/" \
  --anchor "optical co-packaged GPU nodes"

# Approve a queued item for merging
python3 scripts/queue.py approve 1
```
