import json
import os

STOCKS_JSON = os.path.join(os.path.dirname(__file__), '..', 'assets', 'data', 'stocks.json')
STOCKS_DIR = os.path.join(os.path.dirname(__file__), '..', '_stocks')

def generate_stock_pages():
    with open(STOCKS_JSON, 'r') as f:
        data = json.load(f)
    
    stocks = data.get('stocks', [])
    
    os.makedirs(STOCKS_DIR, exist_ok=True)
    
    for s in stocks:
        ticker = s['ticker']
        name = s['name']
        sector = s['sector']
        
        # Determine exchange (heuristic)
        # Most tech is NASDAQ, TSM is NYSE
        exchange = "NASDAQ"
        if ticker in ["TSM", "IBM", "ORCL", "XOM", "CVX", "SHEL", "BP", "TTE", "OXY", "SLB", "GEV", "ETN", "PWR", "JPM", "GS", "MS", "BAC", "WFC", "C", "V", "MA", "AXP"]:
            exchange = "NYSE"
        
        file_path = os.path.join(STOCKS_DIR, f"{ticker.lower()}.md")
        
        # If file exists, skip or update? User said "create stock pages for all".
        # I'll create them if they don't exist to preserve manual work on NVDA/TSM/AMD.
        if os.path.exists(file_path):
            print(f"Skipping {ticker}, file already exists.")
            continue
            
        content = f"""---
layout: stock
name: "{name}"
symbol: {ticker}
exchange: {exchange}
categories: [{sector}]
---

## Investment Thesis
Detailed fundamental analysis and growth catalysts for {name} ({ticker}) are currently under review.

### Sector Performance
As part of the **{sector}** sector, {ticker} is positioned to benefit from the ongoing expansion in digital infrastructure and AI deployment.

### Market Context
- **Industry Position:** Key player in {sector}.
- **Technical Horizon:** Monitoring for high-probability entry points based on sectoral momentum.
"""
        with open(file_path, 'w') as sf:
            sf.write(content)
        print(f"Generated page for {ticker}")

if __name__ == "__main__":
    generate_stock_pages()
