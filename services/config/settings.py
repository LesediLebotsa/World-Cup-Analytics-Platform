import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://dell:Malebina1357@localhost:5432/world_cup_prediction"
)