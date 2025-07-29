from typing import TypedDict, List
import random


class Holding(TypedDict):
    symbol: str
    weight: float
    sector: str


class PortfolioData(TypedDict):
    idle_cash: float
    benchmark_return: float
    time_horizon_years: float
    holdings: List[Holding]


def fetch_portfolio_data(portfolio_id: str) -> PortfolioData:
    random.seed(portfolio_id)  # Ensure deterministic output per portfolio

    sectors = ["Technology", "Financials", "Healthcare", "Energy", "Utilities"]
    symbols = ["AAPL", "TD", "ENB", "JNJ", "MSFT", "GOOG", "BNS", "XOM", "BMO", "CP"]

    holdings = [
        {
            "symbol": random.choice(symbols),
            "weight": round(random.uniform(5, 30), 2),
            "sector": random.choice(sectors),
        }
        for _ in range(5)
    ]

    total_weights = sum(h["weight"] for h in holdings)
    # Normalize to 100%
    for h in holdings:
        h["weight"] = round(h["weight"] / total_weights * 100, 2)

    return {
        "idle_cash": round(random.uniform(5000, 25000), 2),
        "benchmark_return": 6.5,  # Annual benchmark return in %
        "time_horizon_years": 1.0,  # 1-year window
        "holdings": holdings,
    }

