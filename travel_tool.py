# travel_tools.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()

def check_weather_forecast(city):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    res = requests.get(url)
    
    if res.status_code == 200:
        data = res.json()
        desc = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        return f"{desc}, {temp}°C"
    return "Weather data not available."

def find_flights(origin, destination):
    return f"Check flights here: https://www.skyscanner.com/transport/flights/{origin.lower()}/{destination.lower()}/"

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
