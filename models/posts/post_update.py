from pydantic import BaseModel


class PostUpdate(BaseModel):
    title: str
    body: str
    UserId: int