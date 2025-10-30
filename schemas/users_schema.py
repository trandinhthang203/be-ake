from typing import Generic, Optional, TypeVar
from pydantic.generics import GenericModel
from pydantic import BaseModel, Field

class Login(BaseModel):
    username: str
    password: str

class signin(BaseModel):
    username = str
    password = str
    email = str
    full_name = str
    avatar_url = str
    date_of_birth = str