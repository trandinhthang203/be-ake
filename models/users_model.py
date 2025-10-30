from sqlalchemy import Column, Integer, String, Boolean, DateTime
from db.base_db import Base

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)  # bắt buộc và duy nhất
    password = Column(String, nullable=False)
    email = Column(String)
    full_name = Column(String)
    avatar_url = Column(String)
    date_of_birth = Column(DateTime)