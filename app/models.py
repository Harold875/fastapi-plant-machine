import enum
from datetime import datetime, timezone
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import DateTime, String, ForeignKey

class Base(DeclarativeBase):
    pass


class Plant(Base):
    __tablename__ = "plant"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    location: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    machines: Mapped[list["Machine"]] = relationship(back_populates="plant")

    @property
    def total_machines(self):
        return len(self.machines)
    
    def __repr__(self) -> str:
        return f"Plant(id={self.id!r}, name={self.name!r})"



class Status(enum.Enum):
    OPERATIONAL = "operational"
    MAINTENANCE = "maintenance"
    OFFLINE = "offline"



class Machine(Base):
    __tablename__ = "machines"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    type: Mapped[str]
    status: Mapped[Status]
    plant_id: Mapped[int] = mapped_column(ForeignKey("plant.id"))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    
    plant: Mapped["Plant"] = relationship(back_populates="machines")
    
    def __repr__(self) -> str:
        return f"Machine(id={self.id!r}, name={self.name!r}, type={self.type}, status={self.status})"