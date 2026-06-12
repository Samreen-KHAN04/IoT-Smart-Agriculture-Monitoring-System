import streamlit as st
import pandas as pd
import plotly.express as px
import os

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="IoT Smart Agriculture Dashboard",
    page_icon="🌱",
    layout="wide"
)

# ==================================================
# FILE PATH
# ==================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

DATA_FILE = os.path.join(
    BASE_DIR,
    "data",
    "sensor_data.csv"
)

# ==================================================
# TITLE
# ==================================================

st.title("🌱 IoT Smart Agriculture Monitoring System")

# ==================================================
# CHECK FILE
# ==================================================

if not os.path.exists(DATA_FILE):
    st.error("sensor_data.csv not found")
    st.stop()

# ==================================================
# LOAD DATA
# ==================================================

try:
    df = pd.read_csv(DATA_FILE)
except Exception as e:
    st.error(f"Error loading CSV: {e}")
    st.stop()

if df.empty:
    st.warning("No sensor data available.")
    st.stop()

# ==================================================
# CLEAN DATA
# ==================================================

df["Time"] = pd.to_datetime(
    df["Time"],
    errors="coerce"
)

df = df.dropna(subset=["Time"])

latest = df.iloc[-1]

# ==================================================
# KPI SECTION
# ==================================================

st.header("📊 System Overview")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Temperature",
        f"{latest['Temperature']} °C"
    )

with c2:
    st.metric(
        "Humidity",
        f"{latest['Humidity']} %"
    )

with c3:
    st.metric(
        "Soil Moisture",
        f"{latest['SoilMoisture']} %"
    )

with c4:
    st.metric(
        "Water Level",
        f"{latest['WaterLevel']} %"
    )

# ==================================================
# FARM HEALTH STATUS
# ==================================================

st.header("🌾 Farm Health Status")

col1, col2, col3 = st.columns(3)

with col1:

    if latest["Temperature"] > 40:
        st.error("🔥 High Temperature Detected")
    else:
        st.success("✅ Temperature Normal")

with col2:

    if latest["SoilMoisture"] < 30:
        st.warning("⚠️ Low Soil Moisture")
    else:
        st.success("✅ Soil Moisture Healthy")

with col3:

    if latest["WaterLevel"] < 20:
        st.error("🚨 Low Water Level")
    else:
        st.success("✅ Water Reservoir Healthy")

# ==================================================
# CURRENT STATUS
# ==================================================

st.header("🚨 Current System Status")

if str(latest["Pump"]).upper() == "ON":
    st.error("🚿 Irrigation Pump ON")
else:
    st.success("🚿 Irrigation Pump OFF")

alert_value = str(latest["Alert"])

if alert_value.upper() == "NORMAL":
    st.success("✅ No Active Alerts")
else:
    st.warning(alert_value)

# ==================================================
# IRRIGATION RECOMMENDATION
# ==================================================

st.header("🤖 Irrigation Recommendation")

if latest["SoilMoisture"] < 30:

    st.error(
        """
        Recommendation: Start Irrigation

        Reason:
        Soil moisture is below threshold.
        """
    )

else:

    st.success(
        """
        Recommendation: No Irrigation Required

        Soil moisture is sufficient.
        """
    )

# ==================================================
# THRESHOLDS
# ==================================================

st.header("📋 System Thresholds")

threshold_df = pd.DataFrame({
    "Parameter": [
        "Temperature",
        "Soil Moisture",
        "Water Level"
    ],
    "Threshold": [
        "> 40 °C",
        "< 30 %",
        "< 20 %"
    ],
    "Action": [
        "High Temperature Alert",
        "Activate Pump",
        "Low Water Alert"
    ]
})

st.table(threshold_df)

# ==================================================
# TEMPERATURE GRAPH
# ==================================================

st.header("🌡 Temperature Variation Over Time")

fig_temp = px.line(
    df,
    x="Time",
    y="Temperature",
    markers=True,
    title="Temperature Trend"
)

fig_temp.update_layout(
    xaxis_title="Time",
    yaxis_title="Temperature (°C)"
)

st.plotly_chart(
    fig_temp,
    use_container_width=True
)

# ==================================================
# HUMIDITY GRAPH
# ==================================================

st.header("💧 Humidity Variation Over Time")

fig_humidity = px.line(
    df,
    x="Time",
    y="Humidity",
    markers=True,
    title="Humidity Trend"
)

fig_humidity.update_layout(
    xaxis_title="Time",
    yaxis_title="Humidity (%)"
)

st.plotly_chart(
    fig_humidity,
    use_container_width=True
)

# ==================================================
# SOIL MOISTURE GRAPH
# ==================================================

st.header("🌱 Soil Moisture Monitoring")

fig_soil = px.line(
    df,
    x="Time",
    y="SoilMoisture",
    markers=True,
    title="Soil Moisture Trend"
)

fig_soil.update_layout(
    xaxis_title="Time",
    yaxis_title="Soil Moisture (%)"
)

st.plotly_chart(
    fig_soil,
    use_container_width=True
)

# ==================================================
# WATER LEVEL GRAPH
# ==================================================

st.header("🚰 Water Reservoir Monitoring")

fig_water = px.line(
    df,
    x="Time",
    y="WaterLevel",
    markers=True,
    title="Water Level Trend"
)

fig_water.update_layout(
    xaxis_title="Time",
    yaxis_title="Water Level (%)"
)

st.plotly_chart(
    fig_water,
    use_container_width=True
)

# ==================================================
# LIGHT GRAPH
# ==================================================

st.header("☀️ Light Intensity Monitoring")

fig_light = px.line(
    df,
    x="Time",
    y="Light",
    markers=True,
    title="Light Intensity Trend"
)

fig_light.update_layout(
    xaxis_title="Time",
    yaxis_title="Light Intensity (Lux)"
)

st.plotly_chart(
    fig_light,
    use_container_width=True
)

# ==================================================
# ALERT HISTORY
# ==================================================

st.header("📊 Alert History")

alert_counts = (
    df["Alert"]
    .fillna("Unknown")
    .value_counts()
)

alert_df = pd.DataFrame({
    "Alert Type": alert_counts.index,
    "Count": alert_counts.values
})

fig_alert = px.bar(
    alert_df,
    x="Alert Type",
    y="Count",
    title="Alert Frequency Distribution"
)

st.plotly_chart(
    fig_alert,
    use_container_width=True
)

# ==================================================
# PUMP ANALYTICS
# ==================================================

st.header("🚿 Pump Activity Summary")

pump_counts = (
    df["Pump"]
    .fillna("Unknown")
    .value_counts()
)

pump_df = pd.DataFrame({
    "Pump Status": pump_counts.index,
    "Count": pump_counts.values
})

fig_pump = px.pie(
    pump_df,
    names="Pump Status",
    values="Count",
    title="Pump Usage Distribution"
)

st.plotly_chart(
    fig_pump,
    use_container_width=True
)

# ==================================================
# DATASET SUMMARY
# ==================================================

st.header("📈 Dataset Summary")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Total Records",
        len(df)
    )

with c2:
    st.metric(
        "Average Temperature",
        round(df["Temperature"].mean(), 2)
    )

with c3:
    st.metric(
        "Average Soil Moisture",
        round(df["SoilMoisture"].mean(), 2)
    )

# ==================================================
# STATISTICS
# ==================================================

st.header("📊 Dataset Statistics")

numeric_df = df.select_dtypes(include="number")

st.dataframe(
    numeric_df.describe()
)

# ==================================================
# RECENT RECORDS
# ==================================================

st.header("📄 Recent Sensor Records")

st.dataframe(
    df.tail(20),
    use_container_width=True
)