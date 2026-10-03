# Five tier real estate waterfall

The Python module allocates available deal cash to LP and GP investors in this order: proportional repayment of unreturned capital, accrued LP preferred return, optional GP catch-up, the 12% IRR / 1.5x tier, the 15% IRR / 2.0x tier, and the residual split. Both IRR and equity multiple must be met before cash advances past a hurdle tier. The GP catch-up is a separate bridge between the preferred tier and the later promote tiers.

The input is a JSON file containing dated LP contributions, GP contributions, and distributable cash. Dates must be unique ISO dates. Contributions and cash cannot be negative. Enter cash after debt service, fees, taxes, and reserves as appropriate for the governing agreement. The example is illustrative and does not define a specific transaction's legal terms.

```bash
python -m pip install 'openpyxl>=3.1,<4'
python -m unittest discover -s calculators/waterfall -p 'test_*.py' -v
python calculators/waterfall/waterfall.py --input calculators/waterfall/example_deal.json --output-dir output
```

The GitHub workflow runs at minute 17 each hour in UTC, can run manually, and tests pull requests that affect this module. Each completed run offers a JSON result and Excel workbook under its Actions artifacts. It does not commit generated reports to the repository. Replace the example JSON with deal inputs to calculate another partnership.
