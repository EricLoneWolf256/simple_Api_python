import requests

API_KEY = "8aa94b6f9f98ed8cf2225500807d93ae"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
IPINFO_URL = "https://ipinfo.io"

try:
    location_data = requests.get(IPINFO_URL).json()
    city = location_data.get("city")
except Exception as e:
    print("Error detecting location:", e)
    city = None

if city:
    print(f"Detected location: {city}")
    request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        main = data.get("main", {})
        weather = data.get("weather", [{}])[0]
        temperature = round(main.get("temp") - 273.15, 2)
        humidity = main.get("humidity")
        description = weather.get("description", "").lower()

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {main.get('pressure')} hPa")
        print(f"Description: {description}")

        if temperature < 20 or "rain" in description or "drizzle" in description:
            print("Advice: It's best to carry a jacket!")
        else:
            print("Advice: No jacket needed, enjoy the weather!")
    else:
        print("Error fetching weather data.")
else:
    print("Could not detect location.")
