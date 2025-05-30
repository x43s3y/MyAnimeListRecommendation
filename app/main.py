from fastapi import FastAPI
from dotenv import load_dotenv
import os

app = FastAPI()
load_dotenv(dotenv_path="authentication/.env")

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}