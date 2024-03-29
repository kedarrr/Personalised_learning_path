import streamlit as st
import requests

# Define the URL of your FastAPI endpoint
FASTAPI_URL = "https://fastapi-a8tk.onrender.com/generate_learning_path"

# Function to call the FastAPI endpoint
def call_fastapi_endpoint(data):
    response = requests.post(FASTAPI_URL, json=data)
    if response.status_code == 200:
        return response.json()["learning_path"]
    else:
        st.error("Error: Failed to generate learning path")

# Streamlit UI components
st.title("Personalized Learning Path Generator")

# Input fields
domain = st.text_input("Domain")
proficiency = st.text_input("Proficiency")
preferences = st.text_input("Preferences")

# Button to generate learning path
if st.button("Generate Learning Path"):
    if domain and proficiency and preferences:
        input_data = {
            "domain": domain,
            "proficiency": proficiency,
            "preferences": preferences
        }
        learning_path = call_fastapi_endpoint(input_data)
        if learning_path:
            st.success("Generated Learning Path:")
            st.write(learning_path)
    else:
        st.error("Please fill in all fields")
