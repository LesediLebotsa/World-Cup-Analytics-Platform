from services.config.database import engine
from services.models.base import Base
from services.models.team import Team
from services.models.match import Match
from services.models.world_cup import WorldCup

Base.metadata.create_all(bind=engine)

print("Tables created successfully.")