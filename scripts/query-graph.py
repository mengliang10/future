#!/usr/bin/env python3
"""
CLI tool to query the Site Knowledge Graph & Link Map (data/site_graph.db).
Commands:
  summary          - Show overall graph metrics and health
  dead-links       - Check for any broken internal or anchor links
  orphans          - List pages with 0 inbound links
  backlinks <path> - List all pages linking to a specific page or entity
  outbound <path>  - List all outbound links on a specific page
  entity <id>      - View entity details, connections, and deck placements
  top-hubs         - Display the top 20 most connected pages on the site
"""

import sys
import sqlite3
from pathlib import Path

def get_db():
    base_dir = Path(__file__).resolve().parent.parent
    db_path = base_dir / "data" / "site_graph.db"
    if not db_path.exists():
        print(f"[!] site_graph.db not found at {db_path}. Run `python3 scripts/build-site-graph.py` first!")
        sys.exit(1)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def show_summary(conn):
    cur = conn.cursor()
    cur.execute("SELECT metric, value FROM graph_summary")
    metrics = dict(cur.fetchall())

    print("\n--- The Future Tomorrow: Site Graph Summary ---")
    for k, v in metrics.items():
        print(f"  {k:<25}: {v}")
    print("------------------------------------------------\n")

def show_dead_links(conn):
    cur = conn.cursor()
    cur.execute("""
        SELECT source_url, raw_href, target_url, anchor_text, error_reason
        FROM links
        WHERE is_broken = 1
        ORDER BY source_url
    """)
    rows = cur.fetchall()
    if not rows:
        print("\n[✓] Excellent! Zero broken internal links found across all pages.\n")
        return

    print(f"\n[!] Found {len(rows)} broken links:")
    for r in rows:
        print(f"  Source:  {r['source_url']}")
        print(f"  Target:  {r['target_url']} ({r['raw_href']})")
        print(f"  Anchor:  '{r['anchor_text']}'")
        print(f"  Reason:  {r['error_reason']}\n")

def show_orphans(conn):
    cur = conn.cursor()
    cur.execute("SELECT url_path, title, page_type FROM pages WHERE is_orphan = 1 ORDER BY page_type, url_path")
    rows = cur.fetchall()
    if not rows:
        print("\n[✓] Zero orphan pages found! Every page is reachable from site navigation.\n")
        return

    print(f"\n[!] Found {len(rows)} orphan pages (0 inbound links):")
    for r in rows:
        print(f"  [{r['page_type']}] {r['url_path']} - {r['title']}")
    print()

def show_backlinks(conn, target_path):
    cur = conn.cursor()
    # Normalize path
    if not target_path.startswith("/"):
        target_path = "/" + target_path
    if not target_path.endswith("/") and not target_path.endswith(".html"):
        target_path += "/"

    cur.execute("""
        SELECT p.url_path as source_path, p.title as source_title, l.anchor_text, l.raw_href
        FROM links l
        JOIN pages p ON l.source_page_id = p.id
        WHERE l.target_url = ?
        ORDER BY p.url_path
    """, (target_path,))
    rows = cur.fetchall()

    print(f"\n--- Backlinks pointing to '{target_path}' ({len(rows)} inbound links) ---")
    if not rows:
        print("  (No inbound links found)")
    else:
        for r in rows[:40]:
            print(f"  • {r['source_path']:<45} [Anchor: '{r['anchor_text']}']")
        if len(rows) > 40:
            print(f"  ... and {len(rows) - 40} more.")
    print("----------------------------------------------------------------------\n")

def show_outbound(conn, source_path):
    cur = conn.cursor()
    if not source_path.startswith("/"):
        source_path = "/" + source_path
    if not source_path.endswith("/") and not source_path.endswith(".html"):
        source_path += "/"

    cur.execute("""
        SELECT target_url, raw_href, anchor_text, link_type, is_broken
        FROM links
        WHERE source_url = ?
        ORDER BY link_type, target_url
    """, (source_path,))
    rows = cur.fetchall()

    print(f"\n--- Outbound links on '{source_path}' ({len(rows)} total) ---")
    for r in rows:
        broken_flag = " [BROKEN!]" if r["is_broken"] else ""
        print(f"  [{r['link_type']}] -> {r['target_url'] or r['raw_href']}{broken_flag} ('{r['anchor_text']}')")
    print("-------------------------------------------------------------------\n")

def show_entity(conn, entity_id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM entities WHERE id = ?", (entity_id,))
    ent = cur.fetchone()
    if not ent:
        # Search case-insensitive or partial
        cur.execute("SELECT * FROM entities WHERE id LIKE ? LIMIT 5", (f"%{entity_id}%",))
        candidates = cur.fetchall()
        if candidates:
            print(f"\n[!] Entity '{entity_id}' not found directly. Did you mean:")
            for c in candidates:
                print(f"    - {c['id']} ({c['name']} [{c['entity_type']}])")
        else:
            print(f"\n[!] Entity '{entity_id}' not found in entities table.\n")
        return

    print(f"\n=== Entity: {ent['name']} ({ent['id']}) ===")
    print(f" Type:    {ent['entity_type']}")
    print(f" Sector:  {ent['sector']}")

    # Connections
    cur.execute("""
        SELECT to_entity_id, to_entity_type, connection_type
        FROM entity_connections
        WHERE from_entity_id = ?
    """, (entity_id,))
    out_conn = cur.fetchall()
    if out_conn:
        print("\n Outgoing Connections:")
        for c in out_conn:
            print(f"   -> [{c['connection_type']}] {c['to_entity_id']} ({c['to_entity_type']})")

    cur.execute("""
        SELECT from_entity_id, from_entity_type, connection_type
        FROM entity_connections
        WHERE to_entity_id = ?
    """, (entity_id,))
    in_conn = cur.fetchall()
    if in_conn:
        print("\n Inbound Connections:")
        for c in in_conn:
            print(f"   <- [{c['connection_type']}] from {c['from_entity_id']} ({c['from_entity_type']})")

    print("============================================\n")

def show_top_hubs(conn):
    cur = conn.cursor()
    cur.execute("""
        SELECT url_path, title, page_type, in_degree, out_degree
        FROM pages
        ORDER BY in_degree DESC
        LIMIT 20
    """)
    rows = cur.fetchall()
    print("\n--- Top 20 Most Linked-To Pages (Hubs) ---")
    print(f" {'Inbound':<8} | {'Outbound':<8} | {'Type':<12} | URL")
    print("-" * 75)
    for r in rows:
        print(f" {r['in_degree']:<8} | {r['out_degree']:<8} | {r['page_type']:<12} | {r['url_path']}")
    print("-" * 75 + "\n")

def print_help():
    print("""
Usage: python3 scripts/query-graph.py <command> [args]

Available Commands:
  summary             - Overall graph statistics and health check
  dead-links          - Check for broken links and missing targets
  orphans             - List any orphaned pages with 0 inbound links
  backlinks <path>    - View pages linking to a specific path (e.g. /companies/nvda/)
  outbound <path>     - View all outbound links from a specific page
  entity <id>         - View knowledge connections for a technology or company (e.g. nvda)
  top-hubs            - View the top 20 most connected hub pages on the site
""")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
        sys.exit(0)

    cmd = sys.argv[1].lower()
    conn = get_db()

    if cmd == "summary":
        show_summary(conn)
    elif cmd in ["dead-links", "deadlinks", "broken"]:
        show_dead_links(conn)
    elif cmd in ["orphans", "orphan"]:
        show_orphans(conn)
    elif cmd == "backlinks":
        if len(sys.argv) < 3:
            print("Error: path required. Example: python3 scripts/query-graph.py backlinks /companies/nvda/")
            sys.exit(1)
        show_backlinks(conn, sys.argv[2])
    elif cmd == "outbound":
        if len(sys.argv) < 3:
            print("Error: path required. Example: python3 scripts/query-graph.py outbound /")
            sys.exit(1)
        show_outbound(conn, sys.argv[2])
    elif cmd == "entity":
        if len(sys.argv) < 3:
            print("Error: entity ID required. Example: python3 scripts/query-graph.py entity nvda")
            sys.exit(1)
        show_entity(conn, sys.argv[2])
    elif cmd in ["top-hubs", "hubs", "top"]:
        show_top_hubs(conn)
    else:
        print(f"Unknown command: {cmd}")
        print_help()

    conn.close()
