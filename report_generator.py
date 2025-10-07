"""
Report Generation Module
Creates formatted analysis reports
"""

from balance_sheet import BalanceSheet
from analyzer import FinancialAnalyzer
from typing import Dict
from datetime import datetime


class ReportGenerator:
    """Generates financial analysis reports"""

    def __init__(self, balance_sheet: BalanceSheet, analyzer: FinancialAnalyzer):
        self.bs = balance_sheet
        self.analyzer = analyzer

    def generate_text_report(self) -> str:
        """Generate a comprehensive text report"""
        report = []
        report.append("=" * 80)
        report.append(f"BALANCE SHEET FINANCIAL ANALYSIS REPORT")
        report.append("=" * 80)
        report.append(f"\nCompany: {self.bs.company_name}")
        report.append(f"Date: {self.bs.date}")
        report.append(f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("\n" + "-" * 80)

        # Balance Sheet Summary
        report.append("\nBALANCE SHEET SUMMARY")
        report.append("-" * 80)
        report.append(f"\nASSETS:")
        report.append(f"  Current Assets:           ${self.bs.total_current_assets:,.2f}")
        report.append(f"  Long-term Assets:         ${self.bs.total_long_term_assets:,.2f}")
        report.append(f"  TOTAL ASSETS:             ${self.bs.total_assets:,.2f}")

        report.append(f"\nLIABILITIES:")
        report.append(f"  Current Liabilities:      ${self.bs.total_current_liabilities:,.2f}")
        report.append(f"  Long-term Liabilities:    ${self.bs.total_long_term_liabilities:,.2f}")
        report.append(f"  TOTAL LIABILITIES:        ${self.bs.total_liabilities:,.2f}")

        report.append(f"\nEQUITY:")
        report.append(f"  Total Equity:             ${self.bs.total_equity:,.2f}")

        # Balance Verification
        balanced = self.bs.verify_balance()
        status = "✓ BALANCED" if balanced else "✗ NOT BALANCED"
        report.append(f"\nBalance Sheet Status: {status}")

        # Financial Ratios
        report.append("\n" + "-" * 80)
        report.append("\nFINANCIAL RATIOS & ANALYSIS")
        report.append("-" * 80)

        ratios = self.analyzer.get_all_ratios()

        report.append("\nLIQUIDITY RATIOS:")
        report.append("-" * 40)
        for ratio_name in ['Current Ratio', 'Quick Ratio', 'Cash Ratio', 'Working Capital']:
            value = ratios[ratio_name]
            interpretation = self.analyzer.interpret_ratio(ratio_name, value)
            if ratio_name == 'Working Capital':
                report.append(f"  {ratio_name:25} ${value:,.2f}")
            else:
                report.append(f"  {ratio_name:25} {value:.2f}")
            report.append(f"    → {interpretation}")

        report.append("\nLEVERAGE RATIOS:")
        report.append("-" * 40)
        for ratio_name in ['Debt to Equity Ratio', 'Debt to Assets Ratio', 'Equity Ratio', 'Long-term Debt Ratio']:
            value = ratios[ratio_name]
            interpretation = self.analyzer.interpret_ratio(ratio_name, value)
            report.append(f"  {ratio_name:25} {value:.2f}")
            report.append(f"    → {interpretation}")

        # Key Insights
        report.append("\n" + "-" * 80)
        report.append("\nKEY INSIGHTS")
        report.append("-" * 80)
        insights = self._generate_insights(ratios)
        for insight in insights:
            report.append(f"  • {insight}")

        report.append("\n" + "=" * 80)

        return "\n".join(report)

    def _generate_insights(self, ratios: Dict[str, float]) -> list:
        """Generate key insights based on ratios"""
        insights = []

        # Liquidity insights
        if ratios['Current Ratio'] < 1:
            insights.append("WARNING: Current ratio below 1 indicates potential liquidity issues")
        elif ratios['Current Ratio'] > 3:
            insights.append("High current ratio may indicate underutilized assets")

        # Leverage insights
        if ratios['Debt to Equity Ratio'] > 2:
            insights.append("High debt-to-equity ratio suggests significant financial leverage and risk")
        elif ratios['Debt to Equity Ratio'] < 0.5:
            insights.append("Conservative capital structure with low debt levels")

        # Working capital insights
        if ratios['Working Capital'] < 0:
            insights.append("CRITICAL: Negative working capital - immediate attention needed")
        elif ratios['Working Capital'] > 0:
            insights.append(f"Positive working capital of ${ratios['Working Capital']:,.2f} provides financial cushion")

        # Quick ratio insights
        if ratios['Quick Ratio'] < 1:
            insights.append("Quick ratio below 1 indicates potential challenges meeting short-term obligations")

        # Asset composition
        equity_ratio = ratios['Equity Ratio']
        if equity_ratio > 0.7:
            insights.append("Strong equity position provides financial stability")
        elif equity_ratio < 0.3:
            insights.append("Heavy reliance on debt financing increases financial risk")

        return insights

    def save_report(self, file_path: str) -> None:
        """Save the report to a text file"""
        report = self.generate_text_report()
        with open(file_path, 'w') as f:
            f.write(report)

    def print_report(self) -> None:
        """Print the report to console"""
        print(self.generate_text_report())
