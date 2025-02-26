from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from models.user_model import UserModel
from models.submit_task import STaskSubmit

from dtos.user_dto import UserDTO

application = FastAPI()
users = [
    UserModel(user_id=1, nickname='user_one'),
    UserModel(user_id=2, nickname='user_two'),
    UserModel(user_id=3, nickname='user_three')
]


@application.get("/")
async def home():
    return {"data": "Hello world!"}


@application.post("/")
async def submit_task(task: STaskSubmit):
    return {"data": task}


@application.get("/users/{user_id}")
async def get_user(user_id: int):
    matched_user = next((user for user in users if user.user_id == user_id), None)
    if matched_user is None:
        raise HTTPException(status_code=404, detail="user_not_found")
    return JSONResponse(content=jsonable_encoder(
        UserDTO(**{'user_id': matched_user.user_id, 'name': matched_user.nickname})))
