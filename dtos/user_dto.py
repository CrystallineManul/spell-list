from pydantic import BaseModel, ConfigDict


class UserDTO(BaseModel):
    user_id: int
    name: str
