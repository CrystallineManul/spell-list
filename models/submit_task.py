from typing import Optional
from pydantic import BaseModel, ConfigDict


class STaskSubmit(BaseModel):
    name: str
    description: Optional[str] = None


class STask(STaskSubmit):
    id: int
    model_config = ConfigDict(from_attributes=True)
