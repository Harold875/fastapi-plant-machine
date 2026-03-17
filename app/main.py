from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import init_db

from typing import Annotated
from fastapi import Depends
from app.routers import plants
from app.routers import machines
from app.deps import validate_apikey


@asynccontextmanager
async def lifespan(app: FastAPI):
   init_db()
   yield
   print("App Finalizada")


app = FastAPI(lifespan=lifespan)

app.include_router(plants.router, dependencies=[Depends(validate_apikey)])
app.include_router(machines.router, dependencies=[Depends(validate_apikey)])



@app.get('/')
async def welcome():
    return {"message": "Welcome to FastAPI"}