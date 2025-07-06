import streamlit as st
from agent import agent

st.set_page_config(page_title="✈️ Travel Assistant", page_icon="🌍", layout="centered")

st.title("🧳 AI Travel Assistant")
st.markdown("Plan your trip with real-time help from an AI-powered assistant!")

# Input from user
user_input = st.text_input("Ask me anything about your travel (e.g., 'Find hotels in Paris', 'Weather in Tokyo'):")

# Call the LangChain agent
if st.button("Ask"):
    if user_input.strip() != "":
        with st.spinner("Thinking..."):
            response = agent.run(user_input)
            st.success("Answer:")
            st.markdown(response)
    else:
        st.warning("Please enter a valid question.")
