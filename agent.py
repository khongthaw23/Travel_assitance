# agent.py

from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType

from travel_tool import (
    check_weather_forecast,
    find_flights_tool,
    lookup_hotel_availability,
    get_attraction_info
)

# Load API key from .env
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
open_api_key=os.getenv("OPENWEATHER_API_KEY")
print("OpenWeather API Key:", os.getenv("OPENWEATHER_API_KEY"))

# Use Groq's Gemma model
llm = ChatGroq(
    api_key=groq_api_key,
    model_name="gemma2-9b-it"  # Options: llama3-8b, gemma-7b-it, mixtral-8x7b
)

tools = [
    Tool(
        name="WeatherForecast",
        func= check_weather_forecast,
        description="Get the weather forecast for a city."
    ),
    Tool(
        name="FindFlights",
        func=find_flights_tool,
        description="Find flights between two cities. Input should be in the format: 'Delhi to Mumbai'."
    ),
    Tool(
        name="HotelLookup",
        func=lookup_hotel_availability,
        description="Check hotel availability in a city."
    ),
    Tool(
        name="AttractionInfo",
        func=get_attraction_info,
        description="Get information about top attractions in a city."
    )
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
pip install langchain-groq
