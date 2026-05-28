from fastapi import FastAPI
import unicorn

app = FastAPI()
@app.get("/")
def hello():
    return {"message": "Hello World!"}

#sample

