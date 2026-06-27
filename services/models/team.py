from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from services.models.base import Base


class Team(Base):
    __tablename__ = "teams"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True
    )

    def __repr__(self) -> str:
        return f"Team(id={self.id}, name='{self.name}')"