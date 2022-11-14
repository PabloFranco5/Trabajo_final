from fastapi import FastAPI
from app.v1.Scripts.create_tables import create_tables

app = FastAPI()


@app.get('/')
def home():
    return {"message": "Hello World"}

create_tables()
