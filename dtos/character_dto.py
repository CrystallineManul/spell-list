from pydantic import BaseModel


class Character(BaseModel):
    character_id: int
    race_id: int
    name: str
