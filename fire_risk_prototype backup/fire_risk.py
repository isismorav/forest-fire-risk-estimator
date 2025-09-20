def estimate_fire_risk(temperature, humidity):
    if temperature > 35 and humidity < 30:
        return "High"
    elif temperature > 25 and humidity < 50:
        return "Medium"
    else:
        return "Low"

# Example usage
temp = float(input("Enter temperature (°C): "))
hum = float(input("Enter humidity (%): "))

risk = estimate_fire_risk(temp, hum)
print(f"🔥 Fire Risk Level: {risk}")
