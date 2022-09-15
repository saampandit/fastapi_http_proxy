import json
import asyncio
import httpx
import time
from datetime import datetime
import uvicorn
from fastapi import FastAPI, Request
from typing import Union
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from jwt_handler import generate_jwt_token

URL = "http://httpbin.org/post"

class User(BaseModel):
    username: str

# main async function to upstream http request
async def proxy(user_name):
    token = generate_jwt_token(user_name)
    headers = {'x-my-jwt': token}
    data = {'user': user_name}
    res = httpx.post(URL, json=data, headers=headers)
    output = json.loads(res.content)
    print(output)
    return output


# Initialize FastAPI app
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# counter variable to count the request
counter_lock = asyncio.Lock()
counter = 0

# Time calculator
start_time = datetime.now()

# async function to update the counter with the lock functionality
async def update_counter():
    global counter
    async with counter_lock:
        counter += 1

# Default Get request for the app
@app.get("/")
async def read_root():
    await update_counter()
    return {"Welcome to FastAPI"}


# post route for user
@app.post("/user/")
async def create_item(user: User):
    await update_counter()
    result = await proxy(user.username)
    return result

@app.get("/status", response_class=HTMLResponse)
async def get_status(request: Request):
    delta_time = str(datetime.now() - start_time)
    dt_time = delta_time.split(':')
    ss = dt_time[2].split('.')
    print(ss)
    return templates.TemplateResponse("status.html",
                                      {"request": request,
                                       "counter": counter,
                                        "days": dt_time[0],
                                        "minutes": dt_time[1],
                                        "seconds": int(ss[0])}
                                     )
    # return {"Total Requests": counter}


# if __name__ == "__main__":
    # uvicorn.run("main:app", host="127.0.0.1", port=8000)
