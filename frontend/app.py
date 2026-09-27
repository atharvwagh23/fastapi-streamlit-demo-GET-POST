import streamlit as st
import requests

## BACKEND FASTAPI URL
BACKEND_URL = "http://127.0.0.1:8000"

## application title

st.title("FastAPI backend integration with streamlit")

st.header("welcome to FastAPI and Streamlit integration demo")

if st.button("Call Get API"):
    response = requests.get(
        f"{BACKEND_URL}/hello"
    )

    data = response.json()

    st.success(data["message"])

st.header("POST Request example")

name = st.text_input("Enter your name")

if st.button("Call POST API"):
    payload = {
        "name": name
    }

    ## send post request

    response = requests.post(
        f"{BACKEND_URL}/greet",
        json= payload
    )

    data = response.json()

    st.success(data["response"])