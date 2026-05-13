from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

client: Optional[OpenAI] = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None


@dataclass(frozen=True)
class InvestmentScenario:
    property_price: float
    down_payment: float
    closing_costs: float
    rehab_costs: float
    annual_rent_income: float
    annual_property_taxes: float
    annual_insurance: float
    annual_utilities: float
    maintenance_perc: float
    capex_perc: float
    mgmt_perc: float
    vacancy_perc: float
    hoa_fees: float
    other_income: float
    interest_rate: float
    loan_term: int
    exit_cap_rate: float = 6.5
    annual_growth_rate: float = 2.0
    hold_years: int = 5


REQUIRED_FIELDS = [
    "property_price",
    "down_payment",
    "closing_costs",
    "rehab_costs",
    "annual_rent_income",
    "annual_property_taxes",
    "annual_insurance",
    "annual_utilities",
    "maintenance_perc",
    "capex_perc",
    "mgmt_perc",
    "vacancy_perc",
    "hoa_fees",
    "other_income",
    "interest_rate",
    "loan_term",
]


def _to_float(value: Any, field_name: str) -> float:
    try:
        return float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{field_name} must be numeric") from exc


def normalize_financial_details(financial_details: Dict[str, Any]) -> InvestmentScenario:
    missing = [field for field in REQUIRED_FIELDS if field not in financial_details]
    if missing:
        raise ValueError("Missing required fields: " + ", ".join(missing))

    normalized = {field: _to_float(financial_details[field], field) for field in REQUIRED_FIELDS}
    normalized["loan_term"] = int(normalized["loan_term"])
    normalized["exit_cap_rate"] = _to_float(financial_details.get("exit_cap_rate", 6.5), "exit_cap_rate")
    normalized["annual_growth_rate"] = _to_float(financial_details.get("annual_growth_rate", 2.0), "annual_growth_rate")
    normalized["hold_years"] = int(_to_float(financial_details.get("hold_years", 5), "hold_years"))

    if normalized["property_price"] <= 0:
        raise ValueError("property_price must be greater than zero")
    if normalized["down_payment"] < 0:
        raise ValueError("down_payment cannot be negative")
    if normalized["loan_term"] <= 0:
        raise ValueError("loan_term must be greater than zero")
    if normalized["hold_years"] <= 0:
        raise ValueError("hold_years must be greater than zero")

    return InvestmentScenario(**normalized)


def calculate_monthly_payment(loan_amount: float, annual_rate: float, years: int) -> float:
    if loan_amount <= 0:
        return 0.0

    number_of_payments = years * 12
    monthly_rate = annual_rate / 100 / 12

    if monthly_rate == 0:
        return loan_amount / number_of_payments

    return loan_amount * monthly_rate / (1 - (1 + monthly_rate) ** (-number_of_payments))


def calculate_irr(cash_flows: List[float], tolerance: float = 0.000001, max_iterations: int = 200) -> float:
    def npv(rate: float) -> float:
        return sum(value / ((1 + rate) ** index) for index, value in enumerate(cash_flows))

    low = -0.9999
    high = 10.0
    low_value = npv(low)
    high_value = npv(high)

    if low_value * high_value > 0:
        return 0.0

    for _ in range(max_iterations):
        mid = (low + high) / 2
        mid_value = npv(mid)

        if abs(mid_value) < tolerance:
            return mid * 100

        if low_value * mid_value < 0:
            high = mid
            high_value = mid_value
        else:
            low = mid
            low_value = mid_value

    return ((low + high) / 2) * 100


def calculate_metrics(financial_details: Dict[str, Any]) -> Dict[str, Any]:
    try:
        scenario = normalize_financial_details(financial_details)

        loan_amount = max(scenario.property_price - scenario.down_payment, 0)
        monthly_payment = calculate_monthly_payment(
            loan_amount=loan_amount,
            annual_rate=scenario.interest_rate,
            years=scenario.loan_term,
        )
        annual_debt_service = monthly_payment * 12

        annual_hoa = scenario.hoa_fees * 12
        annual_other_income = scenario.other_income * 12

        maintenance_cost = scenario.annual_rent_income * (scenario.maintenance_perc / 100)
        capex_cost = scenario.annual_rent_income * (scenario.capex_perc / 100)
        management_cost = scenario.annual_rent_income * (scenario.mgmt_perc / 100)

        operating_expenses = (
            scenario.annual_property_taxes
            + scenario.annual_insurance
            + scenario.annual_utilities
            + annual_hoa
            + maintenance_cost
            + capex_cost
            + management_cost
        )

        effective_gross_income = scenario.annual_rent_income * (1 - scenario.vacancy_perc / 100) + annual_other_income
        noi = effective_gross_income - operating_expenses
        cash_flow = noi - annual_debt_service
        total_cash_invested = scenario.down_payment + scenario.closing_costs + scenario.rehab_costs

        cap_rate = (noi / scenario.property_price) * 100 if scenario.property_price else 0
        cash_on_cash = (cash_flow / total_cash_invested) * 100 if total_cash_invested else 0
        dscr = noi / annual_debt_service if annual_debt_service else 0
        loan_to_value = (loan_amount / scenario.property_price) * 100 if scenario.property_price else 0

        stabilized_noi = noi * ((1 + scenario.annual_growth_rate / 100) ** scenario.hold_years)
        exit_value = stabilized_noi / (scenario.exit_cap_rate / 100) if scenario.exit_cap_rate > 0 else 0
        sale_costs = exit_value * 0.025
        net_sale_proceeds = max(exit_value - sale_costs - loan_amount, 0)

        cash_flows = [-total_cash_invested]
        for year in range(1, scenario.hold_years + 1):
            grown_cash_flow = cash_flow * ((1 + scenario.annual_growth_rate / 100) ** (year - 1))
            if year == scenario.hold_years:
                grown_cash_flow += net_sale_proceeds
            cash_flows.append(grown_cash_flow)

        irr = calculate_irr(cash_flows)
        total_cash_returned = sum(cash_flows[1:])
        equity_multiple = total_cash_returned / total_cash_invested if total_cash_invested else 0

        return {
            "Monthly Payment": round(monthly_payment, 2),
            "Annual Debt Service": round(annual_debt_service, 2),
            "Operating Expenses": round(operating_expenses, 2),
            "Effective Gross Income": round(effective_gross_income, 2),
            "NOI": round(noi, 2),
            "Cash Flow": round(cash_flow, 2),
            "Cap Rate (%)": round(cap_rate, 2),
            "Cash-on-Cash ROI (%)": round(cash_on_cash, 2),
            "DSCR": round(dscr, 2),
            "LTV (%)": round(loan_to_value, 2),
            "IRR (%)": round(irr, 2),
            "Equity Multiple": round(equity_multiple, 2),
            "Loan Amount": round(loan_amount, 2),
            "Total Cash Invested": round(total_cash_invested, 2),
            "Estimated Exit Value": round(exit_value, 2),
            "Net Sale Proceeds": round(net_sale_proceeds, 2),
        }
    except Exception as exc:
        return {"error": str(exc)}


def metrics_to_dataframe(metrics: Dict[str, Any]) -> pd.DataFrame:
    return pd.DataFrame(metrics.items(), columns=["Metric", "Value"])


def ai_assistant(prompt: str) -> str:
    if not prompt or not prompt.strip():
        return "Enter a real estate investment, lease, underwriting, or market question."

    if client is None:
        return "OpenAI runtime unavailable. Configure OPENAI_API_KEY in environment variables or .env."

    system_prompt = (
        "You are VillaTerras AI, a commercial real estate underwriting and advisory assistant. "
        "Focus on CRE analysis, NOI, cap rate, DSCR, LTV, cash flow, lease economics, industrial, retail, multifamily, land, and acquisition strategy. "
        "State assumptions clearly and do not fabricate live market data."
    )

    try:
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt.strip()},
            ],
            temperature=0.35,
            max_tokens=800,
        )
        return response.choices[0].message.content or "No AI response returned."
    except Exception as exc:
        return f"AI Runtime Error: {exc}"


if __name__ == "__main__":
    test_scenario = {
        "property_price": 1000000,
        "down_payment": 250000,
        "closing_costs": 30000,
        "rehab_costs": 50000,
        "annual_rent_income": 120000,
        "annual_property_taxes": 15000,
        "annual_insurance": 4000,
        "annual_utilities": 6000,
        "maintenance_perc": 5,
        "capex_perc": 5,
        "mgmt_perc": 6,
        "vacancy_perc": 5,
        "hoa_fees": 0,
        "other_income": 500,
        "interest_rate": 6.5,
        "loan_term": 30,
    }
    print(calculate_metrics(test_scenario))
