from fastapi import FastAPI
from models.submit_task import STaskSubmit

application = FastAPI()


@application.get("/")
async def home():
    return {"data": "Hello world!"}


@application.post("/")
async def submit_task(task: STaskSubmit):
    return {"data": task}
