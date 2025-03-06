from fastapi import FastAPI
import random

app = FastAPI()

# http://127.0.0.1:8000/
@app.get("/")
async def root():
    return {"message": "Hello World"}

# http://127.0.0.1:8000/segundocommit
@app.get("/segundocommit")
async def segundocommit():
    return {"message": "segundocommit"}



