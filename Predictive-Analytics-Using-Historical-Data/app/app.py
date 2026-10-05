import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os


# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Predictive Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)


# ---------------------------------------------------
# Load Data and Model
# ---------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "retail_sales_historical.csv"
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "predictive_model.pkl"
)

FORECAST_PATH = os.path.join(
    BASE_DIR,
    "data",
    "future_sales_forecast.csv"
)


@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    df["Date"] = pd.to_datetime(df["Date"])
    return df


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


df = load_data()
model = load_model()


# ---------------------------------------------------
# Title
# ---------------------------------------------------

st.title("📊 Predictive Analytics Dashboard")

st.markdown(
    """
    ### Predictive Analytics Using Historical Retail Sales Data

    This dashboard uses historical sales data and a trained machine
    learning model to analyze sales trends and generate future sales forecasts.
    """
)


# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

st.sidebar.header("Dashboard Controls")

selected_product = st.sidebar.selectbox(
    "Select Product",
    ["All Products"] + sorted(df["Product"].unique().tolist())
)


# ---------------------------------------------------
# Filter Data
# ---------------------------------------------------

if selected_product == "All Products":
    filtered_df = df.copy()
else:
    filtered_df = df[df["Product"] == selected_product].copy()


# ---------------------------------------------------
# KPI Section
# ---------------------------------------------------

total_sales = filtered_df["Sales"].sum()
total_units = filtered_df["Units_Sold"].sum()
average_sales = filtered_df["Sales"].mean()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Sales",
        f"₹{total_sales:,.2f}"
    )

with col2:
    st.metric(
        "Total Units Sold",
        f"{total_units:,}"
    )

with col3:
    st.metric(
        "Average Daily Sales",
        f"₹{average_sales:,.2f}"
    )


st.divider()


# ---------------------------------------------------
# Historical Sales Trend
# ---------------------------------------------------

st.subheader("📈 Historical Sales Trend")

daily_sales = (
    filtered_df.groupby("Date")["Sales"]
    .sum()
    .reset_index()
)

daily_sales = daily_sales.sort_values("Date")

st.line_chart(
    daily_sales.set_index("Date")["Sales"]
)


# ---------------------------------------------------
# Monthly Sales
# ---------------------------------------------------

st.subheader("📅 Monthly Sales")

monthly_sales = (
    filtered_df.set_index("Date")
    .resample("ME")["Sales"]
    .sum()
)

st.bar_chart(monthly_sales)


# ---------------------------------------------------
# Product Performance
# ---------------------------------------------------

st.subheader("🏆 Product Performance")

product_sales = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(product_sales)


# ---------------------------------------------------
# Category Performance
# ---------------------------------------------------

st.subheader("📦 Category Performance")

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(category_sales)


# ---------------------------------------------------
# Future Forecast
# ---------------------------------------------------

st.divider()

st.subheader("🔮 30-Day Sales Forecast")

if os.path.exists(FORECAST_PATH):

    forecast_df = pd.read_csv(FORECAST_PATH)

    forecast_df["Date"] = pd.to_datetime(
        forecast_df["Date"]
    )

    st.dataframe(
        forecast_df,
        use_container_width=True
    )

    st.subheader("Future Sales Prediction")

    st.line_chart(
        forecast_df.set_index("Date")["Predicted_Sales"]
    )

    total_forecast = forecast_df["Predicted_Sales"].sum()
    average_forecast = forecast_df["Predicted_Sales"].mean()

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Expected 30-Day Sales",
            f"₹{total_forecast:,.2f}"
        )

    with col2:
        st.metric(
            "Average Forecasted Daily Sales",
            f"₹{average_forecast:,.2f}"
        )

else:

    st.warning(
        "Future forecast file was not found. "
        "Run the notebook first to generate future_sales_forecast.csv."
    )


# ---------------------------------------------------
# Dataset Preview
# ---------------------------------------------------

st.divider()

st.subheader("📋 Dataset Preview")

st.dataframe(
    filtered_df.head(20),
    use_container_width=True
)


# ---------------------------------------------------
# Footer
# ---------------------------------------------------

st.divider()

st.caption(
    "Predictive Analytics Using Historical Data | "
    "Machine Learning Project"
)