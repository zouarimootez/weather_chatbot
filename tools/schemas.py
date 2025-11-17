from pydantic import BaseModel, Field

class GetCityInput(BaseModel):
    place_description: str = Field(description="Description or name of a place, e.g. 'near the Eiffel Tower'.")

class GetWeatherInput(BaseModel):
    city_name: str = Field(description="Name of the city to get weather data for.")