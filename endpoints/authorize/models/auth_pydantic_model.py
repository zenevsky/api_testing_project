from pydantic import BaseModel


class AuthorizeModel(BaseModel):
    token: str
    user: str

class KillAuthModel(BaseModel):
    message: str = 'Ok'