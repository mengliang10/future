#!/usr/bin/env python3
"""Projects existing companies into the LLM Models & Generative AI sector.

Run from the project root:  python3 scripts/assign-llm-models-sector.py

Two kinds of change:
  * SECONDARY memberships - large platform owners already filed under another
    primary sector stay where they are but are also listed under llms-models.
  * REASSIGNED primary sectors - pure-play model labs that were filed under
    applied AI move their primary sector to llms-models.

Existing fields are preserved; the script is safe to re-run.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
COMPANY_DIR = ROOT / "src/content/companies"
SECTOR = "llms-models"

# Companies whose model business is one part of a wider group.
SECONDARY = {
    "googl": "Gemini models and DeepMind research",
    "msft": "Phi and MAI models plus Azure model serving",
    "amzn": "Nova models and Bedrock model hosting",
    "meta": "Llama open-weight family",
    "alibaba.hk": "Qwen open-weight family",
    "tencent.hk": "Hunyuan model family",
    "baidu.hk": "ERNIE model family",
    "nvda": "Nemotron models and inference hardware",
    "ibm": "Granite open-weight family",
    "samsung.kr": "Samsung Gauss models",
    "groq.pvt": "LPU inference for open models",
    "cere.pvt": "Wafer-scale training and inference systems",
}

# Pure-play model developers that belong in this sector by primary line of business.
REASSIGN = ["xai.pvt", "moonshot.pvt", "infl.pvt"]


def main():
    changed, reassigned, skipped = [], [], []
    for cid, reason in SECONDARY.items():
        path = COMPANY_DIR / f"{cid}.json"
        if not path.exists():
            skipped.append(f"{cid} (missing record)")
            continue
        record = json.loads(path.read_text(encoding="utf-8"))
        if record.get("sector") == SECTOR:
            skipped.append(f"{cid} (already primary)")
            continue
        extra = record.setdefault("sectors", [])
        if SECTOR in extra:
            skipped.append(f"{cid} (already listed)")
            continue
        extra.append(SECTOR)
        path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
        changed.append(f"{cid}: {reason}")

    for cid in REASSIGN:
        path = COMPANY_DIR / f"{cid}.json"
        record = json.loads(path.read_text(encoding="utf-8"))
        if record.get("sector") == SECTOR:
            skipped.append(f"{cid} (already primary)")
            continue
        record["sectors"] = [s for s in record.get("sectors", []) if s != SECTOR]
        if not record["sectors"]:
            record.pop("sectors")
        record["sector"] = SECTOR
        path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
        reassigned.append(cid)

    print(f"secondary={len(changed)} reassigned={len(reassigned)} skipped={len(skipped)}")
    for line in changed:
        print(f"  also listed: {line}")
    for cid in reassigned:
        print(f"  primary moved: {cid}")
    for line in skipped:
        print(f"  skipped: {line}")


if __name__ == "__main__":
    main()
