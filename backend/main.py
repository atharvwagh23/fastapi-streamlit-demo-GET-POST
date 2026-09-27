from fastapi import FastAPI
from pydantic import BaseModel

## Create FastAPI application
app = FastAPI()

## Create a request model

class UserRequest(BaseModel):
    name: str

## Get API
@app.get("/hello")
def hello():
    return {
        "message" : "Hello from the FastAPI backend!"
    }

## Post API:
@app.post("/greet")
def greet_user(user: UserRequest):
    username = user.name
    message = (
        f"Hello, {username}!"
        f"Welcome to the fastAPI backend"
    )

    return {
        "response": message
    }
