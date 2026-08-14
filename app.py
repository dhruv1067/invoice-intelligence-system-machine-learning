import streamlit as st
import pandas as pd 
import numpy as np 
import plotly.express as px

from inferencing.predict_freight import predict_freight_cost
from inferencing.predict_invoice_flag import predict_invoice_flag

# ------------------------------------------------------------------
# Page Configuration
# ------------------------------------------------------------------
st.set_page_config(
    page_title="Vendor Invoice Intelligence Portal",
    layout="wide"
)

# ------------------------------------------------------------------
# Header Section
# ------------------------------------------------------------------
st.markdown("""
# Vendor Innvoice Intelligent Portal
### AI-Driven Freight Cost Prediction & Invoice Risk FLagging

This internal analytics portal leverages machine learning to
- **Forcast freight costs accurately**
- **Reduce financial leakage and manual worload**
""")

st.divider()

# -------------------------------------------------------------------
# Sidebar 
# -------------------------------------------------------------------
st.sidebar.title("Model Selection")
selected_model = st.sidebar.radio(
    "Choose Prediction Model",
    [
        "Freight Cost Prediction",
        "Invoice Manual Approval Flag"
    ]
)

st.sidebar.markdown("""
---
**Business Impact**
- Improved cost forecasting
- Reduced invoice fraud & anomalies
- Faster finance operations 
""")

