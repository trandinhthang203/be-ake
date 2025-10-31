from pydantic import BaseModel
from typing import Optional, TypeVar, Generic

# T = TypeVar['T']


class ResponeBase(BaseModel):
    status_code: int = 200
    message: str = 'Success'
    data: any


class ErrorRespone(BaseModel):
    status_code: int
    messasage: str
    data: any

