from fastapi import FastAPI
from db.base_db import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get('/')
async def root():
    return "hello world"