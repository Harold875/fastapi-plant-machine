from datetime import datetime
from pydantic import BaseModel

from app.models import Status

class PlantBase(BaseModel):
    name: str
    location: str
    created_at: datetime | None = None
    
class PlantPublic(PlantBase):
    id: int
    created_at: datetime
    total_machines: int


class MachineBase(BaseModel):
    name: str
    type: str
    status: Status
    plant_id: int


class MachinePublic(MachineBase):
    id: int
    created_at: datetime

class MachinePatch(BaseModel):
    status: Status

