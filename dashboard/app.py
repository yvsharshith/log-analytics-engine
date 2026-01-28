# pip install streamlit plotly
# streamlit : Python framework for building web apps for data science and machine learning
# plotly : Interactive graphing library
# app.py is independent from main.py
# It reads processed logs and visualizes them in a dashboard

import sys
import os
import streamlit as st
import plotly.express as px

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)

from processing.pipeline import build_pipeline
from anomaly.detector import detect_anomaly

LOG_FILE = os.path.join(PROJECT_ROOT, "log_generator", "realtime_logs.csv")

st.title("Python Based High Throughput Log Analytics Monitoring Engine")

log_df = build_pipeline(LOG_FILE)
anomaly_df = detect_anomaly(log_df)

st.subheader("Anomalies Detected in Logs")

if anomaly_df.empty:
    st.warning("No anomalies detected in the logs.")
    st.stop()

fig = px.line(
    anomaly_df,
    x="timestamp",
    y="anomaly_score",
    title="Anomaly Scores Over Time"
)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Anomalous Log Entries")
st.dataframe(anomaly_df, use_container_width=True)

st.subheader("Filter Anomalies")

threshold = st.slider(
    "Anomaly Score Threshold",
    min_value=0.0,
    max_value=1.0,
    value=0.5,
    step=0.01
)

filtered_anomalies = anomaly_df[anomaly_df["anomaly_score"] >= threshold]

st.dataframe(filtered_anomalies, use_container_width=True)