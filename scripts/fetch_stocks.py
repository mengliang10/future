"""
fetch_stocks.py — runs hourly via GitHub Actions
Fetches price data using yfinance and technical signals using tradingview-ta,
writes to assets/data/stocks.json so the static site can read it.
"""

import yfinance as yf
import json
import os
import time
from datetime import datetime, timezone
from tradingview_ta import TA_Handler, Interval

# Load universe from JSON file
UNIVERSE_PATH = os.path.join(os.path.dirname(__file__), "stocks_universe.json")
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "assets", "data", "stocks.json")

def fetch_all():
    if not os.path.exists(UNIVERSE_PATH):
        print(f"Error: {UNIVERSE_PATH} not found.")
        return

    with open(UNIVERSE_PATH) as f:
        STOCKS = json.load(f)

    # Load existing data as fallback
    existing_data = {}
    if os.path.exists(OUTPUT_PATH):
        try:
            with open(OUTPUT_PATH) as f:
                old_json = json.load(f)
                existing_data = {s["ticker"]: s for s in old_json.get("stocks", [])}
        except Exception as e:
            print(f"Warning: Could not load existing data: {e}")

    tickers_list = [s["ticker"] for s in STOCKS]
    
    print(f"Fetching raw data for {len(tickers_list)} stocks...")
    try:
        raw = yf.download(tickers_list, period="2d", interval="1d",
                          auto_adjust=True, progress=False, group_by="ticker")
    except Exception as e:
        print(f"Global download error: {e}")
        # If global download fails, we might want to stop or use all existing data
        return

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

            ticker_obj = yf.Ticker(t)
            info = ticker_obj.fast_info
            mktcap = getattr(info, "market_cap", None)
            vol    = getattr(info, "three_month_average_volume", None)

            # TradingView technicals with retry logic
            print(f"  Analysing {t}...")
            analysis = None
            retries = 3
            for attempt in range(retries):
                try:
                    handler = TA_Handler(
                        symbol=t,
                        exchange=ex,
                        screener="america",
                        interval=Interval.INTERVAL_1_DAY
                    )
                    analysis = handler.get_analysis()
                    break
                except Exception as e:
                    if "429" in str(e) or "Too Many Requests" in str(e):
                        wait = (attempt + 1) * 5
                        print(f"    Rate limited for {t}, waiting {wait}s...")
                        time.sleep(wait)
                    else:
                        raise e
            
            if analysis:
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
            elif t in existing_data:
                print(f"    Using previous data for {t}")
                results.append(existing_data[t])
                
        except Exception as e:
            print(f"  SKIP {t}: {e}")
            if t in existing_data:
                print(f"    Falling back to previous data for {t}")
                results.append(existing_data[t])

    if not results:
        print("Error: No stock data fetched and no fallback available. Aborting write.")
        return

    output = {
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "stocks":  results,
    }

    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2)

    print(f"Done. {len(results)} stocks written.")

if __name__ == "__main__":
    fetch_all()

