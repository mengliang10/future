#!/usr/bin/env python3
"""Adds editorial supplier/company records and links them to technology records.

Run from the project root:  python3 scripts/add-supplier-companies.py

Each tuple is:
  (id, title, symbol, exchange, private, sector, sourceCategory, summary,
   thesis, [exposure], [watch], businessMeaning, investmentLens, [technologyIds])
Existing company files and existing links are left untouched.
"""
import hashlib
import html
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
COMPANY_DIR = ROOT / "src/content/companies"
SOURCE_DIR = ROOT / "public/source/_stocks"
TECH_DIR = ROOT / "src/content/technologies"
DATA_DIR = ROOT / "scripts/company-batches"
REVIEWED = "2026-11-19"
NOTE = (
    "Editorial brief compiled 19 November 2026 from company disclosures, agency "
    "publications and press reporting. Figures are as reported by those sources "
    "and have not been independently audited; no live market data is used."
)

COMPANIES = [
    (
        "ajinomoto.jp", "Ajinomoto", "2802.T", "TSE", False, "materials",
        "Advanced Materials",
        "Japanese food and fine-chemicals group whose ABF build-up film is a critical insulator in high-end IC substrates.",
        "Ajinomoto is best known for seasonings, but its electronic-materials business supplies Ajinomoto Build-up Film, the dielectric used in flip-chip ball-grid-array substrates for CPUs, GPUs and networking chips. Very few materials combine fine-pitch fill, low thermal expansion and reliability at the layer counts now demanded, which has kept the film a reference choice as substrate bodies grow larger and denser. Substrate capacity additions at Ibiden, Unimicron, Samsung Electro-Mechanics and their peers convert directly into ABF volume.",
        ["ABF build-up film for FC-BGA substrates",
         "Fine chemicals and amino-acid derivatives",
         "Seasonings and frozen foods as a cash-generative base"],
        ["ABF film capacity additions and qualification",
         "Substrate-makers' capex plans",
         "Any qualified alternative dielectric"],
        "Substrate supply gates advanced processor shipments; qualifying a second dielectric source takes years, so buyers treat film availability as a strategic risk.",
        "A high-margin electronic-materials niche inside a food company; the electronic-materials segment margin matters more than group revenue.",
        ["advanced-packaging", "semiconductor-advanced-packaging", "cowos-advanced-packaging", "hbm4-memory"],
    ),
    (
        "dongjin-semichem.kr", "Dongjin Semichem", "005290.KS", "KRX", False, "materials",
        "Semiconductor Materials",
        "Korean maker of photoresists, wet chemicals and deposition precursors for memory and logic fabs.",
        "Dongjin Semichem supplies photoresists, etchants and precursors to Korean memory fabs and has been localising materials historically imported from Japan. Its portfolio spans i-line and KrF resists, spin-on dielectrics and high-purity precursors, placing it close to the DRAM and 3D NAND roadmaps that drive Korean capex. Domestic fab expansion and supply-chain localisation are the main demand levers.",
        ["Photoresists and ancillary lithography chemicals",
         "Precursors for thin-film deposition",
         "Wet etch and cleaning chemistries"],
        ["Qualification at leading-edge DRAM and NAND nodes",
         "Korean materials localisation policy",
         "Raw-material import dependence"],
        "Materials qualification is sticky: once a chemistry is qualified at a node, switching costs are high and supply continuity matters more than unit price.",
        "Levered to Korean memory capex; margin depends on mix shifting from commodity wet chemicals to advanced resists.",
        ["euv-lithography-135nm", "dram-and-hbm-demand", "3d-nand-flash"],
    ),
    (
        "hns-hitech.kr", "HNS HiTech", "036640.KQ", "KRX", False, "materials",
        "Semiconductor Materials",
        "Korean precursor specialist supplying high-purity organometallics to memory fabs.",
        "HNS HiTech produces organometallic precursors used in chemical vapour deposition and atomic layer deposition of electrodes and dielectrics, a segment where purity and batch consistency decide yield. Its customer base is concentrated in Korean memory manufacturing, so node transitions that add deposition steps raise its content per wafer. The company has also been expanding capacity for next-generation precursors.",
        ["Precursors for DRAM capacitor and electrode deposition",
         "ALD and CVD chemistries",
         "Specialty industrial chemicals"],
        ["Adoption of new high-k and electrode stacks",
         "Customer concentration",
         "Precursor plant utilisation"],
        "Every added deposition step is a recurring materials annuity; precursor suppliers earn most when a new stack is qualified.",
        "Small-cap with customer concentration; the thesis rests on content growth per wafer rather than wafer-volume growth.",
        ["dram-and-hbm-demand", "hbm4-memory", "3d-nand-flash"],
    ),
    (
        "samsung-electro-mechanics.kr", "Samsung Electro-Mechanics", "009150.KS", "KRX", False,
        "information-technology", "Semiconductors",
        "Korean components maker supplying FC-BGA substrates, MLCCs and camera modules.",
        "Samsung Electro-Mechanics is one of the few companies able to produce large flip-chip ball-grid-array substrates for server CPUs and AI accelerators, alongside MLCCs and camera modules. It has been adding substrate capacity in Korea and Southeast Asia for AI-server demand, where layer counts and body sizes are rising faster than conventional PCB capacity can absorb. Substrate mix within the Components division is the swing factor for margins.",
        ["FC-BGA substrates for servers and accelerators",
         "MLCCs for handsets, servers and vehicles",
         "Camera modules and mobile package substrates"],
        ["Large-body substrate yields and capacity ramps",
         "AI-server customer wins",
         "MLCC pricing cycle"],
        "Large-body substrates are scarce; securing capacity early is cheaper than redesigning a package later.",
        "A components group where the substrate business carries the AI narrative; track capex and utilisation by division.",
        ["advanced-packaging", "semiconductor-advanced-packaging", "cowos-advanced-packaging", "hbm4-memory"],
    ),
    (
        "kinsus.tw", "Kinsus Interconnect Technology", "3189.TW", "TWSE", False,
        "information-technology", "Semiconductors",
        "Taiwanese IC-substrate maker focused on flip-chip and ABF substrates.",
        "Kinsus produces IC substrates for processors, networking and consumer chips and has been shifting capacity toward the larger, higher-layer ABF substrates needed for AI accelerators. It sits in the same Taiwanese substrate cluster as Unimicron and Nan Ya PCB, and buyers value it as a local second source. Utilisation and product mix, rather than headline capacity, drive profitability.",
        ["ABF and flip-chip substrates",
         "Package substrates for mobile and networking",
         "Printed circuit boards for modules"],
        ["AI-server substrate qualification",
         "Capacity additions and yields",
         "Substrate pricing through the cycle"],
        "A second source for advanced substrates is valuable even at a cost premium, because single-sourcing large bodies is risky.",
        "Cyclical substrate maker; the AI mix shift is the re-rating lever.",
        ["advanced-packaging", "semiconductor-advanced-packaging", "cowos-advanced-packaging"],
    ),
    (
        "unimicron.tw", "Unimicron Technology", "3037.TW", "TWSE", False,
        "information-technology", "Semiconductors",
        "Taiwan's largest IC-substrate and PCB maker, a core supplier of ABF substrates.",
        "Unimicron is the largest Taiwanese maker of IC substrates and printed circuit boards, supplying ABF substrates into CPU, GPU, networking and consumer packages. Its scale makes it the default second source when a platform ramps, and it has been converting capacity toward thicker, larger AI-server substrates. The business remains cyclical, with profitability tracking utilisation and the substrate-to-PCB mix.",
        ["ABF substrates for processors and accelerators",
         "PCB and module boards",
         "Carrier and package substrates"],
        ["AI substrate capacity conversion",
         "Utilisation through the handset and PC cycle",
         "Customer concentration among fabless vendors"],
        "When a platform ramps, substrate capacity is booked months ahead; Unimicron's scale makes it a scheduling buffer for the industry.",
        "A volume cyclical with an AI mix upgrade; watch capex conversion and gross-margin spread between substrates and PCB.",
        ["advanced-packaging", "semiconductor-advanced-packaging", "taiwan-cowos-packaging", "cowos-advanced-packaging"],
    ),
    (
        "ats.at", "AT&S", "ATS.VI", "Vienna", False,
        "information-technology", "Semiconductors",
        "Austrian PCB and IC-substrate maker building capacity for AI-server substrates.",
        "AT&S moved from specialty printed circuit boards into high-end IC substrates, with plants in Austria, India, Malaysia and China. Its Malaysian substrate site was built to serve AI and data-centre customers that want capacity outside Taiwan and Korea. The company carries heavy depreciation from that build-out, so the return depends on how quickly large-body substrate volumes fill the lines.",
        ["IC substrates for processors and accelerators",
         "High-frequency PCBs for aerospace, medical and industrial",
         "Substrate capacity in Malaysia and Southeast Asia"],
        ["Ramp and yield at the Malaysian substrate plant",
         "European and US customer qualification",
         "Debt and depreciation from the build-out"],
        "Geographic diversification of substrate supply is now a procurement requirement, not a nice-to-have.",
        "A capital-intensive turnaround story; watch utilisation of new substrate lines against depreciation.",
        ["advanced-packaging", "semiconductor-advanced-packaging", "cowos-advanced-packaging"],
    ),
    (
        "schott.de", "SCHOTT", "SCHOTT.DE", "PRIVATE", True, "materials",
        "Advanced Materials",
        "German specialty-glass maker supplying glass wafers, through-glass vias and pharma packaging.",
        "SCHOTT makes specialty glass for displays, optics, pharmaceutical containers and semiconductor applications, including glass wafers and substrates used in MEMS, imaging and advanced packaging. Glass is attractive as a package core and carrier because it is stiff, flat and dimensionally stable at panel scale, and SCHOTT's glass-forming know-how is a barrier to entry. The company is owned by the Carl Zeiss Foundation and reports privately.",
        ["Glass wafers and carriers for semiconductor processing",
         "Specialty glass for optics and displays",
         "Pharmaceutical packaging and tubing"],
        ["Glass-core substrate adoption in advanced packaging",
         "Panel-level processing demand",
         "Energy costs at European glass plants"],
        "Glass carriers and cores solve warpage at large panel sizes, but handling and via formation must be proven in volume.",
        "Not directly investable; use its capacity and product announcements as a read on glass-substrate adoption.",
        ["advanced-packaging", "semiconductor-advanced-packaging"],
    ),
    (
        "sk-absolics.kr", "SK Absolics", "ABSOLICS.KR", "PRIVATE", True,
        "information-technology", "Semiconductors",
        "SKC subsidiary commercialising glass-core substrates for advanced packaging.",
        "SK Absolics, a subsidiary of SKC, is building glass-core substrate capacity in Georgia to serve US chip packaging demand. Glass cores promise better flatness and finer routing than organic substrates for large AI packages, and Absolics has been the most visible commercial-scale proponent. The programme is still pre-volume, so qualification and yield are the open questions.",
        ["Glass-core substrates for AI and data-centre packages",
         "Panel-level substrate processing",
         "SKC's broader film and materials portfolio"],
        ["Customer qualification of glass cores",
         "Yield and cost versus organic ABF substrates",
         "Ramp timing at the Georgia facility"],
        "Glass cores could relax the size limits of organic substrates, but only if panel handling reaches acceptable yields.",
        "Private and early-stage; SKC is the listed proxy for the same programme.",
        ["advanced-packaging", "semiconductor-advanced-packaging", "cowos-advanced-packaging"],
    ),
    (
        "agc.jp", "AGC", "5201.T", "TSE", False, "materials",
        "Advanced Materials",
        "Japanese glass and chemicals group that also supplies EUV mask blanks and display glass.",
        "AGC makes architectural and automotive glass, display glass, fluorochemicals and electronic materials, including mask blanks used in EUV lithography. Its glass and chemical process control gives it a position in several constrained supply chains at once, from display substrates to semiconductor photomasks. The electronics and chemicals segments carry much higher margins than architectural glass.",
        ["EUV mask blanks",
         "Glass substrates for displays",
         "Fluorochemicals and specialty chemicals"],
        ["EUV mask-blank demand as leading-edge capacity grows",
         "Display glass pricing",
         "Fluorochemical regulation"],
        "Mask blanks are a quiet bottleneck: every EUV mask starts with one, and qualification is slow.",
        "A diversified materials group where electronic materials provide the margin uplift; watch segment mix.",
        ["euv-lithography-135nm", "oled-display-panel", "advanced-packaging"],
    ),
    (
        "ibiden.jp", "Ibiden", "4062.T", "TSE", False,
        "information-technology", "Semiconductors",
        "Japanese substrate maker and long-standing lead supplier of FC-BGA substrates for high-end processors.",
        "Ibiden is one of the largest suppliers of flip-chip ball-grid-array substrates and has been a lead partner for Intel and other processor vendors for years. It is investing in larger, higher-layer substrates for AI accelerators, where package size and power delivery push organic substrate technology to its limits. Substrate capacity, not demand, has been the binding constraint in recent cycles.",
        ["FC-BGA substrates for CPUs, GPUs and accelerators",
         "Ceramic and other electronic components",
         "Substrate capacity in Japan and overseas"],
        ["AI substrate capacity additions",
         "Customer concentration and programme ramps",
         "Capital intensity and depreciation"],
        "The largest packages in the industry are qualified on a handful of substrate lines; Ibiden's capacity is a strategic asset.",
        "A high-quality franchise with cyclical orders and heavy capex; the AI substrate ramp is the key variable.",
        ["advanced-packaging", "semiconductor-advanced-packaging", "cowos-advanced-packaging", "chiplet-based-architectures"],
    ),
    (
        "shinko.jp", "Shinko Electric Industries", "SHINKO.JP", "PRIVATE", True,
        "information-technology", "Semiconductors",
        "Japanese IC-package and substrate maker taken private in a JIC-led buyout.",
        "Shinko Electric Industries supplies flip-chip substrates, lead frames and package parts, and has long been a key substrate partner for advanced processors. A JIC-led consortium with Fujitsu took the company private, removing it from the Tokyo exchange while leaving its capacity in place. Its technology roadmap centres on finer routing and larger bodies for AI and high-performance computing.",
        ["FC-BGA and flip-chip substrates",
         "Lead frames and package components",
         "Advanced package development"],
        ["Post-buyout investment and capacity plans",
         "AI substrate qualification",
         "Customer relationships under private ownership"],
        "A private substrate supplier can invest on a longer horizon, but customers lose the transparency of a listed peer.",
        "No longer directly investable after the take-private; relevant as a capacity and technology reference.",
        ["advanced-packaging", "semiconductor-advanced-packaging", "chiplet-based-architectures"],
    ),
    (
        "kyocera.jp", "Kyocera", "6971.T", "TSE", False,
        "information-technology", "Semiconductors",
        "Japanese ceramics group supplying packages, substrates and electronic components.",
        "Kyocera builds ceramic packages, organic substrates, capacitors and industrial ceramics, and its package business benefits when chips need hermetic or high-reliability housings. It also sells cutting tools, solar modules and document equipment, so the semiconductor segment is diluted by slower businesses. Advanced ceramic packaging is a genuine differentiator in power, RF and automotive applications.",
        ["Ceramic packages for power, RF and automotive chips",
         "Organic substrates and electronic components",
         "Industrial ceramics and cutting tools"],
        ["Automotive and power-semiconductor packaging demand",
         "Segment profitability outside semiconductors",
         "Capacity investment in ceramic packaging"],
        "Ceramic packaging is chosen where organic substrates cannot survive heat or moisture; the trade-off is cost and size.",
        "A conglomerate with a quality packaging niche; the investment case depends on portfolio focus.",
        ["silicon-carbide", "gan-power-semiconductors", "advanced-packaging"],
    ),
    (
        "ngk-insulators.jp", "NGK Insulators", "5333.T", "TSE", False, "materials",
        "Advanced Materials",
        "Japanese ceramics maker supplying battery, semiconductor and environmental components.",
        "NGK Insulators produces ceramic products for automotive emissions control, power transmission, battery components and semiconductor manufacturing equipment. Its ceramics appear in battery separators and in plasma-resistant parts for etch tools, tying it to both electrification and fab capex. The company is also developing sodium-sulfur and solid-state battery materials.",
        ["Ceramic battery components and separators",
         "Plasma-resistant ceramic parts for etch equipment",
         "Environmental and power-grid ceramics"],
        ["Solid-state and sodium-based battery programmes",
         "Semiconductor equipment demand",
         "Automotive ceramics cycle"],
        "Ceramic parts inside etch chambers are consumables with demanding qualification; supply is concentrated.",
        "A steady industrial with optionality in battery ceramics; watch the semiconductor and battery segments.",
        ["solid-state-battery", "sodium-ion-battery-technology", "3d-nand-flash"],
    ),
    (
        "nan-ya-pcb.tw", "Nan Ya PCB", "8046.TW", "TWSE", False,
        "information-technology", "Semiconductors",
        "Taiwanese PCB and IC-substrate maker within the Nan Ya plastics group.",
        "Nan Ya PCB produces printed circuit boards and IC substrates, with a focus on flip-chip and ball-grid-array packages for processors and networking. It is part of the Formosa Plastics group, which gives it materials integration and balance-sheet depth. Its capacity is a meaningful part of the Taiwanese substrate supply that AI customers rely on.",
        ["IC substrates for processors and networking",
         "Multilayer and high-density PCBs",
         "Group materials integration"],
        ["AI substrate capacity conversion",
         "PCB pricing cycle",
         "Group capital allocation"],
        "Group backing lets Nan Ya add substrate capacity through a downturn, which matters when customers want supply assurance.",
        "A cyclical substrate and PCB producer; track utilisation and the substrate share of revenue.",
        ["advanced-packaging", "semiconductor-advanced-packaging", "cowos-advanced-packaging"],
    ),
    # >>> MORE
]


def build_markdown(thesis, exposure, watch):
    parts = ["## Investment Thesis", "", thesis, "", "## Technology Exposure", ""]
    parts += [f"- {item}" for item in exposure]
    parts += ["", "## What To Watch", ""]
    parts += [f"- {item}" for item in watch]
    parts += ["", "## Record Notes", "", NOTE]
    return "\n".join(parts) + "\n"


def build_html(thesis, exposure, watch):
    esc = lambda value: html.escape(value, quote=False)
    out = ["<h2>Investment Thesis</h2>", f"<p>{esc(thesis)}</p>", "<h2>Technology Exposure</h2>", "<ul>"]
    out += [f"<li>{esc(item)}</li>" for item in exposure]
    out += ["</ul>", "<h2>What To Watch</h2>", "<ul>"]
    out += [f"<li>{esc(item)}</li>" for item in watch]
    out += ["</ul>", "<h2>Record Notes</h2>", f"<p>{esc(NOTE)}</p>"]
    return "\n".join(out) + "\n"


def load_batches():
    rows = []
    if not DATA_DIR.exists():
        return rows
    import importlib.util

    for path in sorted(DATA_DIR.glob("*.py")):
        spec = importlib.util.spec_from_file_location(f"batch_{path.stem}", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        rows.extend(module.COMPANIES)
    return rows


def main():
    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    created, skipped, links, missing_tech = [], [], 0, set()
    for row in COMPANIES + load_batches():
        (cid, title, symbol, exchange, private, sector, category, summary,
         thesis, exposure, watch, business, investor, techs) = row
        target = COMPANY_DIR / f"{cid}.json"
        markdown = build_markdown(thesis, exposure, watch)
        if not target.exists():
            record = {
                "id": cid,
                "title": title,
                "summary": summary,
                "sector": sector,
                "sourceCategory": category,
                "sourcePath": f"_stocks/{cid}.md",
                "sourceHash": hashlib.sha256(markdown.encode("utf-8")).hexdigest(),
                "bodyHtml": build_html(thesis, exposure, watch),
                "bodyMarkdown": markdown.rstrip("\n"),
                "sourceMeta": {
                    "layout": "stock",
                    "name": title,
                    "symbol": symbol,
                    "exchange": exchange,
                    "categories": [category],
                    "node_count": 0,
                    "bottleneck_count": 0,
                },
                "evidenceStatus": "editorial-brief",
                "reviewedAt": REVIEWED,
                "symbol": symbol,
                "exchange": exchange,
                "private": private,
                "businessMeaning": business,
                "investmentLens": investor,
            }
            target.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
            (SOURCE_DIR / f"{cid}.md").write_text(markdown, encoding="utf-8")
            created.append(cid)
        else:
            skipped.append(cid)
        for tid in techs:
            path = TECH_DIR / f"{tid}.json"
            if not path.exists():
                missing_tech.add(tid)
                continue
            data = json.loads(path.read_text(encoding="utf-8"))
            ids = data.setdefault("companies", [])
            if cid in ids:
                continue
            ids.append(cid)
            path.write_text(json.dumps(data, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
            links += 1
    print(f"created={len(created)} skipped={len(skipped)} tech-links={links}")
    if missing_tech:
        print("missing technology ids:", ", ".join(sorted(missing_tech)))


if __name__ == "__main__":
    main()
