# ✈️ Travel Assistant with LangChain + Groq + Real APIs

This is a Python-based conversational travel assistant powered by [LangChain](https://www.langchain.com/), [Groq](https://console.groq.com/), and real-time APIs. It can:

- 🔍 Check current **weather forecasts**
- ✈️ Search **flights**
- 🏨 Find **hotels**
- 🗺️ Show top **attractions**
- 💰 Estimate **travel costs** (experimental)

---

## ⚙️ Tech Stack

- 🔗 [LangChain Agents](https://docs.langchain.com/docs/components/agents/)
- 🤖 [Groq (LLM API)](https://console.groq.com/)
- ☁️ OpenWeatherMap API
- 🗺️ Google Places API
- 🛫 Skyscanner
- 🛏️ Booking.com
- 🧮 Real-time Cost Estimation

---

## 📁 Project Structure

travel-assistant/
├── agent.py # LangChain agent setup
├── travel_tools.py # Tools using external APIs
├── .env # Your API keys
├── README.md # This file
└── requirements.txt


---

## 🔐 Environment Setup

1. Install dependencies:

```bash
pip install -r requirements.txt

2.Create a .env file and the paste your api keys



🚀 Run the Assistant
python agent.py

