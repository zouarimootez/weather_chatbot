from langchain.tools import StructuredTool
from tools.tools_core import get_city_from_description, get_weather
from tools.schemas import GetCityInput, GetWeatherInput

TOOLS = [
    StructuredTool.from_function(
        func=get_city_from_description,
        name="GetCityFromDescription",
        description="Use this tool to find the city name when given a place description (like 'Eiffel Tower').",
        args_schema=GetCityInput,
    ),
    StructuredTool.from_function(
        func=get_weather,
        name="GetWeather",
        description="Use this tool to get the current weather for a given city name.",
        args_schema=GetWeatherInput,
    ),
]
