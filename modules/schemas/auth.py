from pydantic import BaseModel


class RegisterUserSchema(BaseModel):
    display_name: str
    password: str
    login: str