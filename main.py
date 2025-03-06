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

# http://127.0.0.1:8000/terceirocommit
@app.get("/terceirocommit")
async def terceirocommit():
    return {"message": "terceirocommit"}

# http://127.0.0.1:8000/quartocommit
@app.get("/quartocommit")
async def quartocommit():
    return {"message": "quartocommit"}

# http://127.0.0.1:8000/quintocommit
@app.get("/quintocommit")
async def quintocommit():
    return {"message": "quartocommit"}

# http://127.0.0.1:8000/sextocommit
@app.get("/sextocommit")
async def sextocommit():
    return {"message": "sextocommit"}
