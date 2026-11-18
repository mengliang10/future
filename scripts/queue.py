#!/usr/bin/env python3
"""
CLI tool to manage the Ingestion & Queue Database (data/ingest_queue.db).
Ingests and queues new research, signals, proposed connections, and link recommendations.

Commands:
  status                     - Show summary of queued items, connections, and links
  list                       - List queued research items
  add                        - Add a new raw note or article to the queue
  connect                    - Propose a new entity-to-entity relationship
  link                       - Propose a new internal page link
  approve <item_id>          - Approve a queued item for integration
  reject <item_id>           - Mark an item as rejected
"""

import sys
import argparse
import sqlite3
import json
from pathlib import Path

def get_db():
    base_dir = Path(__file__).resolve().parent.parent
    db_path = base_dir / "data" / "ingest_queue.db"
    if not db_path.exists():
        print(f"[*] Initializing ingest_queue.db first...")
        from importlib.util import spec_from_file_location, module_from_spec
        init_script = base_dir / "scripts" / "init-ingest-queue.py"
        spec = spec_from_file_location("init_queue", init_script)
        mod = module_from_spec(spec)
        spec.loader.exec_module(mod)
        mod.init_queue_db()

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def show_status(conn):
    cur = conn.cursor()
    cur.execute("SELECT status, COUNT(*) FROM inbox_items GROUP BY status")
    inbox_counts = dict(cur.fetchall())

    cur.execute("SELECT status, COUNT(*) FROM proposed_connections GROUP BY status")
    conn_counts = dict(cur.fetchall())

    cur.execute("SELECT status, COUNT(*) FROM proposed_links GROUP BY status")
    link_counts = dict(cur.fetchall())

    cur.execute("SELECT COUNT(*) FROM sources_catalog")
    sources_count = cur.fetchone()[0]

    print("\n--- The Future Tomorrow: Ingest & Queue Status ---")
    print(f" Monitored Sources Catalog:  {sources_count} sources")
    print("\n Inbox Items:")
    if not inbox_counts:
        print("   (Empty queue)")
    else:
        for st, cnt in inbox_counts.items():
            print(f"   • {st:<20}: {cnt}")

    print("\n Proposed Entity Connections:")
    if not conn_counts:
        print("   (No proposed connections)")
    else:
        for st, cnt in conn_counts.items():
            print(f"   • {st:<20}: {cnt}")

    print("\n Proposed Page Links:")
    if not link_counts:
        print("   (No proposed links)")
    else:
        for st, cnt in link_counts.items():
            print(f"   • {st:<20}: {cnt}")
    print("--------------------------------------------------\n")

def list_items(conn, status_filter=None):
    cur = conn.cursor()
    if status_filter:
        cur.execute("SELECT * FROM inbox_items WHERE status = ? ORDER BY priority ASC, created_at DESC", (status_filter,))
    else:
        cur.execute("SELECT * FROM inbox_items ORDER BY priority ASC, created_at DESC LIMIT 50")
    rows = cur.fetchall()

    print(f"\n--- Ingest Queue ({len(rows)} items) ---")
    if not rows:
        print("  (Queue is currently empty)")
    for r in rows:
        print(f"  [ID #{r['id']}] [{r['status'].upper()}] (P{r['priority']}) {r['title']}")
        if r['source_url']:
            print(f"         Source: {r['source_url']}")
        if r['suggested_technologies']:
            print(f"         Techs:  {r['suggested_technologies']}")
        if r['suggested_companies']:
            print(f"         Stocks: {r['suggested_companies']}")
        if r['raw_content']:
            preview = (r['raw_content'][:100] + '...') if len(r['raw_content']) > 100 else r['raw_content']
            print(f"         Note:   {preview}")
        print()
    print("-----------------------------------------\n")

def add_item(conn, args):
    cur = conn.cursor()
    techs_json = json.dumps([t.strip() for t in args.techs.split(",") if t.strip()]) if args.techs else "[]"
    companies_json = json.dumps([c.strip().lower() for c in args.companies.split(",") if c.strip()]) if args.companies else "[]"

    cur.execute("""
        INSERT INTO inbox_items (title, raw_content, source_url, source_type, suggested_sector, suggested_technologies, suggested_companies, priority, curator_notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (args.title, args.content, args.url, args.type, args.sector, techs_json, companies_json, args.priority, args.notes))

    new_id = cur.lastrowid
    cur.execute("INSERT INTO queue_logs (action, target_type, target_id, details) VALUES (?, ?, ?, ?)",
                ("create", "inbox_item", new_id, f"Added: {args.title}"))

    conn.commit()
    print(f"\n[✓] Successfully added queue item #{new_id}: '{args.title}'\n")

def propose_connection(conn, args):
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO proposed_connections (inbox_item_id, from_entity_type, from_entity_id, to_entity_type, to_entity_id, relationship, confidence_score, evidence_text)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (args.item_id, args.from_type, args.from_id, args.to_type, args.to_id, args.rel, args.confidence, args.evidence))

    new_id = cur.lastrowid
    cur.execute("INSERT INTO queue_logs (action, target_type, target_id, details) VALUES (?, ?, ?, ?)",
                ("propose_connection", "connection", new_id, f"{args.from_id} -> {args.rel} -> {args.to_id}"))

    conn.commit()
    print(f"\n[✓] Prosposed connection #{new_id}: [{args.from_id}] --({args.rel})--> [{args.to_id}]\n")

def propose_link(conn, args):
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO proposed_links (inbox_item_id, source_url_path, target_url_path, anchor_text, context_text, placement_hint)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (args.item_id, args.source, args.target, args.anchor, args.context, args.hint))

    new_id = cur.lastrowid
    cur.execute("INSERT INTO queue_logs (action, target_type, target_id, details) VALUES (?, ?, ?, ?)",
                ("propose_link", "link", new_id, f"{args.source} -> {args.target} ('{args.anchor}')"))

    conn.commit()
    print(f"\n[✓] Proposed link #{new_id}: '{args.source}' -> '{args.target}' (Anchor: '{args.anchor}')\n")

def set_item_status(conn, item_id, new_status):
    cur = conn.cursor()
    cur.execute("UPDATE inbox_items SET status = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?", (new_status, item_id))
    if cur.rowcount == 0:
        print(f"[!] Item #{item_id} not found.")
    else:
        cur.execute("INSERT INTO queue_logs (action, target_type, target_id, details) VALUES (?, ?, ?, ?)",
                    (f"set_status_{new_status}", "inbox_item", item_id, f"Updated status to {new_status}"))
        conn.commit()
        print(f"\n[✓] Item #{item_id} marked as {new_status}.\n")

def main():
    parser = argparse.ArgumentParser(description="Manage Ingestion & Research Queue for The Future Tomorrow")
    subparsers = parser.add_subparsers(dest="command", help="Subcommand to run")

    # status
    subparsers.add_parser("status", help="Show queue summary")

    # list
    list_p = subparsers.add_parser("list", help="List queued items")
    list_p.add_argument("--status", choices=["queued", "reviewing", "approved", "merged_into_site", "rejected"], help="Filter by status")

    # add
    add_p = subparsers.add_parser("add", help="Add a new research note or URL")
    add_p.add_argument("title", help="Headline or title")
    add_p.add_argument("--url", default="", help="Source URL")
    add_p.add_argument("--content", default="", help="Note content or summary")
    add_p.add_argument("--type", default="web_article", choices=["web_article", "earnings_call", "academic_paper", "note", "tweet_x", "report"])
    add_p.add_argument("--sector", default="", help="Sector alias (ai, semiconductors, biotech, etc.)")
    add_p.add_argument("--techs", default="", help="Comma-separated technology IDs")
    add_p.add_argument("--companies", default="", help="Comma-separated company ticker IDs")
    add_p.add_argument("--priority", type=int, default=3, choices=[1, 2, 3, 4, 5], help="1=urgent to 5=low")
    add_p.add_argument("--notes", default="", help="Internal curator remarks")

    # connect
    conn_p = subparsers.add_parser("connect", help="Propose a relationship between entities")
    conn_p.add_argument("--from-id", required=True, help="Origin entity ID (e.g. nvda, quantum-computing)")
    conn_p.add_argument("--from-type", default="technology", choices=["technology", "company", "sector"])
    conn_p.add_argument("--to-id", required=True, help="Target entity ID (e.g. tsm, artificial-intelligence)")
    conn_p.add_argument("--to-type", default="company", choices=["technology", "company", "sector"])
    conn_p.add_argument("--rel", required=True, help="Relationship (e.g. enables, supplies, competes_with, invested_in)")
    conn_p.add_argument("--evidence", default="", help="Evidence or citation")
    conn_p.add_argument("--confidence", type=float, default=0.85, help="Confidence score 0.0-1.0")
    conn_p.add_argument("--item-id", type=int, default=None, help="Originating inbox item ID")

    # link
    link_p = subparsers.add_parser("link", help="Propose a cross-page internal link")
    link_p.add_argument("--source", required=True, help="Source URL path (e.g. /tech/gpu-compute-cluster/)")
    link_p.add_argument("--target", required=True, help="Target URL path (e.g. /companies/nvda/)")
    link_p.add_argument("--anchor", required=True, help="Anchor text for link")
    link_p.add_argument("--context", default="", help="Surrounding sentence")
    link_p.add_argument("--hint", default="", help="Placement guidance")
    link_p.add_argument("--item-id", type=int, default=None, help="Originating inbox item ID")

    # approve / reject
    app_p = subparsers.add_parser("approve", help="Mark item as approved")
    app_p.add_argument("id", type=int, help="Inbox item ID")

    rej_p = subparsers.add_parser("reject", help="Mark item as rejected")
    rej_p.add_argument("id", type=int, help="Inbox item ID")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)

    conn = get_db()
    if args.command == "status":
        show_status(conn)
    elif args.command == "list":
        list_items(conn, args.status)
    elif args.command == "add":
        add_item(conn, args)
    elif args.command == "connect":
        propose_connection(conn, args)
    elif args.command == "link":
        propose_link(conn, args)
    elif args.command == "approve":
        set_item_status(conn, args.id, "approved")
    elif args.command == "reject":
        set_item_status(conn, args.id, "rejected")

    conn.close()

if __name__ == "__main__":
    main()
