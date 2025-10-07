# Balance Sheet Financial Analysis Tool

A Python automation tool for analyzing company balance sheets and calculating key financial ratios.

## Features

- **Balance Sheet Data Model**: Structured representation of assets, liabilities, and equity
- **Financial Ratio Calculations**:
  - Liquidity ratios (Current, Quick, Cash)
  - Leverage ratios (Debt-to-Equity, Debt-to-Assets)
  - Working Capital analysis
- **Automated Interpretations**: AI-powered insights for each financial metric
- **Multiple Export Formats**: JSON, CSV, and text reports
- **Balance Verification**: Ensures Assets = Liabilities + Equity

## Installation

No external dependencies required - uses Python standard library only.

```bash
cd balance_sheet_analyzer
python main.py
```

## Usage

### Quick Start

Run the example:
```bash
python main.py
```

### Load from JSON

```python
from data_io import DataIO
from analyzer import FinancialAnalyzer
from report_generator import ReportGenerator

# Load balance sheet
bs = DataIO.from_json('sample_balance_sheet.json')

# Analyze
analyzer = FinancialAnalyzer(bs)
ratios = analyzer.get_all_ratios()

# Generate report
report = ReportGenerator(bs, analyzer)
report.print_report()
```

### Create Custom Balance Sheet

```python
from balance_sheet import BalanceSheet

bs = BalanceSheet(
    # Assets
    cash=500000,
    accounts_receivable=300000,
    inventory=400000,
    other_current_assets=100000,
    property_plant_equipment=2000000,
    intangible_assets=500000,
    other_long_term_assets=200000,

    # Liabilities
    accounts_payable=250000,
    short_term_debt=200000,
    other_current_liabilities=150000,
    long_term_debt=1500000,
    other_long_term_liabilities=300000,

    # Equity
    common_stock=1000000,
    retained_earnings=600000,
    other_equity=100000,

    company_name="Your Company",
    date="2024-12-31"
)
```

## Financial Ratios Calculated

### Liquidity Ratios
- **Current Ratio**: Current Assets / Current Liabilities
- **Quick Ratio**: (Current Assets - Inventory) / Current Liabilities
- **Cash Ratio**: Cash / Current Liabilities
- **Working Capital**: Current Assets - Current Liabilities

### Leverage Ratios
- **Debt to Equity**: Total Liabilities / Total Equity
- **Debt to Assets**: Total Liabilities / Total Assets
- **Equity Ratio**: Total Equity / Total Assets
- **Long-term Debt Ratio**: Long-term Debt / Total Assets

## File Structure

```
balance_sheet_analyzer/
├── balance_sheet.py      # Data model
├── analyzer.py           # Financial ratio calculations
├── data_io.py           # Import/export functionality
├── report_generator.py  # Report generation
├── main.py              # Example usage
└── README.md            # Documentation
```

## Example Output

The tool generates comprehensive reports including:
- Balance sheet summary
- All financial ratios with interpretations
- Key insights and warnings
- Export to CSV and text formats

## License

MIT License
