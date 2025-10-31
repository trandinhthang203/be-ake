from fastapi import APIRouter
from api import users_api


router = APIRouter()

router.include_router(users_api.router, tags=['Users'], prefix='/users')
