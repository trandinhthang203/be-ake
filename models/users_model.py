from sqlalchemy import Column, Integer, String, Boolean, DateTime
from models.base_model import BaseModel

class Users(BaseModel):
    __tablename__ = 'users'

    username = Column(String, nullable=False, unique=True)  # bắt buộc và duy nhất
    password = Column(String, nullable=False)
    email = Column(String)
    full_name = Column(String)
    avatar_url = Column(String)
    date_of_birth = Column(DateTime)