import unittest
from examples.research_pipeline import normalize
from examples.unit_economics import contribution, COST_FIELDS


class ResearchTests(unittest.TestCase):
    def setUp(self):
        self.row = {"source": "synthetic", "market": "us", "id": "demo-001",
                    "observed_at": "2026-09-23T00:00:00Z", "sold_units_7d": None,
                    "price": "29.90", "currency": "USD"}

    def test_missing_is_not_zero(self):
        missing = normalize([self.row])[0]
        zero = normalize([{**self.row, "sold_units_7d": 0}])[0]
        self.assertIsNone(missing["sold_units_7d"])
        self.assertEqual(zero["units_status"], "observed")

    def test_exact_duplicate_removed(self):
        self.assertEqual(len(normalize([self.row, self.row])), 1)

    def test_markets_and_observations_stay_separate(self):
        other_market = {**self.row, "market": "gb"}
        later = {**self.row, "observed_at": "2026-09-24T00:00:00Z"}
        self.assertEqual(len(normalize([self.row, other_market, later])), 3)

    def test_conflicting_duplicate_requires_review(self):
        with self.assertRaises(ValueError):
            normalize([self.row, {**self.row, "price": "99"}])

    def test_extra_fields_do_not_escape(self):
        self.assertNotIn("private_note", normalize([{**self.row, "private_note": "do not export"}])[0])

    def test_invalid_values_rejected(self):
        for change in ({"price": "NaN"}, {"price": "-1"}, {"price": "Infinity"},
                       {"sold_units_7d": True}, {"sold_units_7d": -1}, {"currency": None},
                       {"observed_at": "2026-09-23"}, {"id": ""}):
            with self.subTest(change=change), self.assertRaises(ValueError):
                normalize([{**self.row, **change}])


class EconomicsTests(unittest.TestCase):
    def setUp(self):
        self.costs = dict.fromkeys(COST_FIELDS, "0")

    def test_decimal_precision(self):
        self.costs["product"] = "0.1"
        self.assertEqual(contribution("0.3", self.costs, "USD")["contribution"], "0.2")

    def test_losses_not_hidden(self):
        self.costs["product"] = "40"
        self.assertEqual(contribution("30", self.costs, "USD")["contribution"], "-10")

    def test_zero_revenue_has_no_margin(self):
        self.assertIsNone(contribution("0", self.costs, "USD")["contribution_margin"])

    def test_missing_cost_not_silently_zero(self):
        del self.costs["fulfillment"]
        with self.assertRaises(ValueError):
            contribution("30", self.costs, "USD")

    def test_nonfinite_rejected(self):
        for value in ("NaN", "Infinity", "-1"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                contribution(value, self.costs, "USD")


if __name__ == "__main__":
    unittest.main()
