from fastapi import FastAPI
import unicorn

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello World!"}

# API to display name entered by user
@app.get("/name")
def displayName(name: str):
    return {"message": f"Hello {name}"}