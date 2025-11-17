# Weather Chatbot — Python (LangChain Tools + StormGlass + OSM)

A smart conversational Weather Chatbot that uses 2 external APIs to understand human-friendly location descriptions and provide real-time weather data:

✔ Convert a natural text description into a real city name (OpenStreetMap API)  
✔ Fetch live weather conditions such as temperature and cloud coverage (StormGlass API)

This project is built to be easily extendable as a LangChain tool for chat agents.

---

## 🚀 Features

- 🧠 **Understands non-structured input** like:  
  *"How is the weather near the Eiffel Tower?"* → Resolves Paris
- 🌍 **Uses OpenStreetMap Nominatim** for geolocation lookup
- ☀️ **Weather via StormGlass** with real coordinates (lat/lon)
- 🔌 **API-key secured** with environment variables (config module)
- ⚙️ **Modular tool-based design** for AI Agents

---

## 🏗️ Project Structure

```
weather_chatbot/
│
├─ agent/
│   ├─ __init__.py  
│   ├─ agent_setup.py  
│   ├─ config.py  
│   ├─ prompt.py  
│   └─ chat_memory.py 
├─ tools/
│   ├─ __init__.py  
│   ├─ schemas.py  
│   ├─ tool_registry.py  
│   └─ tools_core.py 
├─ main.py       
└─ README.md  
```

---

## 🔑 Requirements

- Python 3.10+
- Dependencies:

```bash
pip install -r requirements.txt
```

---

## 🛠️ Installation & Setup

### Step 1: Create Virtual Environment

Create and activate a Python virtual environment, then install dependencies:

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Step 2: Configure API Key

In `agent/config.py`, set your StormGlass API key:

```python
STORMGLASS_API_KEY = "YOUR_API_KEY_HERE"
```

You must have a **StormGlass API Key** — create a free account at [stormglass.io](https://stormglass.io)

---

## ⚙️ Tools Explained

### 1️⃣ Get City from Description — OpenStreetMap

```python
get_city_from_description(place_description: str) -> str
```

✔ Converts a place description into a city/state/town  
✔ Returns `"unknown"` if not found

### 2️⃣ Get Weather from City — StormGlass

```python
get_weather(city_name: str) -> str
```

✔ Uses geocoding from OSM to extract coordinates  
✔ Queries StormGlass to get:  
  → 🌡 Temperature (NOAA)  
  → ☁ Cloud Coverage (NOAA)

**Example Output:**

```
🌤 In Paris, it's 16°C with 20% cloud cover.
```

---

## 🧪 Example Usage

```python
from agent.tools import get_city_from_description, get_weather

city = get_city_from_description("Eiffel Tower")
print(city)  # Paris

weather = get_weather(city)
print(weather)
```

---


## 📧 Contact

For questions or suggestions, feel free to reach out:

- 📧 **Email**: [zouarimootez@gmail.com](mailto:zouarimootez@gmail.com)
- 💼 **LinkedIn**: [linkedin.com/in/mootez-zouari](https://linkedin.com/in/mootez-zouari/)
- 🌐 **Portfolio**: [mootezzouari.netlify.app](https://mootezzouari.netlify.app/)

You can also open an issue on GitHub for bugs or feature requests.