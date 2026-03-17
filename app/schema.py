from datetime import datetime
from pydantic import BaseModel

class PlantBase(BaseModel):
    name: str
    location: str
    created_at: datetime | None = None
    
class PlantPublic(PlantBase):
    id: int
    created_at: datetime