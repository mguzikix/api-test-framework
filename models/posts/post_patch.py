from pydantic import BaseModel


class PostPatch(BaseModel):
    title: str | None = None
    body: str | None = None
