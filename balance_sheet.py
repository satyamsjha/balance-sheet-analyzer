"""
Balance Sheet Financial Analysis Tool
Analyzes balance sheet data and calculates key financial ratios
"""

from dataclasses import dataclass
from typing import Dict, Optional
import json
from datetime import datetime


@dataclass
class BalanceSheet:
    """Represents a company's balance sheet"""

    # Assets
    cash: float
    accounts_receivable: float
    inventory: float
    other_current_assets: float
    property_plant_equipment: float
    intangible_assets: float
    other_long_term_assets: float

    # Liabilities
    accounts_payable: float
    short_term_debt: float
    other_current_liabilities: float
    long_term_debt: float
    other_long_term_liabilities: float

    # Equity
    common_stock: float
    retained_earnings: float
    other_equity: float

    # Metadata
    company_name: str
    date: str

    @property
    def total_current_assets(self) -> float:
        """Calculate total current assets"""
        return (self.cash + self.accounts_receivable +
                self.inventory + self.other_current_assets)

    @property
    def total_long_term_assets(self) -> float:
        """Calculate total long-term assets"""
        return (self.property_plant_equipment +
                self.intangible_assets + self.other_long_term_assets)

    @property
    def total_assets(self) -> float:
        """Calculate total assets"""
        return self.total_current_assets + self.total_long_term_assets

    @property
    def total_current_liabilities(self) -> float:
        """Calculate total current liabilities"""
        return (self.accounts_payable + self.short_term_debt +
                self.other_current_liabilities)

    @property
    def total_long_term_liabilities(self) -> float:
        """Calculate total long-term liabilities"""
        return self.long_term_debt + self.other_long_term_liabilities

    @property
    def total_liabilities(self) -> float:
        """Calculate total liabilities"""
        return self.total_current_liabilities + self.total_long_term_liabilities

    @property
    def total_equity(self) -> float:
        """Calculate total equity"""
        return self.common_stock + self.retained_earnings + self.other_equity

    def verify_balance(self) -> bool:
        """Verify that Assets = Liabilities + Equity"""
        total_liabilities_equity = self.total_liabilities + self.total_equity
        return abs(self.total_assets - total_liabilities_equity) < 0.01
