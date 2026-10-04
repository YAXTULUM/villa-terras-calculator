import unittest
from waterfall import Terms, calculate, xirr
from datetime import date


class WaterfallTests(unittest.TestCase):
    def test_example_reconciles_and_repays_capital(self):
        from json import loads
        from pathlib import Path
        data = loads((Path(__file__).parent / "example_deal.json").read_text())
        result = calculate(data["periods"], Terms(**data["terms"]))
        s = result["summary"]
        self.assertAlmostEqual(s["cash_difference"], 0, places=6)
        self.assertAlmostEqual(s["lp_capital_outstanding"], 0)
        self.assertAlmostEqual(s["gp_capital_outstanding"], 0)
        self.assertAlmostEqual(s["lp_preferred_outstanding"], 0)
        self.assertGreater(sum(p["gp_catchup"] for p in result["periods"]), 0)
        self.assertAlmostEqual(s["lp_distributions"] + s["gp_distributions"], 24500000)

    def test_partial_capital_return_has_no_promote(self):
        rows = [{"date": "2026-01-01", "lp_contribution": 70, "gp_contribution": 30},
                {"date": "2027-01-01", "cash": 50}]
        r = calculate(rows)["periods"][-1]
        self.assertAlmostEqual(r["lp_capital"], 35)
        self.assertAlmostEqual(r["gp_capital"], 15)
        self.assertAlmostEqual(r["lp_preferred"], 0)
        self.assertAlmostEqual(r["gp_catchup"], 0)

    def test_pref_and_catchup_disabled(self):
        rows = [{"date": "2026-01-01", "lp_contribution": 70, "gp_contribution": 30},
                {"date": "2027-01-01", "cash": 200}]
        r = calculate(rows, Terms(catchup_enabled=False))["periods"][-1]
        self.assertAlmostEqual(r["gp_catchup"], 0)
        self.assertGreater(r["lp_preferred"], 0)
        self.assertAlmostEqual(r["cash_difference"], 0)

    def test_additional_capital_and_missing_irr(self):
        rows = [{"date": "2026-01-01", "lp_contribution": 70, "gp_contribution": 30},
                {"date": "2027-01-01", "lp_contribution": 7, "cash": 0}]
        result = calculate(rows)
        self.assertEqual(result["summary"]["lp_irr"], None)
        self.assertAlmostEqual(result["summary"]["lp_capital_outstanding"], 77)
        self.assertIsNone(xirr([(date(2026, 1, 1), -1)]))

    def test_invalid_terms_rejected(self):
        with self.assertRaises(ValueError):
            calculate([{"date": "2026-01-01"}], Terms(tier3_lp_share=0))

    def test_nonfinite_inputs_rejected(self):
        with self.assertRaises(ValueError):
            calculate([{"date": "2026-01-01", "lp_contribution": 100, "cash": float("nan")}])
        with self.assertRaises(ValueError):
            calculate([{"date": "2026-01-01", "lp_contribution": float("inf")}])
        with self.assertRaises(ValueError):
            calculate([{"date": "2026-01-01"}], Terms(tier3_multiple=float("nan")))


if __name__ == "__main__":
    unittest.main()
