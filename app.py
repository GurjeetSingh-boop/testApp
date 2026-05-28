from fastapi import FastAPI
import unicorn

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello User , welcome to GithUb App!"}

