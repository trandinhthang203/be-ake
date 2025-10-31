from fastapi import FastAPI
from db.base_db import engine, Base
from models import Users
from api import router_api

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router_api)
