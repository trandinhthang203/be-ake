from sqlalchemy import Column, Integer, String, Boolean, DateTime
from db.base_db import Base

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    username = Column(String)
    email = Column(String)
    full_name = Column(String)
    avatar_url = Column(String)
    date_of_birth = Column(DateTime)