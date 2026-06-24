from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from services.models.base import Base


class Match(Base):
    __tablename__ = "matches"

    id: Mapped[int] = mapped_column(primary_key=True)

    match_date: Mapped[date]

    home_team_id: Mapped[int] = mapped_column(
        ForeignKey("teams.id")
    )

    away_team_id: Mapped[int] = mapped_column(
        ForeignKey("teams.id")
    )

    home_score: Mapped[int]

    away_score: Mapped[int]

    tournament: Mapped[str] = mapped_column(
        String(100)
    )