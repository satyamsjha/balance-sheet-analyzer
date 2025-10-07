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

    @staticmethod
    def load(path_or_file) -> BalanceSheet:
        """Load balance sheet from file path or UploadedFile (auto-detects JSON or CSV)"""
        # Read JSON from path or UploadedFile
        if isinstance(path_or_file, str):
            if path_or_file.lower().endswith(".json"):
                with open(path_or_file, 'r') as f:
                    data = json.load(f)
            elif path_or_file.lower().endswith(".csv"):
                raise NotImplementedError("CSV import not yet implemented. Use JSON format.")
            else:
                raise ValueError("Unsupported file type. Use .json")
        elif hasattr(path_or_file, "name"):
            filename = path_or_file.name.lower()
            if filename.endswith(".json"):
                data = json.load(path_or_file)
            elif filename.endswith(".csv"):
                raise NotImplementedError("CSV import not yet implemented. Use JSON format.")
            else:
                raise ValueError("Unsupported uploaded file format. Please upload a JSON file.")
        else:
            raise TypeError("Expected file path or UploadedFile object.")

        # Normalize top-level keys to match BalanceSheet constructor
        alias_map = {
            "as_of_date": "date",
            "asOfDate": "date",
            "companyName": "company_name",
        }
        for old, new in alias_map.items():
            if old in data and new not in data:
                data[new] = data.pop(old)

        # Handle nested structure (if JSON has assets/liabilities/equity objects)
        if "assets" in data or "liabilities" in data or "equity" in data:
            flat_data = {}

            # Extract metadata
            flat_data["company_name"] = data.get("company_name", "Unknown Company")
            flat_data["date"] = data.get("date", "")

            # Flatten assets - try both nested and flat structures
            if "assets" in data:
                assets = data["assets"]
                # If assets is a dict with current/long_term
                if isinstance(assets, dict):
                    if "current" in assets:
                        current = assets["current"]
                        flat_data["cash"] = current.get("cash", 0)
                        flat_data["accounts_receivable"] = current.get("accounts_receivable", 0)
                        flat_data["inventory"] = current.get("inventory", 0)
                        flat_data["other_current_assets"] = current.get("other_current_assets", 0)
                    else:
                        # Try flat structure within assets
                        flat_data["cash"] = assets.get("cash", 0)
                        flat_data["accounts_receivable"] = assets.get("accounts_receivable", 0)
                        flat_data["inventory"] = assets.get("inventory", 0)
                        flat_data["other_current_assets"] = assets.get("other_current_assets", 0)
                        flat_data["property_plant_equipment"] = assets.get("property_plant_equipment", 0)
                        flat_data["intangible_assets"] = assets.get("intangible_assets", 0)
                        flat_data["other_long_term_assets"] = assets.get("other_long_term_assets", 0)

                    if "long_term" in assets:
                        long_term = assets["long_term"]
                        flat_data["property_plant_equipment"] = long_term.get("property_plant_equipment", 0)
                        flat_data["intangible_assets"] = long_term.get("intangible_assets", 0)
                        flat_data["other_long_term_assets"] = long_term.get("other_long_term_assets", 0)

            # Flatten liabilities
            if "liabilities" in data:
                liabilities = data["liabilities"]
                if isinstance(liabilities, dict):
                    if "current" in liabilities:
                        current = liabilities["current"]
                        flat_data["accounts_payable"] = current.get("accounts_payable", 0)
                        flat_data["short_term_debt"] = current.get("short_term_debt", 0)
                        flat_data["other_current_liabilities"] = current.get("other_current_liabilities", 0)
                    else:
                        flat_data["accounts_payable"] = liabilities.get("accounts_payable", 0)
                        flat_data["short_term_debt"] = liabilities.get("short_term_debt", 0)
                        flat_data["other_current_liabilities"] = liabilities.get("other_current_liabilities", 0)
                        flat_data["long_term_debt"] = liabilities.get("long_term_debt", 0)
                        flat_data["other_long_term_liabilities"] = liabilities.get("other_long_term_liabilities", 0)

                    if "long_term" in liabilities:
                        long_term = liabilities["long_term"]
                        flat_data["long_term_debt"] = long_term.get("long_term_debt", 0)
                        flat_data["other_long_term_liabilities"] = long_term.get("other_long_term_liabilities", 0)

            # Flatten equity
            if "equity" in data:
                equity = data["equity"]
                if isinstance(equity, dict):
                    flat_data["common_stock"] = equity.get("common_stock", 0)
                    flat_data["retained_earnings"] = equity.get("retained_earnings", 0)
                    flat_data["other_equity"] = equity.get("other_equity", 0)

            # Fill in any missing required fields with 0
            required_fields = [
                'cash', 'accounts_receivable', 'inventory', 'other_current_assets',
                'property_plant_equipment', 'intangible_assets', 'other_long_term_assets',
                'accounts_payable', 'short_term_debt', 'other_current_liabilities',
                'long_term_debt', 'other_long_term_liabilities',
                'common_stock', 'retained_earnings', 'other_equity'
            ]
            for field in required_fields:
                if field not in flat_data:
                    flat_data[field] = 0

            data = flat_data

        return BalanceSheet(**data)
