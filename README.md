# Weather App with Jacket Advice

## 📌 Description
This is a simple Python weather application that fetches **current weather data** for a given city using the **OpenWeatherMap API**.  
It not only shows you temperature, humidity, and conditions but also gives you **advice on whether to carry a jacket**.

---

## 🚀 Features
- Fetches live weather data from OpenWeatherMap.
- Displays:
  - Temperature (in °C)
  - Humidity (%)
  - Atmospheric pressure (hPa)
  - Weather description (e.g., "light rain", "clear sky")
- Jacket advice:
  - If temperature is **below 20°C** or it’s **raining/drizzling**, it suggests taking a jacket.

---

## 📦 Requirements
- Python 3.x
- `requests` library

Install requests with:
```bash
pip install requests
