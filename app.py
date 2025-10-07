import streamlit as st
from data_io import DataIO
from analyzer import FinancialAnalyzer
from report_generator import ReportGenerator

st.title("Balance Sheet Analyzer")

uploaded = st.file_uploader("Upload your balance sheet (JSON or CSV)")
if uploaded:
    bs = DataIO.load(uploaded)
    analyzer = FinancialAnalyzer(bs)
    report = ReportGenerator(bs, analyzer)
    st.text(report.generate_text_report())
