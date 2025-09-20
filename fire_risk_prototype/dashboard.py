import streamlit as st
import folium
from streamlit_folium import st_folium

def estimate_fire_risk(temperature, humidity):
    if temperature > 35 and humidity < 30:
        return "High"
    elif temperature > 25 and humidity < 50:
        return "Medium"
    else:
        return "Low"

# UI
st.set_page_config(page_title="Forest Fire Risk Estimator", page_icon="🔥")
st.title("🔥 Forest Fire Risk Estimator")

temp = st.slider("🌡️ Select Temperature (°C)", 0, 50, 25)
hum = st.slider("💧 Select Humidity (%)", 0, 100, 50)

risk = estimate_fire_risk(temp, hum)

# Visual feedback
if risk == "High":
    st.markdown("### 🔴 Fire Risk Level: **High**")
    st.error("Extreme caution advised! Conditions are highly flammable.")
elif risk == "Medium":
    st.markdown("### 🟠 Fire Risk Level: **Medium**")
    st.warning("Moderate risk. Stay alert and monitor conditions.")
else:
    st.markdown("### 🟢 Fire Risk Level: **Low**")
    st.success("Low risk. Conditions are relatively safe.")

# Map section
st.subheader("🗺️ Fire-Prone Regions (Dummy Data)")

# Create a Folium map centered on a region (e.g., Alberta)
m = folium.Map(location=[53.9333, -116.5765], zoom_start=5)

# Add dummy fire-prone markers
fire_locations = [
    {"name": "Region A", "lat": 52.0, "lon": -114.0},
    {"name": "Region B", "lat": 54.0, "lon": -115.5},
    {"name": "Region C", "lat": 51.5, "lon": -113.5},
]

for loc in fire_locations:
    folium.Marker(
        location=[loc["lat"], loc["lon"]],
        popup=f"{loc['name']} - Fire Risk Zone",
        icon=folium.Icon(color="red", icon="fire")
    ).add_to(m)

# Display map in Streamlit
st_folium(m, width=700, height=500)

# Risk thresholds
with st.expander("📊 See Risk Thresholds"):
    st.markdown("""
    - **High Risk**: Temperature > 35°C and Humidity < 30%
    - **Medium Risk**: Temperature > 25°C and Humidity < 50%
    - **Low Risk**: All other conditions
    """)



