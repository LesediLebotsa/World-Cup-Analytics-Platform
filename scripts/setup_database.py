from scripts.create_tables import create_tables
from services.importers.team_importer import import_teams
from services.importers.match_importer import import_matches
from services.importers.world_cup_importer import import_world_cups

def setup_database():

    print("\nCreating database tables...")
    create_tables()

    print("\nImporting teams...")
    print(import_teams())

    print("\nImporting matches...")
    print(import_matches())

    print("\nImporting World Cups...")
    print(import_world_cups())

    print("\nDatabase setup completed successfully.")


if __name__ == "__main__":
    setup_database()