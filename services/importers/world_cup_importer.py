from pathlib import Path
import pandas as pd
from services.config.database import SessionLocal
from services.models.world_cup import WorldCup

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

CSV_PATH = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "world_cups1.csv"
)

class WorldCupImporter:

    def run(self):

        df = pd.read_csv(
            CSV_PATH,
            encoding="utf-8-sig"
        )

        imported = 0

        with SessionLocal() as session:

            if session.query(WorldCup).count() > 0:

                return {
                    "world_cups_imported": 0,
                    "message": "World Cups already exist. Skipping import."
                }

            try:

                for _, row in df.iterrows():

                    world_cup = WorldCup(
                        year=row["Year"],
                        host_country=row["Host Country"],
                        winner=row["Winner"],
                        runner_up=row["Runners-Up"],
                        third_place=row["Third"],
                        fourth_place=row["Fourth"],
                        goals_scored=row["Goals Scored"]
                    )

                    session.add(world_cup)

                    imported += 1

                session.commit()

            except Exception:

                session.rollback()
                raise

        return {
            "world_cups_imported": imported,
            "message": "World Cups imported successfully."
        }


def import_world_cups():

    return WorldCupImporter().run()


if __name__ == "__main__":
    print(import_world_cups())