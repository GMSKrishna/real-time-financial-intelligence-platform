import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="Real-Time Financial Intelligence Platform",
    layout="wide"
)

st.title("📊 Real-Time Financial Intelligence Dashboard")

st.markdown("Live crypto analytics with ETL pipeline and FastAPI backend")

# -----------------------------
# Fetch Latest Data
# -----------------------------

latest_response = requests.get(
    "http://127.0.0.1:8000/latest-data"
)

latest_data = latest_response.json()

latest_df = pd.DataFrame(latest_data)

# -----------------------------
# Fetch Top Movers
# -----------------------------

movers_response = requests.get(
    "http://127.0.0.1:8000/top-movers"
)

movers_data = movers_response.json()

movers_df = pd.DataFrame(movers_data)

# -----------------------------
# Dashboard Layout
# -----------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("📈 Latest Market Data")

    st.dataframe(
        latest_df[['symbol', 'price', 'price_change_percent']]
    )

with col2:

    st.subheader("🚀 Top Movers")

    st.dataframe(
        movers_df[['symbol', 'price_change_percent']]
    )

# -----------------------------
# Price Visualization
# -----------------------------

st.subheader("📉 Price Trend Visualization")

chart_df = latest_df.head(20)

st.line_chart(chart_df['price'])

# -----------------------------
# Metrics
# -----------------------------

st.subheader("📌 Platform Metrics")

metric1, metric2, metric3 = st.columns(3)

metric1.metric(
    "Total Records",
    len(latest_df)
)

metric2.metric(
    "Highest Price",
    round(latest_df['price'].max(), 2)
)

metric3.metric(
    "Average Change %",
    round(
        latest_df['price_change_percent'].mean(),
        2
    )
)