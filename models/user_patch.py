from pydantic import BaseModel


class UserPatch(BaseModel):
    name: str | None = None
    username: str | None = None
    email: str | None = None