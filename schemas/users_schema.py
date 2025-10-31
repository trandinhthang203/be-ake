from typing import Generic, Optional, TypeVar
from pydantic.generics import GenericModel
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    avatar_url: Optional[str] = None
    data_of_birth: Optional[datetime] = None

class UserCreate(UserBase):
    password: str = Field(..., min_length=6)


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    full_name: Optional[str] = None
    password: Optional[str] = None
    avatar_url: Optional[bool] = None
    data_of_birth: Optional[datetime] = None

class UserRespone(UserBase):
    updated_at: datetime

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'

