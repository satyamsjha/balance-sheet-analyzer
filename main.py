#!/usr/bin/env python3
"""
Balance Sheet Analyzer - Main Application
Run financial analysis on balance sheet data
"""

from balance_sheet import BalanceSheet
from analyzer import FinancialAnalyzer
from report_generator import ReportGenerator
from data_io import DataIO


def analyze_balance_sheet(balance_sheet: BalanceSheet) -> None:
    """Perform complete analysis on a balance sheet"""

    # Verify balance sheet
    if not balance_sheet.verify_balance():
        print("WARNING: Balance sheet does not balance!")
        print(f"Assets: ${balance_sheet.total_assets:,.2f}")
        print(f"Liabilities + Equity: ${balance_sheet.total_liabilities + balance_sheet.total_equity:,.2f}")
        print()

    # Create analyzer
    analyzer = FinancialAnalyzer(balance_sheet)

    # Generate and print report
    report_gen = ReportGenerator(balance_sheet, analyzer)
    report_gen.print_report()


def main():
    """Main application entry point"""

    # Example 1: Create balance sheet manually
    print("Example 1: Analyzing Sample Company Balance Sheet")
    print()

    sample_bs = BalanceSheet(
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

        # Equity (Total: 1,600,000 to balance with Assets of 4,000,000 - Liabilities of 2,400,000)
        common_stock=1000000,
        retained_earnings=500000,
        other_equity=100000,

        # Metadata
        company_name="Sample Corp",
        date="2024-12-31"
    )

    analyze_balance_sheet(sample_bs)

    # Save sample data to JSON
    DataIO.to_json(sample_bs, 'sample_balance_sheet.json')
    print("\nSample balance sheet saved to: sample_balance_sheet.json")

    # Export to CSV
    DataIO.export_to_csv(sample_bs, 'balance_sheet.csv')
    print("Balance sheet exported to: balance_sheet.csv")

    # Export ratios
    analyzer = FinancialAnalyzer(sample_bs)
    ratios = analyzer.get_all_ratios()
    DataIO.export_ratios_to_csv(ratios, 'financial_ratios.csv')
    print("Financial ratios exported to: financial_ratios.csv")

    # Save report
    report_gen = ReportGenerator(sample_bs, analyzer)
    report_gen.save_report('analysis_report.txt')
    print("Analysis report saved to: analysis_report.txt")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Balance Sheet Analyzer")
    parser.add_argument("--input", help="JSON path to a balance sheet")
    parser.add_argument("--output", default="analysis_report.txt", help="Report output file")
    args = parser.parse_args()

    if args.input:
        # Load from provided file
        bs = DataIO.load(args.input)
        analyzer = FinancialAnalyzer(bs)
        report_gen = ReportGenerator(bs, analyzer)

        # Print to console
        report_gen.print_report()

        # Save to file
        report_gen.save_report(args.output)
        print(f"\nAnalysis report saved to: {args.output}")
    else:
        # Run default example
        main()
