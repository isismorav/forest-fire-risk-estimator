import streamlit as st

def estimate_fire_risk(temperature, humidity):
    if temperature > 35 and humidity < 30:
        return "High"
    elif temperature > 25 and humidity < 50:
        return "Medium"
    else:
        return "Low"

st.title("🔥 Forest Fire Risk Estimator")

temp = st.slider("Select Temperature (°C)", 0, 50, 25)
hum = st.slider("Select Humidity (%)", 0, 100, 50)

risk = estimate_fire_risk(temp, hum)

st.subheader(f"Fire Risk Level: {risk}")
