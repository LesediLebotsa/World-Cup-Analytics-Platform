## 8. Importer File Path Error

### Problem

Running the World Cup importer resulted in:

```text

FileNotFoundError

```

### Root Cause

The importer relied on a relative file path that depended on the current working directory.

### Resolution

The importer was updated to build an absolute project path using `pathlib.Path`.

```python

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

```

This ensures the importer works regardless of the execution location.

---

## 9. Automated Database Setup

### Challenge

Database initialization originally required multiple manual steps:

- Create tables

- Import teams

- Import matches

- Import World Cups

### Resolution

A dedicated `setup_database.py` script was created to automate the entire initialization process.

The script now:

1. Creates all database tables.

2. Imports teams.

3. Imports historical matches.

4. Imports World Cup history.

5. Prevents duplicate imports by checking for existing records.

This significantly simplifies project setup for new developers.

---

## 10. Pytest Import Configuration

### Problem

Running the test suite produced:

```text

ModuleNotFoundError: No module named 'app'

```

### Root Cause

Pytest was unable to resolve the project root as part of the Python module search path.

### Resolution

A `pytest.ini` configuration file was added to define the project root as the Python path. Once configured, the test suite successfully discovered the application modules and executed the integration tests.

---

## 11. Incorrect History Endpoint Test

### Problem

The History integration test failed with:

```text

404 Not Found

```

### Root Cause

The test attempted to call:

```text

/history/world-cups

```

However, the implemented API exposes the following endpoints:

- `/history/overview`

- `/history/timeline`

- `/history/winners`

- `/history/tournament/{year}`

- `/history/facts`

### Resolution

The test suite was updated to target the correct endpoints as defined in the API router.

---

## 12. Test Expectations Did Not Match API Contract

### Problem

The History Overview test failed with an assertion error because it expected fields that were not returned by the API.

Example:

```python

assert "total_world_cups" in overview

```

### Root Cause

The test was written using assumed response fields instead of validating the actual API contract.

### Resolution

The tests were updated to verify the fields actually returned by the service, including:

- `first_world_cup`

- `latest_world_cup`

- `different_champions`

- `average_goals_per_tournament`

This ensured the integration tests accurately reflected the implemented API behaviour.