from pydantic import BaseModel


class AuthorizeModel(BaseModel):
    token: str
    user: str