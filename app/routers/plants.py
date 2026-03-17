# POST /plants Crear una planta
# GET /plants Listar plantas (con conteo de máquinas por planta)
# GET /plants/{id} Detalle de planta con sus máquinas
from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from app.deps import SessionDB
from app.models import Plant
from app.schema import PlantBase, PlantPublic

router = APIRouter(
    # prefix="plants",
    tags=["plants"]
)


@router.get("/plants")
async def get_all_plants(session: SessionDB) -> list[PlantPublic]:
    users = session.scalars(select(Plant)).all()
    return users

@router.get("/plants/{id}")
async def get_one_plant(session: SessionDB, id: int):
    users = session.scalars(select(Plant).where(Plant.id == id)).one()
    return users


@router.post("/plants")
async def create_plant(session: SessionDB, plant: PlantBase) -> PlantPublic:
    p = Plant(**plant.model_dump())
    session.add(p)
    session.commit()
    return p