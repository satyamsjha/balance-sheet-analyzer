import sys
sys.path.insert(0, '..')

from balance_sheet import BalanceSheet


def test_assets_balance():
    """Test that assets equal liabilities + equity for a balanced sheet"""
    bs = BalanceSheet(
        cash=100,
        accounts_receivable=0,
        inventory=0,
        other_current_assets=0,
        property_plant_equipment=0,
        intangible_assets=0,
        other_long_term_assets=0,
        accounts_payable=0,
        short_term_debt=0,
        other_current_liabilities=0,
        long_term_debt=0,
        other_long_term_liabilities=0,
        common_stock=50,
        retained_earnings=50,
        other_equity=0,
        company_name="TestCo",
        date="2025-01-01"
    )
    assert abs(bs.total_assets - (bs.total_liabilities + bs.total_equity)) < 1e-6


def test_current_assets():
    """Test current assets calculation"""
    bs = BalanceSheet(
        cash=100,
        accounts_receivable=200,
        inventory=150,
        other_current_assets=50,
        property_plant_equipment=0,
        intangible_assets=0,
        other_long_term_assets=0,
        accounts_payable=0,
        short_term_debt=0,
        other_current_liabilities=0,
        long_term_debt=0,
        other_long_term_liabilities=0,
        common_stock=300,
        retained_earnings=200,
        other_equity=0,
        company_name="TestCo",
        date="2025-01-01"
    )
    assert bs.total_current_assets == 500


def test_verify_balance():
    """Test balance sheet verification"""
    bs = BalanceSheet(
        cash=1000,
        accounts_receivable=0,
        inventory=0,
        other_current_assets=0,
        property_plant_equipment=0,
        intangible_assets=0,
        other_long_term_assets=0,
        accounts_payable=0,
        short_term_debt=0,
        other_current_liabilities=0,
        long_term_debt=0,
        other_long_term_liabilities=0,
        common_stock=1000,
        retained_earnings=0,
        other_equity=0,
        company_name="TestCo",
        date="2025-01-01"
    )
    assert bs.verify_balance() is True
