from pydantic import BaseModel


class RegisterUserSchema(BaseModel):
    display_name: str
    password: str
    login: str


class OAuthUserSchema(BaseModel):
    display_name: str
    login: str
    password: str
    client_name: str
    client_id: str
