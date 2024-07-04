from pydantic import BaseModel, ConfigDict
from typing import Optional


class SchTaskAdd(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str
    description: Optional[str] = None


class SchTaskGet(SchTaskAdd):
    id: int


class SchTaskResponse(BaseModel):
    ok: bool = True
    id: int

