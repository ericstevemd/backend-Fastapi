from pydantic import BaseModel
from typing import Optional


class UserSchema(BaseModel):
    id: Optional[str]
    name:str
    usermen:str
    user_passw:str