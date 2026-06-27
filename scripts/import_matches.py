from services.importers.match_importer import MatchImporter

matches = MatchImporter().run()

print(f"Imported {matches} matches.")