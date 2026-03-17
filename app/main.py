from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import init_db

from typing import Annotated
from fastapi import Depends
from app.routers import plants
from app.routers import machines


@asynccontextmanager
async def lifespan(app: FastAPI):
   init_db()
   yield
   print("App Finalizada")


app = FastAPI(lifespan=lifespan)

app.include_router(plants.router)
app.include_router(machines.router)




@app.get('/')
async def welcome():
    return {"message": "Welcome to FastAPI"}