"""
fetch_stocks_enriched.py — Enhanced stock data with engine metrics
==================================================================
Drop-in replacement for fetch_stocks.py. Adds timing quality, regime,
alpha signals, OB fingerprints, and factor scores to stocks.json.

Self-contained — only needs yfinance + numpy (works in GitHub Actions).
"""

import yfinance as yf
import json
import os
import numpy as np
from datetime import datetime, timezone

# ═══════════════════════════════════════════════════════
# OVERBOUGHT FINGERPRINTS (from backtest May 7, 2026)
# ═══════════════════════════════════════════════════════
OB_FINGERPRINTS = {
    'MU':   {'rsi70_win':81,'type':'MOMENTUM_LEADER'},  'NVDA':{'rsi70_win':76,'type':'MOMENTUM_LEADER'},
    'INTC': {'rsi70_win':59,'type':'MOMENTUM'},         'AVGO':{'rsi70_win':59,'type':'MOMENTUM'},
    'AMD':  {'rsi70_win':53,'type':'NEUTRAL'},          'QCOM':{'rsi70_win':56,'type':'NEUTRAL'},
    'TSM':  {'rsi70_win':76,'type':'MOMENTUM_LEADER'},  'ARM': {'rsi70_win':22,'type':'MEAN_REVERTER'},
}

# ═══════════════════════════════════════════════════════
# STOCK LIST
# ═══════════════════════════════════════════════════════
STOCKS = [
    {"ticker":"NVDA","name":"NVIDIA","sector":"Semiconductors","exchange":"NASDAQ"},
    {"ticker":"AMD","name":"AMD","sector":"Semiconductors","exchange":"NASDAQ"},
    {"ticker":"INTC","name":"Intel","sector":"Semiconductors","exchange":"NASDAQ"},
    {"ticker":"QCOM","name":"Qualcomm","sector":"Semiconductors","exchange":"NASDAQ"},
    {"ticker":"AVGO","name":"Broadcom","sector":"Semiconductors","exchange":"NASDAQ"},
    {"ticker":"MRVL","name":"Marvell","sector":"Semiconductors","exchange":"NASDAQ"},
    {"ticker":"MU","name":"Micron","sector":"Semiconductors","exchange":"NASDAQ"},
    {"ticker":"ARM","name":"Arm Holdings","sector":"Semiconductors","exchange":"NASDAQ"},
    {"ticker":"TSM","name":"TSMC","sector":"Semiconductors","exchange":"NYSE"},
    {"ticker":"ASML","name":"ASML","sector":"Semiconductors","exchange":"NASDAQ"},
    {"ticker":"AMAT","name":"Applied Materials","sector":"Semiconductors","exchange":"NASDAQ"},
    {"ticker":"LRCX","name":"Lam Research","sector":"Semiconductors","exchange":"NASDAQ"},
    {"ticker":"KLAC","name":"KLA Corp","sector":"Semiconductors","exchange":"NASDAQ"},
    {"ticker":"TXN","name":"Texas Instruments","sector":"Semiconductors","exchange":"NASDAQ"},
    {"ticker":"ADI","name":"Analog Devices","sector":"Semiconductors","exchange":"NASDAQ"},
    {"ticker":"MSFT","name":"Microsoft","sector":"AI & Cloud","exchange":"NASDAQ"},
    {"ticker":"GOOGL","name":"Alphabet","sector":"AI & Cloud","exchange":"NASDAQ"},
    {"ticker":"META","name":"Meta","sector":"AI & Cloud","exchange":"NASDAQ"},
    {"ticker":"AMZN","name":"Amazon","sector":"AI & Cloud","exchange":"NASDAQ"},
    {"ticker":"AAPL","name":"Apple","sector":"AI & Cloud","exchange":"NASDAQ"},
    {"ticker":"PLTR","name":"Palantir","sector":"AI & Cloud","exchange":"NYSE"},
    {"ticker":"SNOW","name":"Snowflake","sector":"AI & Cloud","exchange":"NYSE"},
    {"ticker":"CRM","name":"Salesforce","sector":"Software","exchange":"NYSE"},
    {"ticker":"NOW","name":"ServiceNow","sector":"Software","exchange":"NYSE"},
    {"ticker":"CRWD","name":"CrowdStrike","sector":"Software","exchange":"NASDAQ"},
    {"ticker":"DDOG","name":"Datadog","sector":"Software","exchange":"NASDAQ"},
    {"ticker":"SMCI","name":"Super Micro","sector":"Hardware","exchange":"NASDAQ"},
    {"ticker":"ANET","name":"Arista Networks","sector":"Hardware","exchange":"NYSE"},
    {"ticker":"DELL","name":"Dell","sector":"Hardware","exchange":"NYSE"},
    {"ticker":"TSLA","name":"Tesla","sector":"Robotics & Auto","exchange":"NASDAQ"},
    {"ticker":"IONQ","name":"IonQ","sector":"Quantum","exchange":"NYSE"},
    {"ticker":"RGTI","name":"Rigetti","sector":"Quantum","exchange":"NASDAQ"},
    {"ticker":"RKLB","name":"Rocket Lab","sector":"Space Tech","exchange":"NASDAQ"},
    {"ticker":"ASTS","name":"AST SpaceMobile","sector":"Space Tech","exchange":"NASDAQ"},
    {"ticker":"ENPH","name":"Enphase Energy","sector":"Energy Tech","exchange":"NASDAQ"},
    {"ticker":"FSLR","name":"First Solar","sector":"Energy Tech","exchange":"NASDAQ"},
]


# ═══════════════════════════════════════════════════════
# ENGINE FUNCTIONS (self-contained, no Trading imports)
# ═══════════════════════════════════════════════════════

def compute_timing_quality(close, high, low, volume):
    """
    Timing quality score (0-100). Higher = better entry timing.
    Mirrors TimingEngine logic.
    """
    n = len(close)
    if n < 20:
        return 50, 'WAIT', 'insufficient data'
    
    price = close[-1]
    sma20 = np.mean(close[-20:])
    sma50 = np.mean(close[-min(50,n):])
    dist20 = (price - sma20) / sma20 * 100
    
    # RSI
    delta = np.diff(close)
    gains = delta[delta > 0]
    losses = -delta[delta < 0]
    avg_gain = np.mean(gains[-14:]) if len(gains) >= 14 else np.mean(gains) if len(gains) > 0 else 0
    avg_loss = np.mean(losses[-14:]) if len(losses) >= 14 else np.mean(losses) if len(losses) > 0 else 1e-9
    rsi = 100 - 100/(1 + avg_gain/avg_loss) if avg_loss > 0 else 100
    
    # Extension score (0-100, higher = worse)
    ext = 0
    d20 = abs(dist20)
    if d20 >= 30: ext = 100
    elif d20 >= 15: ext = 80
    elif d20 >= 8: ext = 50
    elif d20 >= 3: ext = 20
    else: ext = max(d20/3*15, 0)
    
    # Overbought score
    ob = 0
    if rsi >= 85: ob = 100
    elif rsi >= 75: ob = 80
    elif rsi >= 70: ob = 50
    elif rsi >= 60: ob = 20
    elif rsi >= 40: ob = 5
    else: ob = 15
    
    quality = 100 - max(ext, ob)
    quality = max(0, min(100, quality))
    
    # Action
    if quality >= 70: action = 'FULL'
    elif quality >= 50: action = 'HALF'
    elif quality >= 30: action = 'QUARTER'
    elif quality >= 15: action = 'WAIT'
    else: action = 'AVOID'
    
    return quality, action, f'ext={ext:.0f} ob={ob:.0f} rsi={rsi:.0f}'


def detect_regime(close):
    """Detect market regime: TRENDING_UP, RANGE_BOUND, HIGH_VOL, etc."""
    n = len(close)
    if n < 60:
        return 'UNKNOWN', 0.5
    
    # Trend detection
    ma20 = np.mean(close[-20:])
    ma50 = np.mean(close[-min(50,n):])
    ma100 = np.mean(close[-min(100,n):])
    
    x = np.arange(min(60,n))
    y = close[-60:] if n >= 60 else close
    slope = np.polyfit(x, y, 1)[0] / np.mean(y) * 100 * 252
    
    # MA alignment
    if ma20 > ma50 > ma100: align = 1
    elif ma20 < ma50 < ma100: align = -1
    else: align = 0
    
    # Volatility
    returns = np.diff(np.log(close[-60:]))
    vol_20 = np.std(returns[-20:]) * np.sqrt(252) * 100
    
    # Regime classification
    if vol_20 > 60:
        return 'HIGH_VOL', 0.80
    elif abs(slope) > 20 and align != 0:
        return 'TRENDING_UP' if slope > 0 else 'TRENDING_DOWN', 0.75
    elif abs(slope) < 10:
        return 'RANGE_BOUND', 0.60
    elif slope > 0:
        return 'TRENDING_UP', 0.55
    else:
        return 'LOW_VOL', 0.60


def compute_alpha_signals(close, high, low, volume):
    """Compute key alpha signals. Returns bullish%, top signal names."""
    n = len(close)
    if n < 26:
        return 0.50, 'NEUTRAL', ''
    
    price = close[-1]
    
    # Momentum
    ret_20 = (close[-1]/close[-21]-1)*100 if n > 20 else 0
    rsi_14 = _rsi(close, 14)
    macd = np.mean(close[-12:]) - np.mean(close[-26:])
    
    # Mean reversion
    sma20 = np.mean(close[-20:])
    zscore = (price - sma20) / np.std(close[-20:]) if np.std(close[-20:]) > 0 else 0
    
    # Volume
    vol_ratio = np.mean(volume[-5:]) / np.mean(volume[-20:]) if np.mean(volume[-20:]) > 0 else 1
    
    # Score each
    signals = []
    if ret_20 > 5: signals.append(1)
    elif ret_20 < -5: signals.append(-1)
    else: signals.append(0)
    
    if 40 < rsi_14 < 60: signals.append(1)
    elif rsi_14 > 75: signals.append(-1)
    else: signals.append(0)
    
    if macd > 0: signals.append(1)
    else: signals.append(-1)
    
    if zscore < -1: signals.append(1)
    elif zscore > 2: signals.append(-1)
    else: signals.append(0)
    
    if 0.8 < vol_ratio < 2: signals.append(1)
    else: signals.append(0)
    
    bull = sum(1 for s in signals if s > 0)
    bear = sum(1 for s in signals if s < 0)
    total = len(signals)
    
    if total == 0: return 0.50, 'NEUTRAL', ''
    
    bull_pct = bull / total
    
    if bull_pct > 0.6: signal = 'BULLISH'
    elif bull_pct > 0.4: signal = 'NEUTRAL'
    else: signal = 'BEARISH'
    
    return bull_pct, signal, f'{bull}/{total} bullish'


def compute_factor_score(info, close):
    """Quick factor score from fundamentals + price."""
    fwdpe = info.get('forwardPE') or 999
    revgr = (info.get('revenueGrowth') or 0) * 100
    roe = (info.get('returnOnEquity') or 0) * 100
    beta = info.get('beta') or 1
    
    score = 50
    if 0 < fwdpe < 30: score += 10
    if revgr > 20: score += 10
    if roe > 20: score += 10
    if beta < 1.5: score += 5
    if fwdpe > 100: score -= 20
    
    return max(0, min(100, score))


def _rsi(close, period=14):
    delta = np.diff(close[-period-1:])
    gains = delta[delta > 0]
    losses = -delta[delta < 0]
    avg_gain = np.mean(gains) if len(gains) > 0 else 0
    avg_loss = np.mean(losses) if len(losses) > 0 else 1e-9
    return 100 - 100/(1 + avg_gain/avg_loss) if avg_loss > 0 else 50


# ═══════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════

def fetch_all():
    tickers_list = [s["ticker"] for s in STOCKS]
    print(f"Fetching {len(tickers_list)} stocks with engine metrics...")
    
    # Batch download (faster than per-ticker)
    raw = yf.download(tickers_list, period="3mo", interval="1d",
                      auto_adjust=True, progress=False, group_by="ticker")
    
    results = []
    for stock in STOCKS:
        t = stock["ticker"]
        try:
            # Price data from batch
            if len(tickers_list) == 1:
                closes_raw = raw["Close"]
                highs = raw["High"]
                lows = raw["Low"]
                volumes = raw["Volume"]
            else:
                closes_raw = raw[t]["Close"]
                highs = raw[t]["High"]
                lows = raw[t]["Low"]
                volumes = raw[t]["Volume"]
            
            closes = closes_raw.dropna()
            if len(closes) < 2:
                raise ValueError("insufficient data")
            
            prev = float(closes.iloc[-2])
            last = float(closes.iloc[-1])
            chg = round(last - prev, 4)
            chg_p = round((chg / prev) * 100, 4)
            
            # Fundamentals
            info = yf.Ticker(t).fast_info
            mktcap = getattr(info, "market_cap", None)
            vol_avg = getattr(info, "three_month_average_volume", None)
            
            # === ENGINE METRICS ===
            c_arr = closes.values
            h_arr = highs.dropna().values if len(highs.dropna()) > 0 else c_arr
            l_arr = lows.dropna().values if len(lows.dropna()) > 0 else c_arr
            v_arr = volumes.dropna().values if len(volumes.dropna()) > 0 else np.ones_like(c_arr)
            
            # Timing
            timing_q, timing_a, timing_d = compute_timing_quality(c_arr, h_arr, l_arr, v_arr)
            
            # Regime
            regime, regime_conf = detect_regime(c_arr)
            
            # Alphas
            alpha_bull, alpha_sig, alpha_det = compute_alpha_signals(c_arr, h_arr, l_arr, v_arr)
            
            # Factor score
            full_info = yf.Ticker(t).info  # Need full info for fundamentals
            factor = compute_factor_score(full_info, c_arr)
            
            # OB fingerprint
            fp = OB_FINGERPRINTS.get(t, {})
            ob_type = fp.get('type', 'UNKNOWN')
            ob_win = fp.get('rsi70_win', None)
            
            # RSI
            rsi_val = _rsi(c_arr)
            
            # Price vs MAs
            sma20 = float(np.mean(c_arr[-20:])) if len(c_arr) >= 20 else last
            sma50 = float(np.mean(c_arr[-min(50,len(c_arr)):]))
            
            # 30d return
            ret_30d = round((last / c_arr[-min(21,len(c_arr))] - 1) * 100, 2) if len(c_arr) >= 21 else None
            
            print(f"  {t}: timing={timing_q:.0f} regime={regime} alpha={alpha_sig} factor={factor:.0f}")
            
            results.append({
                # Core
                "ticker": t,
                "name": stock["name"],
                "sector": stock["sector"],
                "price": round(last, 4),
                "change": chg,
                "change_pct": chg_p,
                "market_cap": int(mktcap) if mktcap else None,
                "volume": int(vol_avg) if vol_avg else None,
                # Technical
                "rsi": round(rsi_val, 1),
                "sma20": round(sma20, 2),
                "sma50": round(sma50, 2),
                "ret_30d": ret_30d,
                # Engine metrics
                "timing_quality": round(timing_q, 0),
                "timing_action": timing_a,
                "timing_detail": timing_d,
                "regime": regime,
                "regime_confidence": round(regime_conf, 2),
                "alpha_signal": alpha_sig,
                "alpha_bullish_pct": round(alpha_bull * 100, 0),
                "alpha_detail": alpha_det,
                "factor_score": round(factor, 0),
                "ob_fingerprint": ob_type,
                "ob_rsi70_winrate": ob_win,
            })
            
        except Exception as e:
            print(f"  SKIP {t}: {e}")
            results.append({
                "ticker": t, "name": stock["name"], "sector": stock["sector"],
                "price": None, "change": None, "change_pct": None,
                "market_cap": None, "volume": None,
                "rsi": None, "sma20": None, "sma50": None, "ret_30d": None,
                "timing_quality": None, "timing_action": "N/A",
                "regime": "N/A", "alpha_signal": "N/A",
                "factor_score": None, "ob_fingerprint": "UNKNOWN",
            })
    
    output = {
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "stock_count": len(results),
        "stocks": results,
    }
    
    out_path = os.path.join(os.path.dirname(__file__), "..", "assets", "data", "stocks.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    
    print(f"\nDone. {len(results)} stocks written with engine metrics.")


if __name__ == "__main__":
    fetch_all()
