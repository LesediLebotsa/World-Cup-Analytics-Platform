from services.importers.team_importer import TeamImporter

result = TeamImporter().run()

print("\n===== Team Import =====")
print(f"Teams Found: {result['teams_found']}")
print(f"Imported: {result['teams_imported']}")