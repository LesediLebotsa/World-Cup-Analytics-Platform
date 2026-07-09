from services.repositories.history_repository import HistoryRepository


class WorldCupHistoryService:

    def __init__(
            self,
            repository: HistoryRepository
    ):
        self.repository = repository

    def overview(self):

        tournaments = self.repository.get_world_cups()

        if not tournaments:
            raise ValueError("No World Cup history found.")

        total_goals = self.repository.total_goals()
        total_matches = self.repository.total_matches()

        return {

            "first_world_cup":
                tournaments[0].year,

            "latest_world_cup":
                tournaments[-1].year,

            "total_tournaments":
                len(tournaments),

            "different_champions":
                len(self.repository.winner_counts()),

            "total_matches":
                total_matches,

            "total_goals":
                total_goals,

            "average_goals_per_tournament":
                round(
                    total_goals / len(tournaments),
                    2
                )
        }

    def winners(self):

        counts = self.repository.winner_counts()

        return [

            {
                "country": country,
                "titles": titles
            }

            for country, titles in sorted(
                counts.items(),
                key=lambda x: x[1],
                reverse=True
            )

        ]

    def timeline(self):

        tournaments = self.repository.get_world_cups()

        return [

            {
                "year": tournament.year,
                "host": tournament.host_country,
                "winner": tournament.winner,
                "runner_up": tournament.runner_up,
                "third": tournament.third_place,
                "fourth": tournament.fourth_place,
                "goals": tournament.goals_scored
            }

            for tournament in tournaments

        ]

    def tournament(
            self,
            year: int
    ):

        tournament = self.repository.tournament_by_year(year)

        if tournament is None:
            raise ValueError("Tournament not found.")

        return {

            "year": tournament.year,
            "host": tournament.host_country,
            "winner": tournament.winner,
            "runner_up": tournament.runner_up,
            "third": tournament.third_place,
            "fourth": tournament.fourth_place,
            "goals": tournament.goals_scored

        }

    def facts(self):

        highest = self.repository.highest_scoring_world_cup()

        counts = self.repository.winner_counts()

        champion = max(
            counts,
            key=counts.get
        )

        return {

            "most_successful_country":
                champion,

            "titles":
                counts[champion],

            "highest_scoring_year":
                highest.year,

            "highest_goals":
                highest.goals_scored

        }