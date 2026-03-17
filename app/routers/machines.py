# POST /machines Crear una máquina asociada a una planta
# PATCH /machines/{id}/status Actualizar solo el estado de una máquina
from fastapi import APIRouter, Body
from sqlalchemy import select
from typing import Annotated

from app.deps import SessionDB
from app.models import Machine
from app.schema import MachineBase, MachinePatch, MachinePublic, PlantBase


router = APIRouter(
    tags=["machines"]
)

@router.post("/machines")
async def create_machine(
    session: SessionDB, 
    machine: MachineBase
) -> MachinePublic:
    m = Machine(**machine.model_dump())
    session.add(m)
    session.commit()
    return m


@router.get("/machines")
async def get_all_machines(session: SessionDB) -> list[MachinePublic]:
    machines = session.scalars(select(Machine)).all()
    return machines


@router.patch('/machines/{id}/status')
async def update_status_machine(
    session: SessionDB,
    id: int,
    status: MachinePatch
):
    machine = session.scalars(select(Machine).where(Machine.id == id)).one()
    machine.status = status.status
    session.add(machine)
    session.commit()
    return machine