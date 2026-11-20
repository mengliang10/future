#!/usr/bin/env python3
"""Add secondary sector memberships for companies whose products already serve a
second future-tech sector. Run from the project root:

    python3 scripts/assign-sector-crosslistings.py

Safe to re-run: memberships are merged, never duplicated.
"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
COMPANIES = ROOT / "src/content/companies"

SECONDARY = {
    # Spatial computing / XR
    "aapl": ["spatial-computing"],
    "meta": ["spatial-computing"],
    "sony.jp": ["spatial-computing"],
    "qcom": ["spatial-computing", "autonomous"],
    "u": ["spatial-computing"],
    "rblx": ["spatial-computing"],
    "snap": ["spatial-computing"],
    "msft": ["spatial-computing", "ai-agents-software", "cybersecurity"],
    "googl": ["spatial-computing", "ai-agents-software", "autonomous"],
    "amzn": ["ai-agents-software", "cybersecurity"],
    "byd.hk": ["autonomous"],
    # Memory
    "hxscl": ["memory"],
    "samsung.kr": ["memory"],
    # AI infrastructure
    "nvda": ["ai-infrastructure", "robotics"],
    "avgo": ["ai-infrastructure"],
    "mrvl": ["ai-infrastructure"],
    "tsm": ["ai-infrastructure"],
    # Cybersecurity
    "crwd": [],
    # Autonomous
    "baidu.hk": ["autonomous"],
}

added = 0
for cid, sectors in SECONDARY.items():
    path = COMPANIES / f"{cid}.json"
    if not path.exists():
        print(f"missing record: {cid}")
        continue
    record = json.loads(path.read_text())
    current = record.get("sectors") or []
    merged = list(dict.fromkeys(current + [s for s in sectors if s != record["sector"]]))
    if merged != current:
        record["sectors"] = merged
        path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
        added += 1
        print(f"{cid}: {', '.join(merged)}")
print(f"updated={added}")
