import streamlit as st
import pandas as pd
import plotly.express as px

from utils.security import PIIRedactor
from engine.parser import DocumentParser
from engine.categorizer import SemanticCategorizer
from engine.anomaly_detector import AnomalyDetector
from engine.optimizer import OptimizerIntelligence

st.set_page_config(page_title="FinTracker AI Dashboard", layout="wide", page_icon="💸")

# Theming and Layout
st.title("🛡️ FinTracker Executive Agent Dashboard")
st.markdown("##### Real-Time Anomaly Detection & Spend Optimization Pipeline")

@st.cache_resource
def init_agent():
    return PIIRedactor(), DocumentParser(), SemanticCategorizer(), AnomalyDetector(), OptimizerIntelligence()

redactor, parser, categorizer, anomaly_detector, optimizer = init_agent()

# Data Gateway (Moved to Main Dashboard)
with st.container(border=True):
    st.subheader("📤 Data Gateway")
    st.markdown("Securely upload transactional data (`.pdf`, `.csv`, `.xlsx`). All data is passed through the PII redactor automatically.")
    uploaded_file = st.file_uploader("Upload Receipts/Ledger", type=["csv", "xlsx", "pdf"], label_visibility="collapsed")

if uploaded_file is not None:
    file_ext = uploaded_file.name.split('.')[-1].lower()
    try:
        raw_df = parser.parse(uploaded_file, file_ext)
    except Exception as e:
        st.error(f"Ingestion Module Failure: {e}")
        st.stop()
        
    if raw_df.empty:
        st.warning("No tabular vectors could be extracted by the Data Gateway.")
        st.stop()

    with st.spinner("Agentic pipeline actively processing dataset..."):
        secure_df = redactor.redact_dataframe(raw_df)
        cat_df = categorizer.categorize(secure_df)
        analyzed_df = anomaly_detector.flag_anomalies(cat_df)
        roadmap = optimizer.generate_roadmap(analyzed_df)

    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    c1.metric("Gross Capital Output", f"${roadmap['Total Spend']:,.2f}")
    c2.metric("Identified Capital Leakage", f"${roadmap['Leakage Amount']:,.2f}")
    
    score = roadmap['Leakage Score']
    delta_color = "normal" if score < 25 else "off" if score < 60 else "inverse"
    c3.metric("Platform Leakage Score (0-100)", f"{score}", delta=f"{'Critical' if score > 60 else 'Stable'}", delta_color=delta_color)

    st.markdown("---")
    r1c1, r1c2 = st.columns(2)

    with r1c1:
        st.subheader("Categorical Synthesis")
        cat_sum = analyzed_df.groupby('category', as_index=False)['transaction_amount'].sum()
        if not cat_sum.empty:
            fig = px.pie(cat_sum, values='transaction_amount', names='category', 
                         hole=0.45, color_discrete_sequence=px.colors.sequential.Electric)
            fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
            st.plotly_chart(fig, use_container_width=True)

    with r1c2:
        st.subheader("Agentic Cost Reduction Roadmap")
        for rec in roadmap['Recommendations']:
            st.info(rec)

    st.markdown("---")
    st.subheader("🚨 Detected Anomaly Feed")
    anomalies = analyzed_df[analyzed_df['is_anomaly'] == True]
    if not anomalies.empty:
        # Displaying with highlighting equivalent logic
        st.dataframe(anomalies[['transaction_date', 'merchant', 'transaction_amount', 'category', 'anomaly_reason']], use_container_width=True)
    else:
        st.success("Verification check passed: Minimal anomaly footprints detected.")

    st.markdown("---")
    st.subheader("Secure Master Ledger Context (PII Stripped)")
    st.dataframe(analyzed_df, use_container_width=True)

    st.markdown("### Export Phase")
    csv_out = analyzed_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download CFO Summary Report",
        data=csv_out,
        file_name='cfo_fintracker_redacted_export.csv',
        mime='text/csv'
    )
else:
    st.info("👋 Welcome to FinTracker! Please upload a financial document above to initialize the agentic pipeline.")

# Styled Footer (Always displayed)
st.markdown("---")
footer_col1, footer_col2, footer_col3 = st.columns([1, 2, 1])
with footer_col2:
    st.markdown(
        "<div style='text-align: center; color: grey; font-size: 0.8rem;'>"
        "FinTracker created by <b>Mywish Anand</b><br>"
        "<a href='https://github.com/MywishAnand/' target='_blank' style='text-decoration: none;'>"
        "<img src='https://img.shields.io/badge/GitHub-MywishAnand-black?logo=github' style='margin-top: 5px;'>"
        "</a>"
        "</div>",
        unsafe_allow_html=True
    )
