#!/usr/bin/env python3
"""
Builds the complete Site Knowledge Graph & Link Map into SQLite (data/site_graph.db).
Crawls the built static output (dist/) and source content (src/content/).
Maps all pages, internal links, anchors, dead links, backlinks, and entity connections.
"""

import sys
import os
import json
import sqlite3
from pathlib import Path
from urllib.parse import urlsplit, unquote
from bs4 import BeautifulSoup

def main():
    base_dir = Path(__file__).resolve().parent.parent
    dist_dir = base_dir / "dist"
    content_dir = base_dir / "src" / "content"
    data_dir = base_dir / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    db_path = data_dir / "site_graph.db"

    print(f"[*] Base Directory: {base_dir}")
    print(f"[*] Target Database: {db_path}")

    if not dist_dir.exists():
        print(f"[!] dist directory not found at {dist_dir}. Run `npm run build` first!")
        sys.exit(1)

    # Initialize SQLite database
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.executescript("""
    PRAGMA foreign_keys = ON;

    DROP TABLE IF EXISTS links;
    DROP TABLE IF EXISTS entity_connections;
    DROP TABLE IF EXISTS entities;
    DROP TABLE IF EXISTS pages;
    DROP TABLE IF EXISTS graph_summary;

    CREATE TABLE pages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url_path TEXT UNIQUE NOT NULL,
        title TEXT,
        page_type TEXT,
        entity_id TEXT,
        html_file TEXT,
        source_file TEXT,
        in_degree INTEGER DEFAULT 0,
        out_degree INTEGER DEFAULT 0,
        is_orphan INTEGER DEFAULT 0,
        scanned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE links (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source_page_id INTEGER REFERENCES pages(id) ON DELETE CASCADE,
        source_url TEXT NOT NULL,
        raw_href TEXT NOT NULL,
        target_url TEXT,
        target_page_id INTEGER REFERENCES pages(id) ON DELETE SET NULL,
        target_fragment TEXT,
        anchor_text TEXT,
        link_type TEXT NOT NULL,
        is_broken INTEGER DEFAULT 0,
        error_reason TEXT
    );

    CREATE TABLE entities (
        id TEXT PRIMARY KEY,
        entity_type TEXT NOT NULL,
        name TEXT NOT NULL,
        sector TEXT,
        metadata_json TEXT
    );

    CREATE TABLE entity_connections (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        from_entity_id TEXT NOT NULL,
        from_entity_type TEXT NOT NULL,
        to_entity_id TEXT NOT NULL,
        to_entity_type TEXT NOT NULL,
        connection_type TEXT NOT NULL,
        source TEXT
    );

    CREATE TABLE graph_summary (
        metric TEXT PRIMARY KEY,
        value TEXT,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE INDEX idx_pages_url ON pages(url_path);
    CREATE INDEX idx_pages_type ON pages(page_type);
    CREATE INDEX idx_links_source ON links(source_page_id);
    CREATE INDEX idx_links_target ON links(target_page_id);
    CREATE INDEX idx_links_broken ON links(is_broken);
    CREATE INDEX idx_connections_from ON entity_connections(from_entity_id);
    CREATE INDEX idx_connections_to ON entity_connections(to_entity_id);
    """)

    # 1. Map all HTML pages in dist
    print("[*] Scanning built HTML files in dist/...")
    html_files = list(dist_dir.rglob("*.html"))
    print(f"[*] Found {len(html_files)} HTML pages.")

    pages_data = [] # list of dicts
    page_by_url = {}

    for file_path in html_files:
        rel = file_path.relative_to(dist_dir)
        if rel.name == "index.html":
            parent = rel.parent.as_posix()
            url_path = "/future/" if parent == "." else f"/future/{parent}/"
        elif rel.name == "404.html":
            url_path = "/future/404.html"
        else:
            url_path = f"/future/{rel.as_posix()}"

        # Classify page type
        page_type = "misc"
        entity_id = None
        if url_path == "/future/":
            page_type = "home"
        elif url_path.startswith("/future/tech/"):
            page_type = "technology"
            parts = [p for p in url_path.replace("/future", "").split("/") if p]
            if len(parts) >= 2:
                entity_id = parts[1]
        elif url_path.startswith("/future/companies/"):
            parts = [p for p in url_path.replace("/future", "").split("/") if p]
            page_type = "company" if len(parts) >= 2 else "company_hub"
            if len(parts) >= 2:
                entity_id = parts[1]
        elif url_path.startswith("/future/sectors/"):
            parts = [p for p in url_path.replace("/future", "").split("/") if p]
            page_type = "sector" if len(parts) >= 2 else "sector_hub"
            if len(parts) >= 2:
                entity_id = parts[1]
        elif url_path.startswith("/future/presentations/"):
            parts = [p for p in url_path.replace("/future", "").split("/") if p]
            page_type = "deck" if len(parts) >= 2 else "deck_hub"
            if len(parts) >= 2:
                entity_id = parts[1]
        elif url_path.startswith("/future/read/"):
            page_type = "article"
            parts = [p for p in url_path.replace("/future", "").split("/") if p]
            if len(parts) >= 2:
                entity_id = parts[1]
        elif url_path in ["/future/explore/", "/future/roadmaps/", "/future/research/", "/future/markets/"]:
            page_type = "hub"

        # Read HTML to get title
        try:
            content = file_path.read_text(encoding="utf-8", errors="replace")
            soup = BeautifulSoup(content, "html.parser")
            title_tag = soup.find("title")
            title = title_tag.get_text().strip() if title_tag else ""
        except Exception as e:
            title = ""
            soup = None

        record = {
            "url_path": url_path,
            "title": title,
            "page_type": page_type,
            "entity_id": entity_id,
            "html_file": str(rel),
            "source_file": "",
            "soup": soup
        }
        pages_data.append(record)
        page_by_url[url_path] = record

    # Insert pages into SQLite
    for p in pages_data:
        cur.execute("""
            INSERT INTO pages (url_path, title, page_type, entity_id, html_file, source_file)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (p["url_path"], p["title"], p["page_type"], p["entity_id"], p["html_file"], p["source_file"]))
        p["id"] = cur.lastrowid

    # 2. Extract and Validate All Links
    print("[*] Extracting and validating all hyperlinks across pages...")
    total_links = 0
    broken_links = 0
    internal_links = 0
    external_links = 0

    link_inserts = []

    for p in pages_data:
        soup = p["soup"]
        if not soup:
            continue

        source_page_id = p["id"]
        source_url = p["url_path"]

        anchors = soup.find_all("a", href=True)
        for a in anchors:
            raw_href = a["href"].strip()
            anchor_text = a.get_text().strip()
            if not raw_href or raw_href.startswith("#"):
                continue

            total_links += 1
            u = urlsplit(raw_href)

            if u.scheme in ["http", "https"]:
                # External link
                external_links += 1
                link_inserts.append((
                    source_page_id, source_url, raw_href, raw_href, None, u.fragment,
                    anchor_text[:250], "external", 0, None
                ))
            elif u.scheme in ["mailto", "tel"]:
                link_inserts.append((
                    source_page_id, source_url, raw_href, raw_href, None, None,
                    anchor_text[:250], "mail_or_tel", 0, None
                ))
            else:
                # Internal link
                internal_links += 1
                clean_path = unquote(u.path)
                if not clean_path.startswith("/"):
                    # Relative path resolution
                    clean_path = str(Path(source_url).parent / clean_path)
                if not clean_path.endswith("/") and not clean_path.endswith(".html") and not clean_path.endswith(".svg") and not clean_path.endswith(".png") and not clean_path.endswith(".json"):
                    clean_path += "/"

                target_page = page_by_url.get(clean_path)
                target_page_id = target_page["id"] if target_page else None

                # Check if target file exists on disk (stripping /future/ prefix if present)
                disk_relative = clean_path.replace("/future/", "", 1) if clean_path.startswith("/future/") else clean_path.lstrip("/")
                target_disk_path = dist_dir / disk_relative
                is_broken = 0
                error_reason = None

                if not target_disk_path.exists():
                    if not (dist_dir / (disk_relative + "index.html")).exists():
                        is_broken = 1
                        error_reason = "Page or file does not exist"
                        broken_links += 1

                link_inserts.append((
                    source_page_id, source_url, raw_href, clean_path, target_page_id,
                    u.fragment, anchor_text[:250], "internal_page", is_broken, error_reason
                ))

    # Bulk insert links
    cur.executemany("""
        INSERT INTO links (
            source_page_id, source_url, raw_href, target_url, target_page_id,
            target_fragment, anchor_text, link_type, is_broken, error_reason
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, link_inserts)

    # 3. Calculate Page In-Degree & Out-Degree & Orphan status
    print("[*] Computing connectivity metrics (in-degree, out-degree, orphans)...")
    cur.execute("""
        UPDATE pages
        SET out_degree = (
            SELECT COUNT(*) FROM links WHERE links.source_page_id = pages.id AND link_type = 'internal_page'
        ),
        in_degree = (
            SELECT COUNT(*) FROM links WHERE links.target_page_id = pages.id AND link_type = 'internal_page'
        )
    """)

    cur.execute("""
        UPDATE pages
        SET is_orphan = 1
        WHERE in_degree = 0 AND url_path NOT IN ('/', '/404.html')
    """)

    # 4. Populate Entities & Entity Connections from src/content/
    print("[*] Importing structured entities & knowledge connections...")
    entity_count = 0
    connection_count = 0

    # Sectors
    sectors_dir = content_dir / "sectors"
    if sectors_dir.exists():
        for f in sectors_dir.glob("*.json"):
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
                eid = data.get("id", f.stem)
                cur.execute("INSERT OR REPLACE INTO entities (id, entity_type, name, sector, metadata_json) VALUES (?, ?, ?, ?, ?)",
                            (eid, "sector", data.get("title", eid), eid, json.dumps(data)))
                entity_count += 1
            except Exception:
                pass

    # Companies
    companies_dir = content_dir / "companies"
    if companies_dir.exists():
        for f in companies_dir.glob("*.json"):
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
                eid = data.get("id", f.stem)
                cur.execute("INSERT OR REPLACE INTO entities (id, entity_type, name, sector, metadata_json) VALUES (?, ?, ?, ?, ?)",
                            (eid, "company", data.get("name", eid), data.get("sector", ""), json.dumps(data)))
                entity_count += 1
            except Exception:
                pass

    # Technologies
    tech_dir = content_dir / "technologies"
    if tech_dir.exists():
        for f in tech_dir.glob("*.json"):
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
                eid = data.get("id", f.stem)
                sector = data.get("sector", "")
                cur.execute("INSERT OR REPLACE INTO entities (id, entity_type, name, sector, metadata_json) VALUES (?, ?, ?, ?, ?)",
                            (eid, "technology", data.get("title", eid), sector, json.dumps(data)))
                entity_count += 1

                # Connections
                if sector:
                    cur.execute("""
                        INSERT INTO entity_connections (from_entity_id, from_entity_type, to_entity_id, to_entity_type, connection_type, source)
                        VALUES (?, 'technology', ?, 'sector', 'belongs_to_sector', 'frontmatter')
                    """, (eid, sector))
                    connection_count += 1

                for cid in data.get("companies", []):
                    cur.execute("""
                        INSERT INTO entity_connections (from_entity_id, from_entity_type, to_entity_id, to_entity_type, connection_type, source)
                        VALUES (?, 'technology', ?, 'company', 'linked_company', 'frontmatter')
                    """, (eid, cid))
                    connection_count += 1

            except Exception:
                pass

    # Decks
    decks_dir = content_dir / "decks"
    if decks_dir.exists():
        for f in decks_dir.glob("*.json"):
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
                eid = data.get("id", f.stem)
                cur.execute("INSERT OR REPLACE INTO entities (id, entity_type, name, sector, metadata_json) VALUES (?, ?, ?, ?, ?)",
                            (eid, "deck", data.get("title", eid), data.get("sector", ""), json.dumps(data)))
                entity_count += 1

                for tid in data.get("technologies", []):
                    cur.execute("""
                        INSERT INTO entity_connections (from_entity_id, from_entity_type, to_entity_id, to_entity_type, connection_type, source)
                        VALUES (?, 'deck', ?, 'technology', 'includes_technology', 'manifest')
                    """, (eid, tid))
                    connection_count += 1
            except Exception:
                pass

    # Record summary metrics
    cur.execute("SELECT COUNT(*) FROM pages WHERE is_orphan = 1")
    orphan_count = cur.fetchone()[0]

    summary = [
        ("total_pages", str(len(pages_data))),
        ("total_links", str(total_links)),
        ("internal_links", str(internal_links)),
        ("external_links", str(external_links)),
        ("broken_internal_links", str(broken_links)),
        ("orphan_pages", str(orphan_count)),
        ("total_entities", str(entity_count)),
        ("entity_connections", str(connection_count)),
        ("source_commit", "070a5da211c921ed23e6a695e698753a153a229a")
    ]
    cur.executemany("INSERT OR REPLACE INTO graph_summary (metric, value) VALUES (?, ?)", summary)

    conn.commit()
    conn.close()

    print("\n==========================================")
    print(" SITE GRAPH & LINK MAP DATABASE COMPLETE ")
    print("==========================================")
    print(f" Database file:        {db_path}")
    print(f" Pages Mapped:         {len(pages_data):,}")
    print(f" Total Links Indexed:  {total_links:,}")
    print(f" Internal Links:       {internal_links:,}")
    print(f" External Links:       {external_links:,}")
    print(f" Broken Links:         {broken_links:,}")
    print(f" Orphan Pages:         {orphan_count:,}")
    print(f" Structured Entities:  {entity_count:,}")
    print(f" Entity Connections:   {connection_count:,}")
    print("==========================================\n")

if __name__ == "__main__":
    main()
