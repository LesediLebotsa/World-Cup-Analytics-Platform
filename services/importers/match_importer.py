from pathlib import Path

import pandas as pd

from services.config.database import SessionLocal
from services.models.match import Match
from services.repositories.match_repository import MatchRepository
from services.repositories.team_repository import TeamRepository

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

CSV_PATH = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "international_matches1.csv"
)


class MatchImporter:

    def run(self):

        df = pd.read_csv(CSV_PATH)

        with SessionLocal() as session:

            if session.query(Match).count() > 0:

                return {
                    "matches_imported": 0,
                    "message": "Matches already exist. Skipping import."
                }

            team_repository = TeamRepository(session)
            match_repository = MatchRepository(session)

            teams = team_repository.get_team_lookup()

            imported = 0

            try:

                for _, row in df.iterrows():

                    home_team = teams[row["Home Team"]]
                    away_team = teams[row["Away Team"]]

                    match = Match(
                        external_id=row["ID"],
                        tournament=row["Tournament"],
                        match_date=pd.to_datetime(
                            row["Date"]
                        ).date(),
                        home_team_id=home_team.id,
                        away_team_id=away_team.id,
                        home_goals=row["Home Goals"],
                        away_goals=row["Away Goals"],
                        home_stadium=row["Home Stadium or Not"]
                    )

                    match_repository.add(match)

                    imported += 1

                session.commit()

            except Exception:

                session.rollback()
                raise

        return {
            "matches_imported": imported,
            "message": "Matches imported successfully."
        }


def import_matches():

    return MatchImporter().run()


if __name__ == "__main__":
    print(import_matches())