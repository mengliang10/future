#!/usr/bin/env python3
"""
Initializes the Ingestion & Queue Database (data/ingest_queue.db).
Sets up schemas for:
- inbox_items (new research, signals, unstructured notes)
- proposed_connections (graph relationships to review)
- proposed_links (internal & cross-page link suggestions)
- sources_catalog (monitored publications and feeds)
"""

import sqlite3
from pathlib import Path

def init_queue_db():
    base_dir = Path(__file__).resolve().parent.parent
    data_dir = base_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    db_path = data_dir / "ingest_queue.db"

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.executescript("""
    PRAGMA foreign_keys = ON;

    CREATE TABLE IF NOT EXISTS inbox_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        raw_content TEXT,
        source_url TEXT,
        source_type TEXT DEFAULT 'web_article', -- web_article, earnings_call, academic_paper, note, tweet_x, report
        suggested_sector TEXT,
        suggested_technologies TEXT, -- JSON array string e.g. ["optical-interconnects", "gpu-compute"]
        suggested_companies TEXT,    -- JSON array string e.g. ["nvda", "tsm"]
        priority INTEGER DEFAULT 3,  -- 1 (urgent) to 5 (low)
        status TEXT DEFAULT 'queued', -- queued, reviewing, approved, merged_into_site, archived, rejected
        curator_notes TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS proposed_connections (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        inbox_item_id INTEGER REFERENCES inbox_items(id) ON DELETE SET NULL,
        from_entity_type TEXT NOT NULL, -- technology, company, sector
        from_entity_id TEXT NOT NULL,
        to_entity_type TEXT NOT NULL,
        to_entity_id TEXT NOT NULL,
        relationship TEXT NOT NULL,     -- enables, supplies, competes_with, invested_in, partners_with, depends_on
        confidence_score REAL DEFAULT 0.8,
        evidence_text TEXT,
        status TEXT DEFAULT 'proposed', -- proposed, approved, applied_to_content, rejected
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS proposed_links (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        inbox_item_id INTEGER REFERENCES inbox_items(id) ON DELETE SET NULL,
        source_url_path TEXT NOT NULL,
        target_url_path TEXT NOT NULL,
        anchor_text TEXT NOT NULL,
        context_text TEXT,
        placement_hint TEXT,
        status TEXT DEFAULT 'proposed', -- proposed, approved, applied_to_content, rejected
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS sources_catalog (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        domain TEXT,
        feed_or_api_url TEXT,
        category TEXT,
        reliability_tier TEXT DEFAULT 'tier_1_primary', -- tier_1_primary, tier_2_expert_analysis, tier_3_general
        notes TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS queue_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        action TEXT NOT NULL,
        target_type TEXT NOT NULL,
        target_id INTEGER,
        details TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE INDEX IF NOT EXISTS idx_inbox_status ON inbox_items(status);
    CREATE INDEX IF NOT EXISTS idx_inbox_priority ON inbox_items(priority);
    CREATE INDEX IF NOT EXISTS idx_connections_status ON proposed_connections(status);
    CREATE INDEX IF NOT EXISTS idx_links_status ON proposed_links(status);
    """)

    # Seed baseline primary sources if empty
    cur.execute("SELECT COUNT(*) FROM sources_catalog")
    if cur.fetchone()[0] == 0:
        seed_sources = [
            ("arXiv Computer Science & Quantum", "arxiv.org", "http://export.arxiv.org/rss/cs", "academic", "tier_1_primary", "Pre-print academic papers"),
            ("US Patent & Trademark Office (USPTO)", "uspto.gov", "", "patents", "tier_1_primary", "Weekly assigned patents"),
            ("SEC EDGAR 10-K & 10-Q Filings", "sec.gov", "https://www.sec.gov/edgar", "filings", "tier_1_primary", "Audited company financial & tech disclosures"),
            ("SemiAnalysis", "semianalysis.com", "", "semiconductors", "tier_2_expert_analysis", "Deep semiconductor architecture analysis"),
            ("Nature Biotechnology", "nature.com/nbt", "", "biotech", "tier_1_primary", "Peer-reviewed biotech breakthroughs")
        ]
        cur.executemany("""
            INSERT INTO sources_catalog (name, domain, feed_or_api_url, category, reliability_tier, notes)
            VALUES (?, ?, ?, ?, ?, ?)
        """, seed_sources)

    conn.commit()
    conn.close()
    print(f"[✓] Initialized Ingestion & Queue database at: {db_path}")

if __name__ == "__main__":
    init_queue_db()
