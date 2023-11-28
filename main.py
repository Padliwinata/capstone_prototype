from datetime import datetime
import requests
import streamlit as st

current_year = datetime.now().year
year_before = current_year - 1

left_column, right_column = st.columns(2)
with left_column:
    st.write(str(current_year))
    account_receivables_1 = int(st.text_input('Account Receivables', '100000', key="a1"))
    sales_1 = int(st.text_input('Sales', '100000', key="a2"))
    cogs_1 = int(st.text_input('Cost of Goods Sales', '150000', key="a3"))
    current_assets_1 = int(st.text_input('Current Assets', '100000', key="a4"))
    ppe_1 = int(st.text_input('Propterty, Plant, and Equipment', '100000', key="a5"))
    depreciation_1 = int(st.text_input('Depreciation', '100000', key="current"))
    sga_expense_1 = int(st.text_input('Selling, General, and Administrative Expenses', '100000', key="a6"))
    long_term_debt_1 = int(st.text_input('Long Term Debt', '100000', key="a7"))
    current_liabilities_1 = int(st.text_input('Current Liabilities', '100000', key="a8"))
    total_asset_1 = int(st.text_input('Total Asset', '100000', key="a9"))
    cash_1 = int(st.text_input('Cash', '100000', key="a10"))
    current_maturities_of_ltd_1 = int(st.text_input('Current Maturities of Long Term Debt', '100000', key="a11"))
    income_tax_payable_1 = int(st.text_input('Income Tax Payable', '100000', key="a12"))
    depreciation_and_amortization_1 = int(st.text_input('Depreciation and Amortization', '100000', key="a13"))

with right_column:
    st.write(str(year_before))
    account_receivables_2 = int(st.text_input('Account Receivables', '200000', key="b1"))
    sales_2 = int(st.text_input('Sales', '200000', key="b2"))
    cogs_2 = int(st.text_input('Cost of Goods Sales', '250000', key="b3"))
    current_assets_2 = int(st.text_input('Current Assets', '200000', key="b4"))
    ppe_2 = int(st.text_input('Propterty, Plant, and Equipment', '200000', key="b5"))
    depreciation_2 = int(st.text_input('Depreciation', '200000', key="currebt"))
    sga_expense_2 = int(st.text_input('Selling, General, and Administrative Expenses', '200000', key="b6"))
    long_term_debt_2 = int(st.text_input('Long Term Debt', '200000', key="b7"))
    current_liabilities_2 = int(st.text_input('Current Liabilities', '200000', key="b8"))
    total_asset_2 = int(st.text_input('Total Asset', '200000', key="b9"))
    cash_2 = int(st.text_input('Cash', '200000', key="b10"))
    current_maturities_of_ltd_2 = int(st.text_input('Current Maturities of Long Term Debt', '200000', key="b11"))
    income_tax_payable_2 = int(st.text_input('Income Tax Payable', '200000', key="b12"))
    depreciation_and_amortization_2 = int(st.text_input('Depreciation and Amortization', '200000', key="b13"))

data = {
    "account_receivables_1": account_receivables_1,
    "sales_1": sales_1,
    "cogs_1": cogs_1,
    "current_assets_1": current_assets_1,
    "ppe_1": ppe_1,
    "depreciation_1": depreciation_1,
    "sga_expense_1": sga_expense_1,
    "long_term_debt_1": long_term_debt_1,
    "current_liabilities_1": current_liabilities_1,
    "total_asset_1": total_asset_1,
    "cash_1": cash_1,
    "current_maturities_of_ltd_1": current_maturities_of_ltd_1,
    "income_tax_payable_1": income_tax_payable_1,
    "depreciation_and_amortization_1": depreciation_and_amortization_1,
    "account_receivables_2": account_receivables_2,
    "sales_2": sales_2,
    "cogs_2": cogs_2,
    "current_assets_2": current_assets_2,
    "ppe_2": ppe_2,
    "depreciation_2": depreciation_2,
    "sga_expense_2": sga_expense_2,
    "long_term_debt_2": long_term_debt_2,
    "current_liabilities_2": current_liabilities_2,
    "total_asset_2": total_asset_2,
    "cash_2": cash_2,
    "current_maturities_of_ltd_2": current_maturities_of_ltd_2,
    "income_tax_payable_2": income_tax_payable_2,
    "depreciation_and_amortization_2": depreciation_and_amortization_2
}

example_data = {
    "account_receivables_1": account_receivables_1,
    "sales_1": sales_1,
    "cogs_1": cogs_1,
    "current_assets_1": current_assets_1,
    "ppe_1": ppe_1,
    "depreciation_1": depreciation_1,
    "sga_expense_1": sga_expense_1,
    "long_term_debt_1": long_term_debt_1,
    "current_liabilities_1": current_liabilities_1,
    "total_asset_1": total_asset_1,
    "cash_1": cash_1,
    "current_maturities_of_ltd_1": current_maturities_of_ltd_1,
    "income_tax_payable_1": income_tax_payable_1,
    "depreciation_and_amortization_1": depreciation_and_amortization_1,
    "account_receivables_2": account_receivables_2,
    "sales_2": sales_2,
    "cogs_2": cogs_2,
    "current_assets_2": current_assets_2,
    "ppe_2": ppe_2,
    "depreciation_2": depreciation_2,
    "sga_expense_2": sga_expense_2,
    "long_term_debt_2": long_term_debt_2,
    "current_liabilities_2": current_liabilities_2,
    "total_asset_2": total_asset_2,
    "cash_2": cash_2,
    "current_maturities_of_ltd_2": current_maturities_of_ltd_2,
    "income_tax_payable_2": income_tax_payable_2,
    "depreciation_and_amortization_2": depreciation_and_amortization_2
}

res = requests.post('https://fraud_detection-1-d1112249.deta.app/index', json=example_data)
st.write(f"M score: {res.text}")