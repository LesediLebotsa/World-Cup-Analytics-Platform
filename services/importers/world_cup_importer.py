import csv
from pathlib import Path
from services.config.database import SessionLocal
from services.models.world_cup import WorldCup

db = SessionLocal()

db.query(WorldCup).delete()

csv_path = (
    Path(__file__)
    .resolve()
    .parents[2]
    / "data"
    / "raw"
    / "world_cups1.csv"
)

with open(
    csv_path,
    newline="",
    encoding="utf-8-sig"
) as file:

    reader = csv.DictReader(file)

    for row in reader:

        world_cup = WorldCup(
            year=int(row["Year"]),
            host_country=row["Host Country"],
            winner=row["Winner"],
            runner_up=row["Runners-Up"],
            third_place=row["Third"],
            fourth_place=row["Fourth"],
            goals_scored=int(row["Goals Scored"])
        )

        db.add(world_cup)

db.commit()
db.close()

print("World Cup history imported successfully.")