from datetime import date

from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from services.models.base import Base


class Match(Base):
    __tablename__ = "matches"

    id: Mapped[int] = mapped_column(primary_key=True)

    external_id: Mapped[int] = mapped_column(
        unique=True,
        nullable=False,
        index=True
    )

    match_date: Mapped[date]

    tournament: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    home_team_id: Mapped[int] = mapped_column(
        ForeignKey("teams.id"),
        nullable=False
    )

    away_team_id: Mapped[int] = mapped_column(
        ForeignKey("teams.id"),
        nullable=False
    )

    home_goals: Mapped[int]

    away_goals: Mapped[int]

    home_stadium: Mapped[bool]

    home_team = relationship(
        "Team",
        foreign_keys=[home_team_id]
    )

    away_team = relationship(
        "Team",
        foreign_keys=[away_team_id]
    )

    def __repr__(self) -> str:
        return (
            f"Match("
            f"{self.home_team_id} vs "
            f"{self.away_team_id})"
        )