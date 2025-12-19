# weather.py
import requests

def Weather():
    # Coordinates for Hyderabad (or update dynamically if needed)
    lat = "17.3616"
    lon = "78.4746"
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={lat}&lon={lon}"
    headers = {
        "User-Agent": "MyWeatherApp/1.0"  # Required by met.no
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            weather = data["properties"]["timeseries"][0]["data"]["instant"]["details"]
            temp = weather.get("air_temperature", "N/A")
            return f"The current temperature is {temp}°C."
    except Exception as e:
        return f"Error fetching weather"

    return "Weather data not available."
