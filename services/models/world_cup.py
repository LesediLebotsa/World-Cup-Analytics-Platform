from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from services.models.base import Base


class WorldCup(Base):
    __tablename__ = "world_cups"

    id: Mapped[int] = mapped_column(primary_key=True)

    year: Mapped[int]

    host_country: Mapped[str] = mapped_column(
        String(100)
    )

    winner: Mapped[str] = mapped_column(
        String(100)
    )

    runner_up: Mapped[str] = mapped_column(
        String(100)
    )