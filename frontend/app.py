import streamlit as st
import requests

# 1. Page Configuration (Must be the first Streamlit command)
st.set_page_config(
    page_title="FastAPI & Streamlit Demo",
    page_icon="⚡",
    layout="centered"
)

# BACKEND FASTAPI URL
BACKEND_URL = "http://127.0.0.1:8000"

# 2. Hero Section / Headers
st.title("⚡ FastAPI & Streamlit")
st.markdown(
    "Welcome to the **FastAPI** and **Streamlit** integration demo. "
    "Test the connection between your frontend and backend using the tabs below."
)
st.divider()

# 3. Use Tabs to separate GET and POST requests cleanly
tab1, tab2 = st.tabs(["🌐 GET Request", "✉️ POST Request"])

# --- GET REQUEST TAB ---
with tab1:
    st.subheader("Test GET Endpoint")
    st.markdown("Fetch a simple greeting message from the backend.")
    
    # Use primary styling and full width for the button
    if st.button("Call GET API", type="primary", use_container_width=True):
        with st.spinner("Fetching response..."):
            try:
                response = requests.get(f"{BACKEND_URL}/hello")
                response.raise_for_status() # Check for HTTP errors
                data = response.json()
                st.success(f"**Response:** {data['message']}")
            except requests.exceptions.RequestException as e:
                st.error(f"**Connection Error:** Make sure the FastAPI backend is running.\n\n{e}")

# --- POST REQUEST TAB ---
with tab2:
    st.subheader("Test POST Endpoint")
    st.markdown("Send your name to the backend and receive a personalized greeting.")
    
    # Add a placeholder to the text input for better UX
    name = st.text_input("Enter your name:", placeholder="e.g., Jane Doe")
    
    if st.button("Call POST API", type="primary", use_container_width=True):
        if name.strip() == "":
            st.warning("⚠️ Please enter your name before calling the API.")
        else:
            with st.spinner("Sending data..."):
                try:
                    payload = {"name": name}
                    response = requests.post(f"{BACKEND_URL}/greet", json=payload)
                    response.raise_for_status()
                    data = response.json()
                    st.success(f"**Response:** {data['response']}")
                except requests.exceptions.RequestException as e:
                    st.error(f"**Connection Error:** Make sure the FastAPI backend is running.\n\n{e}")

# 4. Optional Footer
st.markdown("---")
st.caption("🚀 Built with [Streamlit](https://streamlit.io/) and [FastAPI](https://fastapi.tiangolo.com/)")
