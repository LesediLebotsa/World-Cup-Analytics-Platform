from services.config.database import engine

from services.models.base import Base
from services.models.team import Team
from services.models.match import Match
from services.models.world_cup import WorldCup


def create_tables():

    Base.metadata.create_all(bind=engine)

    print("Database tables created.")


if __name__ == "__main__":
    create_tables()