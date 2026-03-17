# POST /plants Crear una planta
# GET /plants Listar plantas (con conteo de máquinas por planta)
# GET /plants/{id} Detalle de planta con sus máquinas
from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import selectinload
from app.deps import SessionDB
from app.models import Plant
from app.schema import PlantBase, PlantDetail, PlantPublic


router = APIRouter(
    # prefix="plants",
    tags=["plants"]
)


@router.get("/plants")
async def get_all_plants(session: SessionDB) -> list[PlantPublic]:
    stmt = (
        select(Plant)
        .options(selectinload(Plant.machines))
    )
    plants = session.scalars(stmt).all()
    return plants

@router.get("/plants/{id}")
async def get_one_plant(session: SessionDB, id: int) -> PlantDetail:
    stmt = (
        select(Plant)
        .where(Plant.id == id)
        .options(selectinload(Plant.machines))
    )
    try:
        plant = session.scalars(stmt).one()
    except NoResultFound:
        raise HTTPException(404, f"Plant with id={id} not found.")
    return plant


@router.post("/plants")
async def create_plant(session: SessionDB, plant: PlantBase) -> PlantPublic:
    p = Plant(**plant.model_dump())
    session.add(p)
    session.commit()
    return p