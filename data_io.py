"""
Data Input/Output Module
Handles loading and saving balance sheet data
"""

import json
import csv
from typing import Dict, List
from balance_sheet import BalanceSheet


class DataIO:
    """Handles data import/export for balance sheets"""

    @staticmethod
    def from_json(file_path: str) -> BalanceSheet:
        """Load balance sheet from JSON file"""
        with open(file_path, 'r') as f:
            data = json.load(f)
        return BalanceSheet(**data)

    @staticmethod
    def to_json(balance_sheet: BalanceSheet, file_path: str) -> None:
        """Save balance sheet to JSON file"""
        data = {
            'cash': balance_sheet.cash,
            'accounts_receivable': balance_sheet.accounts_receivable,
            'inventory': balance_sheet.inventory,
            'other_current_assets': balance_sheet.other_current_assets,
            'property_plant_equipment': balance_sheet.property_plant_equipment,
            'intangible_assets': balance_sheet.intangible_assets,
            'other_long_term_assets': balance_sheet.other_long_term_assets,
            'accounts_payable': balance_sheet.accounts_payable,
            'short_term_debt': balance_sheet.short_term_debt,
            'other_current_liabilities': balance_sheet.other_current_liabilities,
            'long_term_debt': balance_sheet.long_term_debt,
            'other_long_term_liabilities': balance_sheet.other_long_term_liabilities,
            'common_stock': balance_sheet.common_stock,
            'retained_earnings': balance_sheet.retained_earnings,
            'other_equity': balance_sheet.other_equity,
            'company_name': balance_sheet.company_name,
            'date': balance_sheet.date
        }
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)

    @staticmethod
    def from_dict(data: Dict) -> BalanceSheet:
        """Create balance sheet from dictionary"""
        return BalanceSheet(**data)

    @staticmethod
    def export_to_csv(balance_sheet: BalanceSheet, file_path: str) -> None:
        """Export balance sheet to CSV format"""
        rows = [
            ['Category', 'Item', 'Amount'],
            ['ASSETS', '', ''],
            ['Current Assets', 'Cash', balance_sheet.cash],
            ['Current Assets', 'Accounts Receivable', balance_sheet.accounts_receivable],
            ['Current Assets', 'Inventory', balance_sheet.inventory],
            ['Current Assets', 'Other Current Assets', balance_sheet.other_current_assets],
            ['Current Assets', 'Total Current Assets', balance_sheet.total_current_assets],
            ['', '', ''],
            ['Long-term Assets', 'Property, Plant & Equipment', balance_sheet.property_plant_equipment],
            ['Long-term Assets', 'Intangible Assets', balance_sheet.intangible_assets],
            ['Long-term Assets', 'Other Long-term Assets', balance_sheet.other_long_term_assets],
            ['Long-term Assets', 'Total Long-term Assets', balance_sheet.total_long_term_assets],
            ['', '', ''],
            ['TOTAL ASSETS', '', balance_sheet.total_assets],
            ['', '', ''],
            ['LIABILITIES', '', ''],
            ['Current Liabilities', 'Accounts Payable', balance_sheet.accounts_payable],
            ['Current Liabilities', 'Short-term Debt', balance_sheet.short_term_debt],
            ['Current Liabilities', 'Other Current Liabilities', balance_sheet.other_current_liabilities],
            ['Current Liabilities', 'Total Current Liabilities', balance_sheet.total_current_liabilities],
            ['', '', ''],
            ['Long-term Liabilities', 'Long-term Debt', balance_sheet.long_term_debt],
            ['Long-term Liabilities', 'Other Long-term Liabilities', balance_sheet.other_long_term_liabilities],
            ['Long-term Liabilities', 'Total Long-term Liabilities', balance_sheet.total_long_term_liabilities],
            ['', '', ''],
            ['TOTAL LIABILITIES', '', balance_sheet.total_liabilities],
            ['', '', ''],
            ['EQUITY', '', ''],
            ['Equity', 'Common Stock', balance_sheet.common_stock],
            ['Equity', 'Retained Earnings', balance_sheet.retained_earnings],
            ['Equity', 'Other Equity', balance_sheet.other_equity],
            ['Equity', 'Total Equity', balance_sheet.total_equity],
            ['', '', ''],
            ['TOTAL LIABILITIES & EQUITY', '', balance_sheet.total_liabilities + balance_sheet.total_equity],
        ]

        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)

    @staticmethod
    def export_ratios_to_csv(ratios: Dict[str, float], file_path: str) -> None:
        """Export financial ratios to CSV"""
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Ratio', 'Value'])
            for ratio_name, value in ratios.items():
                writer.writerow([ratio_name, f"{value:.2f}"])
