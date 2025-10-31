from models.users_model import Users
from typing import Optional
from sqlalchemy.orm import Session
from schemas.users_schema import UserCreate

def authenticate(db: Session, username: str, password:str) -> Optional[Users]:
    # kiem tra username da ton tai chua
    pass

def create_user(db: Session, data: UserCreate):
    # kiem tra user ton tai chua
    # neu ton tai, return 'user da ton tai'
    exist_user = db.query(Users).filter(Users.username == data.username).first()
    if exist_user:
        raise Exception('User already exists')
    # neu chua ton tai , add vao db
    new_user = Users(
        username = data.username,
        password = data.password, # hash password
        email = data.email,
        full_name = data.full_name,
        avatar_url = data.avatar_url,
        date_of_birth = data.data_of_birth
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user