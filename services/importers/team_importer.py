from pathlib import Path

import pandas as pd

from services.config.database import SessionLocal
from services.models.team import Team
from services.repositories.team_repository import TeamRepository

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

CSV_PATH = PROJECT_ROOT / "data" / "raw" / "international_matches1.csv"


class TeamImporter:

    def run(self) -> dict:

        df = pd.read_csv(CSV_PATH)

        teams = (
            pd.concat(
                [
                    df["Home Team"],
                    df["Away Team"]
                ]
            )
            .dropna()
            .drop_duplicates()
            .sort_values()
            .tolist()
        )

        imported = 0

        with SessionLocal() as session:

            repository = TeamRepository(session)

            # Skip if teams already exist
            if session.query(Team).count() > 0:

                return {
                    "teams_found": len(teams),
                    "teams_imported": 0,
                    "message": "Teams already exist. Skipping import."
                }

            try:

                for team_name in teams:

                    repository.add(
                        Team(name=team_name)
                    )

                    imported += 1

                session.commit()

            except Exception:

                session.rollback()
                raise

        return {
            "teams_found": len(teams),
            "teams_imported": imported,
            "message": "Teams imported successfully."
        }


def import_teams():

    return TeamImporter().run()


if __name__ == "__main__":
    print(import_teams())