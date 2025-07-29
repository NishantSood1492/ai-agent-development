import json
from collections import defaultdict

def calculate_diversification_score(holdings_json: str) -> dict:
    """
    Accepts a JSON string of holdings and computes a diversification score.
    Each holding must have: symbol, weight, sector
    """
    try:
        holdings = json.loads(holdings_json)
    except Exception as e:
        return {"error": f"Invalid input format: {e}"}

    sector_weights = defaultdict(float)
    for asset in holdings:
        sector = asset.get("sector", "Unknown")
        weight = asset.get("weight", 0.0)
        sector_weights[sector] += weight

    total_weight = sum(sector_weights.values())
    herfindahl_index = sum((w / total_weight) ** 2 for w in sector_weights.values())
    diversification_score = max(0, round((1 - herfindahl_index) * 100, 2))
    overexposed = [s for s, w in sector_weights.items() if w / total_weight > 0.4]

    message = (
        f"Diversification score is {diversification_score}/100. "
        f"You're highly concentrated in: {', '.join(overexposed)}"
        if overexposed else
        f"Diversification looks good with score {diversification_score}/100."
    )

    return {
        "score": diversification_score,
        "overexposed_sectors": overexposed,
        "message": message
    }

