import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="VisionScope Command Center", layout="wide")

# --------------------------
# CORPORATE + CIVIC THEME
# --------------------------
st.markdown("""
<style>
body {
    background-color: #0e1624;
}

.main {
    background-color: #0e1624;
    color: #f5f6fa;
    font-family: 'Segoe UI', sans-serif;
}

h1 {
    color: #c8a94a;
    font-weight: 700;
}

h2, h3 {
    color: #ffffff;
    font-weight: 600;
}

div[data-testid="metric-container"] {
    background-color: #1b263b;
    padding: 25px;
    border-radius: 14px;
    border: 1px solid rgba(200,169,74,0.4);
}

.stMetric label {
    color: #9ca3af !important;
    font-size: 14px !important;
}

.stMetric div {
    color: #ffffff !important;
    font-size: 30px !important;
    font-weight: bold;
}

hr {
    border: 1px solid #2c3e50;
}
</style>
""", unsafe_allow_html=True)

st.title("VisionScope — Urban Intelligence Platform")

csv_path = "analytics_log.csv"

if not os.path.exists(csv_path):
    st.warning("Analytics file not found. Run detection system first.")
    st.stop()

df = pd.read_csv(csv_path)

if df.empty:
    st.warning("Analytics file is empty.")
    st.stop()

latest = df.iloc[-1]

# --------------------------
# STATUS COLOR LOGIC
# --------------------------
def status_color(status):
    if "High" in status or "Dense" in status:
        return "#e74c3c"
    elif "Medium" in status or "Moderate" in status:
        return "#f39c12"
    else:
        return "#2ecc71"

traffic_color = status_color(latest["traffic_status"])
crowd_color = status_color(latest["crowd_status"])

st.subheader("Real-Time Urban Status")

col1, col2, col3 = st.columns(3)

col1.metric("Vehicles", latest["vehicle_count"])
col2.metric("People", latest["people_count"])
col3.markdown(
    f"<h3 style='color:{traffic_color};'>Traffic: {latest['traffic_status']}</h3>",
    unsafe_allow_html=True
)

st.markdown(
    f"<h3 style='color:{crowd_color};'>Crowd: {latest['crowd_status']}</h3>",
    unsafe_allow_html=True
)

# Advisory Panel
st.markdown("### Command Advisory")
st.markdown(
    f"""
    <div style='
        background-color:#1b263b;
        padding:20px;
        border-radius:12px;
        border-left:6px solid {traffic_color};
        font-size:16px;
    '>
        {latest["advisory"]}
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# --------------------------
# ANALYTICS SECTION
# --------------------------
st.subheader("Operational Trends")

st.line_chart(df[["vehicle_count", "people_count"]])

st.subheader("Traffic Density Distribution")
st.bar_chart(df["traffic_status"].value_counts())

st.subheader("Crowd Density Distribution")
st.bar_chart(df["crowd_status"].value_counts())

st.success("Command Center Operational")