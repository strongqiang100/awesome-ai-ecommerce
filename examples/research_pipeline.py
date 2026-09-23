"""Offline synthetic product normalization; no network or business writes."""
import json
from decimal import Decimal, InvalidOperation


def normalize(records):
    """Deduplicate exact snapshots; reject conflicting duplicates and invalid values.

    Keys include source, market, product ID and observation time. Unknown extra
    fields are excluded. This is an in-memory demonstration, not durable storage.
    """
    output, seen = [], {}
    for record in records:
        for field in ("source", "market", "id", "observed_at"):
            if not isinstance(record.get(field), str) or not record[field].strip():
                raise ValueError(f"Missing or invalid {field}")
        from datetime import datetime
        try:
            observed = datetime.fromisoformat(record["observed_at"].replace("Z", "+00:00"))
        except ValueError as exc:
            raise ValueError("Invalid observation time") from exc
        if observed.utcoffset() is None:
            raise ValueError("Observation time requires a timezone")
        units = record.get("sold_units_7d")
        if units is not None and (type(units) is not int or units < 0):
            raise ValueError("Units must be a non-negative integer or null")
        price = record.get("price")
        currency = record.get("currency")
        if price is not None:
            if not isinstance(currency, str) or len(currency) != 3 or not currency.isalpha():
                raise ValueError("Known prices require a three-letter currency code")
            try:
                amount = Decimal(str(price))
            except InvalidOperation as exc:
                raise ValueError("Invalid price") from exc
            if not amount.is_finite() or amount < 0:
                raise ValueError("Price must be finite and non-negative")
            price = str(amount)
        normalized = {
            "schema_version": "1.0",
            "source": record["source"].strip(),
            "market": record["market"].strip().upper(),
            "source_record_id": record["id"].strip(),
            "observed_at": observed.isoformat(),
            "sold_units_7d": units,
            "units_status": "missing" if units is None else "observed",
            "price": price,
            "currency": currency.upper() if price is not None else None,
        }
        key = tuple(normalized[k] for k in ("source", "market", "source_record_id", "observed_at"))
        if key in seen:
            if seen[key] != normalized:
                raise ValueError("Conflicting duplicate snapshot requires review")
            continue
        seen[key] = normalized
        output.append(normalized)
    return output


if __name__ == "__main__":
    sample = {
        "source": "synthetic", "market": "us", "id": "demo-001",
        "observed_at": "2026-09-23T00:00:00Z", "sold_units_7d": None,
        "price": "29.90", "currency": "USD",
    }
    print(json.dumps(normalize([sample, dict(sample)]), indent=2))
