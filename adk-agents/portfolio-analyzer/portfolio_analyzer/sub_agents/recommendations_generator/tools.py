def generate_recommendations(cash_drag_message: str, diversification_message: str) -> list:
    """
    Synthesizes messages into 3 high-impact recommendations.

    Args:
        cash_drag_message: Message from the cash drag agent
        diversification_message: Message from the diversification agent

    Returns:
        list: List of 3 high-impact recommendations
    """
    recommendations = []

    if "cash_drag_score" in cash_drag_message or "missing out" in cash_drag_message:
        recommendations.append({
            "recommendation": "Deploy idle cash into a diversified investment.",
            "rationale": cash_drag_message,
            "impact": "High",
            "ease": "Easy"
        })

    if "Tech" in diversification_message or "concentrated" in diversification_message:
        recommendations.append({
            "recommendation": "Reduce sector concentration (e.g., Tech <30%).",
            "rationale": diversification_message,
            "impact": "Medium",
            "ease": "Medium"
        })

    # Limit to top 3
    return recommendations[:3]
