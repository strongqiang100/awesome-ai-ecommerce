"""Illustrative per-order contribution in one currency; no tax or FX engine."""
from decimal import Decimal, InvalidOperation
import json

COST_FIELDS = ("product", "inbound_freight", "fulfillment", "platform_fees",
               "payment_fees", "creator_commission", "advertising", "expected_returns_loss")


def amount(value):
    try:
        result = Decimal(str(value))
    except InvalidOperation as exc:
        raise ValueError("Invalid money value") from exc
    if not result.is_finite() or result < 0:
        raise ValueError("Money values must be finite and non-negative")
    return result


def contribution(net_revenue, costs, currency):
    if not isinstance(currency, str) or len(currency) != 3 or not currency.isalpha():
        raise ValueError("Provide a three-letter currency code")
    if set(costs) != set(COST_FIELDS):
        raise ValueError("Provide every defined cost exactly once; use zero explicitly")
    revenue = amount(net_revenue)
    total = sum((amount(costs[name]) for name in COST_FIELDS), Decimal("0"))
    result = revenue - total
    margin = None if revenue == 0 else result / revenue
    return {"currency": currency.upper(), "net_revenue": str(revenue),
            "variable_costs": str(total), "contribution": str(result),
            "contribution_margin": None if margin is None else str(margin)}


if __name__ == "__main__":
    costs = dict(zip(COST_FIELDS, ("7", "1", "4", "2", "1", "0", "5", "2")))
    print(json.dumps(contribution("30", costs, "USD"), indent=2))
