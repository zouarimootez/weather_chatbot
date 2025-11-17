import requests
from agent.config import STORMGLASS_API_KEY

WEATHER_API_KEY = STORMGLASS_API_KEY

# 1️⃣ Get City from description (OpenStreetMap API)
def get_city_from_description(place_description: str) -> str:
    """Resolve a location description into a city name using OpenStreetMap."""
    try:
        url = "https://nominatim.openstreetmap.org/search"
        params = {"q": place_description, "format": "json", "addressdetails": 1, "limit": 1}
        resp = requests.get(url, params=params, headers={"User-Agent": "weather-bot/1.0"})
        data = resp.json()

        if not data:
            return f"unknown"

        address = data[0].get("address", {})
        city = (
            address.get("city")
            or address.get("town")
            or address.get("village")
            or address.get("state")
        )
        return city or "unknown"
    except Exception as e:
        return "unknown"

# 2️⃣ Get Weather from StormGlass API
def get_weather(city_name: str) -> str:
    """Get weather for a given city using StormGlass API."""
    try:
        # NOTE: Replace with your real coordinates lookup in production
        geo_url = "https://nominatim.openstreetmap.org/search"
        geo_resp = requests.get(geo_url, params={"q": city_name, "format": "json", "limit": 1}, headers={"User-Agent": "weather-bot/1.0"})
        geo_data = geo_resp.json()
        if not geo_data:
            return f"❌ Could not find coordinates for {city_name}."
        lat, lon = geo_data[0]["lat"], geo_data[0]["lon"]

        url = "https://api.stormglass.io/v2/weather/point"
        params = {"lat": lat, "lng": lon, "params": "airTemperature,cloudCover"}
        headers = {"Authorization": WEATHER_API_KEY} 
        resp = requests.get(url, params=params, headers=headers)

        if resp.status_code != 200:
            return f"⚠️ StormGlass error {resp.status_code}: {resp.text}"

        data = resp.json()
        hour = data["hours"][0]
        temp = hour["airTemperature"]["noaa"]
        clouds = hour["cloudCover"]["noaa"]

        return f"🌤 In {city_name}, it's {temp}°C with {clouds}% cloud cover."
    except Exception as e:
        return f"⚠️ Error fetching weather: {e}"
