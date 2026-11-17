# Private evidence inbox

The pipeline collects evidence for review and never edits published pages or
changes article read/starred status in Miniflux. Existing RSS and graph scripts
are unchanged. Their outputs can be imported into this inbox using import-json;
they are not automatically redirected through it.

## Storage

- `research/ingest/<URL hash>.json`: first collected article snapshot.
- `research/future_research_consolidated.db`: evidence, source provenance,
  proposed changes, and append-only review decisions (`inbox_*` tables).
- `research/staging/review-queue.json`: regeneratable queue; SQLite is authoritative.
- `research/database/`: reserved for other private database artifacts. The existing
  consolidated database remains in place; existing graph DBs are untouched.

`research/` is already Git-ignored; the installer also explicitly excludes it from
Jekyll output. Do not force-add private files to Git. No historical data is migrated.
The stored article snapshot is evidence, not a verified claim. A reviewer supplies
the claim, destination and replacement before approval. URL deduplication removes
tracking parameters and fragments; it does not merge syndicated articles or
perform semantic deduplication. Changed content at the same URL retains its first
snapshot; versioned article snapshots are future work.

## Miniflux

Reads `MINIFLUX_BASE_URL` and `MINIFLUX_API_KEY` from the environment, falling back
to `~/.config/environment.d/miniflux.conf` (plain KEY=value, optionally quoted).
No shell evaluation is performed. API token authentication and GET /v1/entries
follow https://miniflux.app/docs/api.html. HTTPS is required except on loopback.
A seven-day overlapping publication-time window and URL deduplication allow safe
reruns; articles newly fetched with older publication dates require a wider window.
Both read and unread entries are collected. All categories are collected unless
`--category ID` is supplied. The upstream publisher remains the evidence source URL;
Miniflux is the collection channel, not an independent corroborating source.

From the site root:

```bash
bash scripts/ingest-private.sh
bash scripts/ingest-private.sh --days 30 --category 42
python3 scripts/ingestion.py queue
```

An example local daily crontab entry (uses the machine's timezone):

```cron
0 7 * * * /bin/bash /media/ml/data/future/scripts/ingest-private.sh
```

This is a scheduling example, not an installed job. Run locally, where credentials
and private data exist, rather than on the public GitHub Actions runner.

## Other sources

Adapt RSS, papers, or manual research to a JSON array:

```json
[{"id":"source-item-id","url":"https://example.org/article","title":"Article title","published_at":"2026-11-17T00:00:00Z","content":"Supporting text"}]
```

```bash
python3 scripts/ingestion.py import-json /path/articles.json --source rss
```

## Review

Use the complete ID in `research/staging/review-queue.json`:

```bash
python3 scripts/ingestion.py review FULL_ID reviewed --note 'Checked primary source'
python3 scripts/ingestion.py review FULL_ID approved --target _tech/example.md --claim 'Verified claim' --replacement 'Proposed page text' --note 'Evidence supports this edit'
```

Allowed transitions: new → reviewed/rejected; reviewed → approved/rejected;
approved → published/reviewed/rejected; rejected → new. Published is terminal.
Approval requires destination, claim, replacement and review note. Make and verify
the approved site edit separately, then record it with:

```bash
python3 scripts/ingestion.py review FULL_ID published --note 'Applied in commit HASH'
```

The published status is a manual record, not proof of deployment. Nothing is
published automatically. Existing legacy generators may still write site data;
this inbox does not place a review gate around those older pipelines.
