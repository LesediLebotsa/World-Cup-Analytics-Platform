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
            try:

                for team_name in teams:

                    if repository.get_by_name(team_name):
                        continue

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
            "teams_imported": imported
        }