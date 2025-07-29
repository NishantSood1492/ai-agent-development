def calculate_cash_drag(idle_cash: float, benchmark_return: float, time_horizon_years: float) -> dict:
    """
    Estimate the opportunity cost of idle cash.

    Args:
        idle_cash: Amount of idle cash (in dollars)
        benchmark_return: Annual expected return (in %)
        time_horizon_years: Time horizon over which to calculate the drag

    Returns:
        dict: opportunity_cost and explanation message
    """
    rate = benchmark_return / 100
    drag = idle_cash * rate * time_horizon_years
    message = (
        f"With ${idle_cash:,.2f} sitting idle over {time_horizon_years} year(s), "
        f"and an expected return of {benchmark_return}%, "
        f"you're potentially missing out on ${drag:,.2f} in returns."
    )
    return {"opportunity_cost": drag, "message": message}
