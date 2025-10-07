"""
Financial Ratio Analysis Module
Calculates key financial ratios from balance sheet data
"""

from balance_sheet import BalanceSheet
from typing import Dict


class FinancialAnalyzer:
    """Analyzes balance sheet and calculates financial ratios"""

    def __init__(self, balance_sheet: BalanceSheet):
        self.bs = balance_sheet

    def current_ratio(self) -> float:
        """
        Current Ratio = Current Assets / Current Liabilities
        Measures liquidity - ability to pay short-term obligations
        """
        if self.bs.total_current_liabilities == 0:
            return float('inf')
        return self.bs.total_current_assets / self.bs.total_current_liabilities

    def quick_ratio(self) -> float:
        """
        Quick Ratio = (Current Assets - Inventory) / Current Liabilities
        More conservative liquidity measure (excludes inventory)
        """
        if self.bs.total_current_liabilities == 0:
            return float('inf')
        quick_assets = self.bs.total_current_assets - self.bs.inventory
        return quick_assets / self.bs.total_current_liabilities

    def cash_ratio(self) -> float:
        """
        Cash Ratio = Cash / Current Liabilities
        Most conservative liquidity measure
        """
        if self.bs.total_current_liabilities == 0:
            return float('inf')
        return self.bs.cash / self.bs.total_current_liabilities

    def debt_to_equity_ratio(self) -> float:
        """
        Debt to Equity = Total Liabilities / Total Equity
        Measures financial leverage
        """
        if self.bs.total_equity == 0:
            return float('inf')
        return self.bs.total_liabilities / self.bs.total_equity

    def debt_to_assets_ratio(self) -> float:
        """
        Debt to Assets = Total Liabilities / Total Assets
        Measures proportion of assets financed by debt
        """
        if self.bs.total_assets == 0:
            return 0
        return self.bs.total_liabilities / self.bs.total_assets

    def equity_ratio(self) -> float:
        """
        Equity Ratio = Total Equity / Total Assets
        Measures proportion of assets financed by equity
        """
        if self.bs.total_assets == 0:
            return 0
        return self.bs.total_equity / self.bs.total_assets

    def working_capital(self) -> float:
        """
        Working Capital = Current Assets - Current Liabilities
        Measures short-term financial health
        """
        return self.bs.total_current_assets - self.bs.total_current_liabilities

    def long_term_debt_ratio(self) -> float:
        """
        Long-term Debt Ratio = Long-term Debt / Total Assets
        Measures long-term financial obligations
        """
        if self.bs.total_assets == 0:
            return 0
        return self.bs.total_long_term_liabilities / self.bs.total_assets

    def get_all_ratios(self) -> Dict[str, float]:
        """Calculate and return all financial ratios"""
        return {
            'Current Ratio': self.current_ratio(),
            'Quick Ratio': self.quick_ratio(),
            'Cash Ratio': self.cash_ratio(),
            'Debt to Equity Ratio': self.debt_to_equity_ratio(),
            'Debt to Assets Ratio': self.debt_to_assets_ratio(),
            'Equity Ratio': self.equity_ratio(),
            'Working Capital': self.working_capital(),
            'Long-term Debt Ratio': self.long_term_debt_ratio()
        }

    def interpret_ratio(self, ratio_name: str, value: float) -> str:
        """Provide interpretation of financial ratios"""
        interpretations = {
            'Current Ratio': self._interpret_current_ratio(value),
            'Quick Ratio': self._interpret_quick_ratio(value),
            'Cash Ratio': self._interpret_cash_ratio(value),
            'Debt to Equity Ratio': self._interpret_debt_to_equity(value),
            'Debt to Assets Ratio': self._interpret_debt_to_assets(value),
            'Equity Ratio': self._interpret_equity_ratio(value),
            'Working Capital': self._interpret_working_capital(value),
            'Long-term Debt Ratio': self._interpret_long_term_debt(value)
        }
        return interpretations.get(ratio_name, "No interpretation available")

    def _interpret_current_ratio(self, value: float) -> str:
        if value < 1:
            return "Poor - May struggle to meet short-term obligations"
        elif value < 1.5:
            return "Below Average - Limited liquidity cushion"
        elif value < 2:
            return "Good - Adequate liquidity"
        elif value < 3:
            return "Excellent - Strong liquidity position"
        else:
            return "Very High - May indicate inefficient use of assets"

    def _interpret_quick_ratio(self, value: float) -> str:
        if value < 0.5:
            return "Poor - Liquidity concerns without inventory"
        elif value < 1:
            return "Below Average - Some liquidity risk"
        elif value < 1.5:
            return "Good - Solid liquidity"
        else:
            return "Excellent - Very strong liquidity"

    def _interpret_cash_ratio(self, value: float) -> str:
        if value < 0.2:
            return "Low - Limited immediate cash availability"
        elif value < 0.5:
            return "Moderate - Reasonable cash position"
        else:
            return "High - Strong cash reserves"

    def _interpret_debt_to_equity(self, value: float) -> str:
        if value < 0.5:
            return "Conservative - Low leverage, equity-financed"
        elif value < 1:
            return "Moderate - Balanced leverage"
        elif value < 2:
            return "High - Significant debt leverage"
        else:
            return "Very High - Heavy reliance on debt financing"

    def _interpret_debt_to_assets(self, value: float) -> str:
        if value < 0.3:
            return "Low - Conservative debt levels"
        elif value < 0.5:
            return "Moderate - Balanced capital structure"
        elif value < 0.7:
            return "High - Significant debt burden"
        else:
            return "Very High - Heavy debt load"

    def _interpret_equity_ratio(self, value: float) -> str:
        if value < 0.3:
            return "Low - Heavy reliance on debt"
        elif value < 0.5:
            return "Moderate - Balanced financing"
        elif value < 0.7:
            return "Good - Strong equity base"
        else:
            return "Excellent - Conservative financing"

    def _interpret_working_capital(self, value: float) -> str:
        if value < 0:
            return "Negative - Short-term financial stress"
        elif value < 100000:
            return "Low - Limited working capital buffer"
        elif value < 1000000:
            return "Moderate - Adequate working capital"
        else:
            return "Strong - Healthy working capital position"

    def _interpret_long_term_debt(self, value: float) -> str:
        if value < 0.2:
            return "Low - Minimal long-term debt"
        elif value < 0.4:
            return "Moderate - Reasonable long-term debt"
        else:
            return "High - Significant long-term obligations"
