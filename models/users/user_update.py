from pydantic import BaseModel


class UserUpdate(BaseModel):
    name: str
    username: str
    email: str