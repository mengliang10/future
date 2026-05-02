"""
fetch_stocks.py — runs daily via GitHub Actions
Fetches price data for all tracked stocks using yfinance,
writes to assets/data/stocks.json so the static site can read it.
"""

import yfinance as yf
import json
import os
from datetime import datetime, timezone

STOCKS = [
    # Semiconductors
    {"ticker": "NVDA",  "name": "NVIDIA Corporation",           "sector": "Semiconductors"},
    {"ticker": "AMD",   "name": "Advanced Micro Devices",        "sector": "Semiconductors"},
    {"ticker": "INTC",  "name": "Intel Corporation",             "sector": "Semiconductors"},
    {"ticker": "QCOM",  "name": "Qualcomm Inc.",                 "sector": "Semiconductors"},
    {"ticker": "AVGO",  "name": "Broadcom Inc.",                 "sector": "Semiconductors"},
    {"ticker": "MRVL",  "name": "Marvell Technology",            "sector": "Semiconductors"},
    {"ticker": "MU",    "name": "Micron Technology",             "sector": "Semiconductors"},
    {"ticker": "ARM",   "name": "Arm Holdings",                  "sector": "Semiconductors"},
    {"ticker": "TSM",   "name": "Taiwan Semiconductor Mfg",      "sector": "Semiconductors"},
    {"ticker": "ASML",  "name": "ASML Holding N.V.",             "sector": "Semiconductors"},
    {"ticker": "AMAT",  "name": "Applied Materials Inc.",        "sector": "Semiconductors"},
    {"ticker": "LRCX",  "name": "Lam Research Corp.",            "sector": "Semiconductors"},
    {"ticker": "KLAC",  "name": "KLA Corporation",               "sector": "Semiconductors"},
    {"ticker": "TXN",   "name": "Texas Instruments Inc.",        "sector": "Semiconductors"},
    {"ticker": "ADI",   "name": "Analog Devices Inc.",           "sector": "Semiconductors"},
    {"ticker": "MCHP",  "name": "Microchip Technology",          "sector": "Semiconductors"},
    {"ticker": "NXPI",  "name": "NXP Semiconductors",            "sector": "Semiconductors"},
    {"ticker": "ON",    "name": "ON Semiconductor",              "sector": "Semiconductors"},
    {"ticker": "MPWR",  "name": "Monolithic Power Systems",      "sector": "Semiconductors"},
    {"ticker": "SWKS",  "name": "Skyworks Solutions",            "sector": "Semiconductors"},
    {"ticker": "CRUS",  "name": "Cirrus Logic Inc.",             "sector": "Semiconductors"},
    {"ticker": "AMBA",  "name": "Ambarella Inc.",                "sector": "Semiconductors"},
    {"ticker": "TER",   "name": "Teradyne Inc.",                 "sector": "Semiconductors"},
    {"ticker": "ONTO",  "name": "Onto Innovation Inc.",          "sector": "Semiconductors"},
    {"ticker": "ACLS",  "name": "Axcelis Technologies",          "sector": "Semiconductors"},
    # AI & Cloud
    {"ticker": "MSFT",  "name": "Microsoft Corporation",         "sector": "AI & Cloud"},
    {"ticker": "GOOGL", "name": "Alphabet Inc.",                 "sector": "AI & Cloud"},
    {"ticker": "META",  "name": "Meta Platforms Inc.",           "sector": "AI & Cloud"},
    {"ticker": "AMZN",  "name": "Amazon.com Inc.",               "sector": "AI & Cloud"},
    {"ticker": "AAPL",  "name": "Apple Inc.",                    "sector": "AI & Cloud"},
    {"ticker": "IBM",   "name": "IBM Corporation",               "sector": "AI & Cloud"},
    {"ticker": "ORCL",  "name": "Oracle Corporation",            "sector": "AI & Cloud"},
    {"ticker": "PLTR",  "name": "Palantir Technologies",         "sector": "AI & Cloud"},
    {"ticker": "AI",    "name": "C3.ai Inc.",                    "sector": "AI & Cloud"},
    {"ticker": "PATH",  "name": "UiPath Inc.",                   "sector": "AI & Cloud"},
    {"ticker": "SOUN",  "name": "SoundHound AI Inc.",            "sector": "AI & Cloud"},
    {"ticker": "BBAI",  "name": "BigBear.ai Holdings",           "sector": "AI & Cloud"},
    {"ticker": "SNOW",  "name": "Snowflake Inc.",                "sector": "AI & Cloud"},
    # Software
    {"ticker": "DDOG",  "name": "Datadog Inc.",                  "sector": "Software"},
    {"ticker": "NET",   "name": "Cloudflare Inc.",               "sector": "Software"},
    {"ticker": "NOW",   "name": "ServiceNow Inc.",               "sector": "Software"},
    {"ticker": "CRM",   "name": "Salesforce Inc.",               "sector": "Software"},
    {"ticker": "ADBE",  "name": "Adobe Inc.",                    "sector": "Software"},
    {"ticker": "WDAY",  "name": "Workday Inc.",                  "sector": "Software"},
    {"ticker": "INTU",  "name": "Intuit Inc.",                   "sector": "Software"},
    {"ticker": "TEAM",  "name": "Atlassian Corporation",         "sector": "Software"},
    {"ticker": "HUBS",  "name": "HubSpot Inc.",                  "sector": "Software"},
    {"ticker": "MDB",   "name": "MongoDB Inc.",                  "sector": "Software"},
    {"ticker": "GTLB",  "name": "GitLab Inc.",                   "sector": "Software"},
    {"ticker": "ZS",    "name": "Zscaler Inc.",                  "sector": "Software"},
    {"ticker": "OKTA",  "name": "Okta Inc.",                     "sector": "Software"},
    {"ticker": "PANW",  "name": "Palo Alto Networks",            "sector": "Software"},
    {"ticker": "ESTC",  "name": "Elastic N.V.",                  "sector": "Software"},
    {"ticker": "BILL",  "name": "Bill Holdings Inc.",            "sector": "Software"},
    {"ticker": "VEEV",  "name": "Veeva Systems Inc.",            "sector": "Software"},
    {"ticker": "CRWD",  "name": "CrowdStrike Holdings",          "sector": "Software"},
    # Hardware
    {"ticker": "SMCI",  "name": "Super Micro Computer",          "sector": "Hardware"},
    {"ticker": "DELL",  "name": "Dell Technologies",             "sector": "Hardware"},
    {"ticker": "HPE",   "name": "Hewlett Packard Enterprise",    "sector": "Hardware"},
    {"ticker": "ANET",  "name": "Arista Networks Inc.",          "sector": "Hardware"},
    {"ticker": "CSCO",  "name": "Cisco Systems Inc.",            "sector": "Hardware"},
    {"ticker": "STX",   "name": "Seagate Technology",            "sector": "Hardware"},
    {"ticker": "WDC",   "name": "Western Digital Corp.",         "sector": "Hardware"},
    {"ticker": "PSTG",  "name": "Pure Storage Inc.",             "sector": "Hardware"},
    {"ticker": "NTAP",  "name": "NetApp Inc.",                   "sector": "Hardware"},
    {"ticker": "FFIV",  "name": "F5 Inc.",                       "sector": "Hardware"},
    # Quantum
    {"ticker": "IONQ",  "name": "IonQ Inc.",                     "sector": "Quantum"},
    {"ticker": "RGTI",  "name": "Rigetti Computing Inc.",        "sector": "Quantum"},
    {"ticker": "QBTS",  "name": "D-Wave Quantum Inc.",           "sector": "Quantum"},
    {"ticker": "ARQQ",  "name": "Arqit Quantum Inc.",            "sector": "Quantum"},
    {"ticker": "QUBT",  "name": "Quantum Computing Inc.",        "sector": "Quantum"},
    # Energy Tech
    {"ticker": "ENPH",  "name": "Enphase Energy Inc.",           "sector": "Energy Tech"},
    {"ticker": "SEDG",  "name": "SolarEdge Technologies",        "sector": "Energy Tech"},
    {"ticker": "FSLR",  "name": "First Solar Inc.",              "sector": "Energy Tech"},
    {"ticker": "BE",    "name": "Bloom Energy Corp.",            "sector": "Energy Tech"},
    {"ticker": "PLUG",  "name": "Plug Power Inc.",               "sector": "Energy Tech"},
    {"ticker": "NEE",   "name": "NextEra Energy Inc.",           "sector": "Energy Tech"},
    {"ticker": "GEV",   "name": "GE Vernova Inc.",               "sector": "Energy Tech"},
    {"ticker": "ETN",   "name": "Eaton Corporation",             "sector": "Energy Tech"},
    {"ticker": "PWR",   "name": "Quanta Services Inc.",          "sector": "Energy Tech"},
    {"ticker": "SHLS",  "name": "Shoals Technologies",           "sector": "Energy Tech"},
    # Robotics & Auto
    {"ticker": "TSLA",  "name": "Tesla Inc.",                    "sector": "Robotics & Auto"},
    {"ticker": "ISRG",  "name": "Intuitive Surgical Inc.",       "sector": "Robotics & Auto"},
    {"ticker": "ROK",   "name": "Rockwell Automation",           "sector": "Robotics & Auto"},
    {"ticker": "HON",   "name": "Honeywell International",       "sector": "Robotics & Auto"},
    {"ticker": "FARO",  "name": "FARO Technologies Inc.",        "sector": "Robotics & Auto"},
    {"ticker": "LAZR",  "name": "Luminar Technologies",          "sector": "Robotics & Auto"},
    {"ticker": "MVIS",  "name": "MicroVision Inc.",              "sector": "Robotics & Auto"},
    {"ticker": "OUST",  "name": "Ouster Inc.",                   "sector": "Robotics & Auto"},
    {"ticker": "AEVA",  "name": "Aeva Technologies Inc.",        "sector": "Robotics & Auto"},
    {"ticker": "INVZ",  "name": "Innoviz Technologies",          "sector": "Robotics & Auto"},
    # Space Tech
    {"ticker": "RKLB",  "name": "Rocket Lab USA Inc.",           "sector": "Space Tech"},
    {"ticker": "ASTS",  "name": "AST SpaceMobile Inc.",          "sector": "Space Tech"},
    {"ticker": "LUNR",  "name": "Intuitive Machines Inc.",       "sector": "Space Tech"},
    {"ticker": "SPIR",  "name": "Spire Global Inc.",             "sector": "Space Tech"},
    {"ticker": "MNTS",  "name": "Momentus Inc.",                 "sector": "Space Tech"},
    {"ticker": "SATL",  "name": "Satellogic Inc.",               "sector": "Space Tech"},
    {"ticker": "GSAT",  "name": "Globalstar Inc.",               "sector": "Space Tech"},
    {"ticker": "VSAT",  "name": "Viasat Inc.",                   "sector": "Space Tech"},
    {"ticker": "RDW",   "name": "Redwire Corporation",           "sector": "Space Tech"},
    {"ticker": "BKSY",  "name": "BlackSky Technology",           "sector": "Space Tech"},
]

def fetch_all():
    tickers_list = [s["ticker"] for s in STOCKS]
    meta = {s["ticker"]: s for s in STOCKS}

    # Download all at once (faster than one-by-one)
    raw = yf.download(tickers_list, period="2d", interval="1d",
                      auto_adjust=True, progress=False, group_by="ticker")

    results = []
    for stock in STOCKS:
        t = stock["ticker"]
        try:
            if len(tickers_list) == 1:
                closes = raw["Close"]
            else:
                closes = raw[t]["Close"]

            closes = closes.dropna()
            if len(closes) < 2:
                raise ValueError("insufficient data")

            prev  = float(closes.iloc[-2])
            last  = float(closes.iloc[-1])
            chg   = round(last - prev, 4)
            chg_p = round((chg / prev) * 100, 4)

            info = yf.Ticker(t).fast_info
            mktcap = getattr(info, "market_cap", None)
            vol    = getattr(info, "three_month_average_volume", None)

            results.append({
                "ticker":     t,
                "name":       stock["name"],
                "sector":     stock["sector"],
                "price":      round(last, 4),
                "change":     chg,
                "change_pct": chg_p,
                "market_cap": int(mktcap) if mktcap else None,
                "volume":     int(vol)    if vol    else None,
            })
        except Exception as e:
            print(f"  SKIP {t}: {e}")
            results.append({
                "ticker":     t,
                "name":       stock["name"],
                "sector":     stock["sector"],
                "price":      None,
                "change":     None,
                "change_pct": None,
                "market_cap": None,
                "volume":     None,
            })

    output = {
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "stocks":  results,
    }

    out_path = os.path.join(os.path.dirname(__file__), "..", "assets", "data", "stocks.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)

    print(f"Done. {len(results)} stocks written.")

if __name__ == "__main__":
    fetch_all()
