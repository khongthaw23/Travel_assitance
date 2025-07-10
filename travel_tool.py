# travel_tools.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()

def check_weather_forecast(city):
    try:
        api_key = os.getenv("OPENWEATHER_API_KEY")
        if not api_key:
            return "Missing OpenWeather API key."

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        res = requests.get(url)

        if res.status_code == 200:
            data = res.json()
            desc = data["weather"][0]["description"].capitalize()
            temp = data["main"]["temp"]
            return f"{desc}, {temp}°C"
        else:
            return f"Weather API error {res.status_code}: {res.text}"
    except Exception as e:
        return f"Exception occurred: {e}"


def find_flights_tool(destination: str):
    destination_query = destination.replace(" ", "+")  # URL-safe
    return f"Search flights to {destination}: https://www.google.com/travel/flights?q=flights+to+{destination_query}"





def lookup_hotel_availability(city):
    return f"Search hotels in {city}: https://www.booking.com/searchresults.html?ss={city}"

def get_attraction_info(city):
    api_key = os.getenv("GOOGLE_PLACES_API_KEY")
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=top+attractions+in+{city}&key={api_key}"
    
    res = requests.get(url)
    if res.status_code == 200:
        results = res.json().get("results", [])[:3]
        attractions = [place["name"] for place in results]
        return f"Top attractions in {city}: " + ", ".join(attractions)
    return "No attraction data found."
