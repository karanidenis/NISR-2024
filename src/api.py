import streamlit as st
import json
from typing import Optional
import requests

# API configuration
BASE_API_URL = "http://127.0.0.1:7860"
FLOW_ID = "3d2c03b3-5f26-4331-9b93-786ab29bce23"
TWEAKS = {
    "ChatInput-qw1LG": {
        "input_value": "",
        "sender": "User",
        "sender_name": "User",
        "should_store_message": True,
    }
}

def run_flow(message: str,
             endpoint: str,
             output_type: str = "chat",
             input_type: str = "chat",
             tweaks: Optional[dict] = None) -> dict:
    """Run a flow with the given message and tweaks."""
    api_url = f"{BASE_API_URL}/api/v1/run/{endpoint}"
    payload = {
        "output_type": output_type,
        "input_type": input_type,
    }
    if tweaks:
        payload["tweaks"] = tweaks
    response = requests.post(api_url, json=payload)
    return response.json()

# Streamlit UI
st.title("Rwanda Labour Force Survey Chatbot")

# Input for user message
user_input = st.text_input("Ask a question:", key="user_input")

# Submit button
if st.button("Send"):
    if user_input.strip():
        # Update tweaks with the user's input
        TWEAKS["ChatInput-qw1LG"]["input_value"] = user_input
        
        # Call the API
        with st.spinner("Getting response..."):
            try:
                response = run_flow(
                    message=user_input,
                    endpoint=FLOW_ID,
                    tweaks=TWEAKS
                )
                # Extract the text field
                text = response['outputs'][0]['outputs'][0]['results']['message']['data']['text']
                print(text)
                # print(response)
                # Display response
                st.success("Response:")
                # st.write(text.get("output", {}).get("response", "No response received."))
                st.write(text)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a question before submitting.")
