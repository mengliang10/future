"""
fetch_stocks.py — runs hourly via GitHub Actions
Fetches price data using yfinance and technical signals using tradingview-ta,
writes to assets/data/stocks.json so the static site can read it.
"""

import yfinance as yf
import json
import os
from datetime import datetime, timezone
from tradingview_ta import TA_Handler, Interval

STOCKS = [
    # Semiconductors
    {"ticker": "NVDA",  "name": "NVIDIA Corporation",           "sector": "Semiconductors", "exchange": "NASDAQ"},
    {"ticker": "AMD",   "name": "Advanced Micro Devices",        "sector": "Semiconductors", "exchange": "NASDAQ"},
    {"ticker": "INTC",  "name": "Intel Corporation",             "sector": "Semiconductors", "exchange": "NASDAQ"},
    {"ticker": "QCOM",  "name": "Qualcomm Inc.",                 "sector": "Semiconductors", "exchange": "NASDAQ"},
    {"ticker": "AVGO",  "name": "Broadcom Inc.",                 "sector": "Semiconductors", "exchange": "NASDAQ"},
    {"ticker": "MRVL",  "name": "Marvell Technology",            "sector": "Semiconductors", "exchange": "NASDAQ"},
    {"ticker": "MU",    "name": "Micron Technology",             "sector": "Semiconductors", "exchange": "NASDAQ"},
    {"ticker": "ARM",   "name": "Arm Holdings",                  "sector": "Semiconductors", "exchange": "NASDAQ"},
    {"ticker": "TSM",   "name": "Taiwan Semiconductor Mfg",      "sector": "Semiconductors", "exchange": "NYSE"},
    {"ticker": "ASML",  "name": "ASML Holding N.V.",             "sector": "Semiconductors", "exchange": "NASDAQ"},
    {"ticker": "AMAT",  "name": "Applied Materials Inc.",        "sector": "Semiconductors", "exchange": "NASDAQ"},
    {"ticker": "LRCX",  "name": "Lam Research Corp.",            "sector": "Semiconductors", "exchange": "NASDAQ"},
    {"ticker": "KLAC",  "name": "KLA Corporation",               "sector": "Semiconductors", "exchange": "NASDAQ"},
    {"ticker": "TXN",   "name": "Texas Instruments Inc.",        "sector": "Semiconductors", "exchange": "NASDAQ"},
    {"ticker": "ADI",   "name": "Analog Devices Inc.",           "sector": "Semiconductors", "exchange": "NASDAQ"},
    {"ticker": "MCHP",  "name": "Microchip Technology",          "sector": "Semiconductors", "exchange": "NASDAQ"},
    {"ticker": "NXPI",  "name": "NXP Semiconductors",            "sector": "Semiconductors", "exchange": "NASDAQ"},
    {"ticker": "ON",    "name": "ON Semiconductor",              "sector": "Semiconductors", "exchange": "NASDAQ"},
    {"ticker": "MPWR",  "name": "Monolithic Power Systems",      "sector": "Semiconductors", "exchange": "NASDAQ"},
    {"ticker": "SWKS",  "name": "Skyworks Solutions",            "sector": "Semiconductors", "exchange": "NASDAQ"},
    {"ticker": "CRUS",  "name": "Cirrus Logic Inc.",             "sector": "Semiconductors", "exchange": "NASDAQ"},
    {"ticker": "AMBA",  "name": "Ambarella Inc.",                "sector": "Semiconductors", "exchange": "NASDAQ"},
    {"ticker": "TER",   "name": "Teradyne Inc.",                 "sector": "Semiconductors", "exchange": "NASDAQ"},
    {"ticker": "ONTO",  "name": "Onto Innovation Inc.",          "sector": "Semiconductors", "exchange": "NYSE"},
    {"ticker": "ACLS",  "name": "Axcelis Technologies",          "sector": "Semiconductors", "exchange": "NASDAQ"},
    # AI & Cloud
    {"ticker": "MSFT",  "name": "Microsoft Corporation",         "sector": "AI & Cloud", "exchange": "NASDAQ"},
    {"ticker": "GOOGL", "name": "Alphabet Inc.",                 "sector": "AI & Cloud", "exchange": "NASDAQ"},
    {"ticker": "META",  "name": "Meta Platforms Inc.",           "sector": "AI & Cloud", "exchange": "NASDAQ"},
    {"ticker": "AMZN",  "name": "Amazon.com Inc.",               "sector": "AI & Cloud", "exchange": "NASDAQ"},
    {"ticker": "AAPL",  "name": "Apple Inc.",                    "sector": "AI & Cloud", "exchange": "NASDAQ"},
    {"ticker": "IBM",   "name": "IBM Corporation",               "sector": "AI & Cloud", "exchange": "NYSE"},
    {"ticker": "ORCL",  "name": "Oracle Corporation",            "sector": "AI & Cloud", "exchange": "NYSE"},
    {"ticker": "PLTR",  "name": "Palantir Technologies",         "sector": "AI & Cloud", "exchange": "NYSE"},
    {"ticker": "AI",    "name": "C3.ai Inc.",                    "sector": "AI & Cloud", "exchange": "NYSE"},
    {"ticker": "PATH",  "name": "UiPath Inc.",                   "sector": "AI & Cloud", "exchange": "NYSE"},
    {"ticker": "SOUN",  "name": "SoundHound AI Inc.",            "sector": "AI & Cloud", "exchange": "NASDAQ"},
    {"ticker": "BBAI",  "name": "BigBear.ai Holdings",           "sector": "AI & Cloud", "exchange": "NYSE"},
    {"ticker": "SNOW",  "name": "Snowflake Inc.",                "sector": "AI & Cloud", "exchange": "NYSE"},
    # Software
    {"ticker": "DDOG",  "name": "Datadog Inc.",                  "sector": "Software", "exchange": "NASDAQ"},
    {"ticker": "NET",   "name": "Cloudflare Inc.",               "sector": "Software", "exchange": "NYSE"},
    {"ticker": "NOW",   "name": "ServiceNow Inc.",               "sector": "Software", "exchange": "NYSE"},
    {"ticker": "CRM",   "name": "Salesforce Inc.",               "sector": "Software", "exchange": "NYSE"},
    {"ticker": "ADBE",  "name": "Adobe Inc.",                    "sector": "Software", "exchange": "NASDAQ"},
    {"ticker": "WDAY",  "name": "Workday Inc.",                  "sector": "Software", "exchange": "NASDAQ"},
    {"ticker": "INTU",  "name": "Intuit Inc.",                   "sector": "Software", "exchange": "NASDAQ"},
    {"ticker": "TEAM",  "name": "Atlassian Corporation",         "sector": "Software", "exchange": "NASDAQ"},
    {"ticker": "HUBS",  "name": "HubSpot Inc.",                  "sector": "Software", "exchange": "NYSE"},
    {"ticker": "MDB",   "name": "MongoDB Inc.",                  "sector": "Software", "exchange": "NASDAQ"},
    {"ticker": "GTLB",  "name": "GitLab Inc.",                   "sector": "Software", "exchange": "NASDAQ"},
    {"ticker": "ZS",    "name": "Zscaler Inc.",                  "sector": "Software", "exchange": "NASDAQ"},
    {"ticker": "OKTA",  "name": "Okta Inc.",                     "sector": "Software", "exchange": "NASDAQ"},
    {"ticker": "PANW",  "name": "Palo Alto Networks",            "sector": "Software", "exchange": "NASDAQ"},
    {"ticker": "ESTC",  "name": "Elastic N.V.",                  "sector": "Software", "exchange": "NYSE"},
    {"ticker": "BILL",  "name": "Bill Holdings Inc.",            "sector": "Software", "exchange": "NYSE"},
    {"ticker": "VEEV",  "name": "Veeva Systems Inc.",            "sector": "Software", "exchange": "NYSE"},
    {"ticker": "CRWD",  "name": "CrowdStrike Holdings",          "sector": "Software", "exchange": "NASDAQ"},
    # Hardware
    {"ticker": "SMCI",  "name": "Super Micro Computer",          "sector": "Hardware", "exchange": "NASDAQ"},
    {"ticker": "DELL",  "name": "Dell Technologies",             "sector": "Hardware", "exchange": "NYSE"},
    {"ticker": "HPE",   "name": "Hewlett Packard Enterprise",    "sector": "Hardware", "exchange": "NYSE"},
    {"ticker": "ANET",  "name": "Arista Networks Inc.",          "sector": "Hardware", "exchange": "NYSE"},
    {"ticker": "CSCO",  "name": "Cisco Systems Inc.",            "sector": "Hardware", "exchange": "NASDAQ"},
    {"ticker": "STX",   "name": "Seagate Technology",            "sector": "Hardware", "exchange": "NASDAQ"},
    {"ticker": "WDC",   "name": "Western Digital Corp.",         "sector": "Hardware", "exchange": "NASDAQ"},
    {"ticker": "PSTG",  "name": "Pure Storage Inc.",             "sector": "Hardware", "exchange": "NYSE"},
    {"ticker": "NTAP",  "name": "NetApp Inc.",                   "sector": "Hardware", "exchange": "NASDAQ"},
    {"ticker": "FFIV",  "name": "F5 Inc.",                       "sector": "Hardware", "exchange": "NASDAQ"},
    # Quantum
    {"ticker": "IONQ",  "name": "IonQ Inc.",                     "sector": "Quantum", "exchange": "NYSE"},
    {"ticker": "RGTI",  "name": "Rigetti Computing Inc.",        "sector": "Quantum", "exchange": "NASDAQ"},
    {"ticker": "QBTS",  "name": "D-Wave Quantum Inc.",           "sector": "Quantum", "exchange": "NYSE"},
    {"ticker": "ARQQ",  "name": "Arqit Quantum Inc.",            "sector": "Quantum", "exchange": "NASDAQ"},
    {"ticker": "QUBT",  "name": "Quantum Computing Inc.",        "sector": "Quantum", "exchange": "NASDAQ"},
    # Energy Tech
    {"ticker": "ENPH",  "name": "Enphase Energy Inc.",           "sector": "Energy Tech", "exchange": "NASDAQ"},
    {"ticker": "SEDG",  "name": "SolarEdge Technologies",        "sector": "Energy Tech", "exchange": "NASDAQ"},
    {"ticker": "FSLR",  "name": "First Solar Inc.",              "sector": "Energy Tech", "exchange": "NASDAQ"},
    {"ticker": "BE",    "name": "Bloom Energy Corp.",            "sector": "Energy Tech", "exchange": "NYSE"},
    {"ticker": "PLUG",  "name": "Plug Power Inc.",               "sector": "Energy Tech", "exchange": "NASDAQ"},
    {"ticker": "NEE",   "name": "NextEra Energy Inc.",           "sector": "Energy Tech", "exchange": "NYSE"},
    {"ticker": "GEV",   "name": "GE Vernova Inc.",               "sector": "Energy Tech", "exchange": "NYSE"},
    {"ticker": "ETN",   "name": "Eaton Corporation",             "sector": "Energy Tech", "exchange": "NYSE"},
    {"ticker": "PWR",   "name": "Quanta Services Inc.",          "sector": "Energy Tech", "exchange": "NYSE"},
    {"ticker": "SHLS",  "name": "Shoals Technologies",           "sector": "Energy Tech", "exchange": "NASDAQ"},
    # Robotics & Auto
    {"ticker": "TSLA",  "name": "Tesla Inc.",                    "sector": "Robotics & Auto", "exchange": "NASDAQ"},
    {"ticker": "ISRG",  "name": "Intuitive Surgical Inc.",       "sector": "Robotics & Auto", "exchange": "NASDAQ"},
    {"ticker": "ROK",   "name": "Rockwell Automation",           "sector": "Robotics & Auto", "exchange": "NYSE"},
    {"ticker": "HON",   "name": "Honeywell International",       "sector": "Robotics & Auto", "exchange": "NASDAQ"},
    {"ticker": "FARO",  "name": "FARO Technologies Inc.",        "sector": "Robotics & Auto", "exchange": "NASDAQ"},
    {"ticker": "LAZR",  "name": "Luminar Technologies",          "sector": "Robotics & Auto", "exchange": "NASDAQ"},
    {"ticker": "MVIS",  "name": "MicroVision Inc.",              "sector": "Robotics & Auto", "exchange": "NASDAQ"},
    {"ticker": "OUST",  "name": "Ouster Inc.",                   "sector": "Robotics & Auto", "exchange": "NYSE"},
    {"ticker": "AEVA",  "name": "Aeva Technologies Inc.",        "sector": "Robotics & Auto", "exchange": "NYSE"},
    {"ticker": "INVZ",  "name": "Innoviz Technologies",          "sector": "Robotics & Auto", "exchange": "NASDAQ"},
    # Space Tech
    {"ticker": "RKLB",  "name": "Rocket Lab USA Inc.",           "sector": "Space Tech", "exchange": "NASDAQ"},
    {"ticker": "ASTS",  "name": "AST SpaceMobile Inc.",          "sector": "Space Tech", "exchange": "NASDAQ"},
    {"ticker": "LUNR",  "name": "Intuitive Machines Inc.",       "sector": "Space Tech", "exchange": "NASDAQ"},
    {"ticker": "SPIR",  "name": "Spire Global Inc.",             "sector": "Space Tech", "exchange": "NYSE"},
    {"ticker": "MNTS",  "name": "Momentus Inc.",                 "sector": "Space Tech", "exchange": "NASDAQ"},
    {"ticker": "SATL",  "name": "Satellogic Inc.",               "sector": "Space Tech", "exchange": "NASDAQ"},
    {"ticker": "GSAT",  "name": "Globalstar Inc.",               "sector": "Space Tech", "exchange": "NYSE"},
    {"ticker": "VSAT",  "name": "Viasat Inc.",                   "sector": "Space Tech", "exchange": "NASDAQ"},
    {"ticker": "RDW",   "name": "Redwire Corporation",           "sector": "Space Tech", "exchange": "NYSE"},
    {"ticker": "BKSY",  "name": "BlackSky Technology",           "sector": "Space Tech", "exchange": "NYSE"},
]

def fetch_all():
    tickers_list = [s["ticker"] for s in STOCKS]
    
    print(f"Fetching raw data for {len(tickers_list)} stocks...")
    raw = yf.download(tickers_list, period="2d", interval="1d",
                      auto_adjust=True, progress=False, group_by="ticker")

    results = []
    for stock in STOCKS:
        t = stock["ticker"]
        ex = stock["exchange"]
        try:
            # yfinance data
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

            # TradingView technicals
            print(f"  Analysing {t}...")
            handler = TA_Handler(
                symbol=t,
                exchange=ex,
                screener="america",
                interval=Interval.INTERVAL_1_DAY
            )
            analysis = handler.get_analysis()
            
            results.append({
                "ticker":     t,
                "name":       stock["name"],
                "sector":     stock["sector"],
                "price":      round(last, 4),
                "change":     chg,
                "change_pct": chg_p,
                "market_cap": int(mktcap) if mktcap else None,
                "volume":     int(vol)    if vol    else None,
                "signal":     analysis.summary['RECOMMENDATION'].replace("_", " "),
                "rsi":        round(analysis.indicators['RSI'], 2)
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
                "signal":     "N/A",
                "rsi":        None
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
