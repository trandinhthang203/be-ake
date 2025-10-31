from services.users_service import create_user
from fastapi import APIRouter, Depends, HTTPException, status
from schemas.users_schema import UserCreate, UserRespone
from schemas.base_schema import ResponeBase, ErrorRespone
from db.base_db import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post('/register')
def register(user: UserCreate, db: Session = Depends(get_db)):
    new_user = create_user(db, user)
    return ResponeBase(
        status_code=201,
        message='Successfull',
        data= new_user
    )

