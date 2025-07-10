import streamlit as st
from agent import agent

# Page config
st.set_page_config(page_title="✈️ Travel Assistant", page_icon="🌍", layout="centered")

# Custom CSS for better visuals
st.markdown("""
    <style>
        .main {
            background-color: #f5f9ff;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.05);
        }
        .stTextInput > div > div > input {
            border: 2px solid #1f77b4;
            border-radius: 8px;
        }
        .stButton > button {
            background-color: #1f77b4;
            color: white;
            border-radius: 8px;
            padding: 0.6rem 1.2rem;
            font-weight: bold;
        }
        .stButton > button:hover {
            background-color: #155d8b;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("🧳 AI Travel Assistant")
st.caption("Plan smarter. Explore better. Powered by AI.")

# Input area inside styled container
with st.container():
    st.markdown('<div class="main">', unsafe_allow_html=True)

    user_input = st.text_input("✍️ What do you need help with?", 
                               placeholder="e.g., Find flights from Delhi to Tokyo")

    ask_btn = st.button("Ask the Assistant")

    if ask_btn:
        if user_input.strip():
            with st.spinner("✈️ Let me find the best info for you..."):
                response = agent.run(user_input)
                st.success("✅ Here's what I found:")
                st.markdown(response)
        else:
            st.warning("⚠️ Please enter a valid travel question.")

    st.markdown('</div>', unsafe_allow_html=True)
