# Development Challenges & Solutions

Throughout the development of the World Cup Analytics & Prediction Platform, several technical and architectural challenges were encountered. Each issue provided valuable insight into software design, debugging, and best development practices.

---

# Challenge 1: Incorrect Prediction Engine Structure

## Problem

The `determine_winner()` function was accidentally defined inside the `predict()` method instead of as a private class method.

## Symptoms

- Variables such as `winner`, `confidence`, and `explanation` were unavailable outside the nested function.
- The prediction response could not be generated correctly.

## Root Cause

The helper function was incorrectly scoped, making it inaccessible from the rest of the class.

## Solution

- Moved the logic into a dedicated private method (`_determine_winner()`).
- Refactored the `predict()` method to orchestrate helper methods rather than contain all business logic.

## Outcome

The prediction engine became cleaner, easier to maintain, and easier to test.

---

# Challenge 2: Prediction Engine Dependency Injection

## Problem

After refactoring the Prediction Engine, the API attempted to construct it using an outdated constructor.

## Symptoms

```text
TypeError:
PredictionEngine.__init__() takes 2 positional arguments but 5 were given
```

## Root Cause

The constructor had been simplified to accept only the repository, while the router still attempted to inject multiple services.

## Solution

- Updated the API router to instantiate the engine using only the repository.
- Standardised dependency construction across the application.

## Outcome

The API successfully instantiated the Prediction Engine using a consistent dependency injection strategy.

---

# Challenge 3: PostgreSQL Installation Conflict

## Problem

Both EnterpriseDB PostgreSQL and Homebrew PostgreSQL were installed simultaneously.

## Symptoms

- Port 5432 conflicts
- Authentication failures
- Database startup errors
- Multiple PostgreSQL instances running

## Root Cause

The EnterpriseDB installation continued occupying the default PostgreSQL port while the Homebrew installation attempted to use the same port.

## Solution

- Removed EnterpriseDB from the development workflow.
- Standardised on the Homebrew installation.
- Restarted the Homebrew PostgreSQL service.
- Updated the project configuration to use the Homebrew database instance.

## Outcome

Database connectivity became stable and all services connected successfully.

---

# Challenge 4: Python Import Errors

## Problem

Several modules failed to import after reorganising the project structure.

## Symptoms

```text
ModuleNotFoundError
```

## Root Cause

Package paths were no longer valid after moving configuration files and dashboard modules.

## Solution

- Updated all import paths.
- Centralised configuration files.
- Standardised the project package structure.

## Outcome

The project loaded successfully without module import errors.

---

# Challenge 5: Streamlit Package Naming Conflict

## Problem

The Streamlit entry point was named `dashboard.py`.

## Symptoms

```text
'dashboard' is not a package
```

## Root Cause

The file name conflicted with the package directory named `dashboard`, causing Python's import system to import the wrong module.

## Solution

- Renamed the entry point to `home_app.py`.
- Updated the Streamlit launch command.
- Left the package directory named `dashboard`.

## Outcome

Dashboard pages imported correctly and navigation functioned as expected.

---

# Challenge 6: Circular Service Dependency

## Problem

While implementing the team comparison functionality, a circular dependency was introduced between analytics services.

## Symptoms

```text
ImportError:
cannot import name 'StrengthScoreService'
from partially initialized module
```

## Root Cause

`StrengthScoreService` depended on `TeamAnalyticsService`, while `TeamAnalyticsService` also depended on `StrengthScoreService`.

```
TeamAnalyticsService
        ↓
StrengthScoreService
        ↓
TeamAnalyticsService
```

## Solution

- Removed the dependency from `TeamAnalyticsService`.
- Moved the comparison orchestration into the FastAPI router.
- Allowed both services to depend only on `AnalyticsRepository`.

Final architecture:

```
AnalyticsRepository
        │
        ├──────────────┐
        │              │
TeamAnalyticsService   StrengthScoreService
        │              │
        └──────┬───────┘
               │
          FastAPI Router
```

## Outcome

The circular dependency was eliminated and the service architecture became significantly cleaner.

---

# Challenge 7: Recent Form Scoring Bug

## Problem

The recent form calculation always returned zero points.

## Symptoms

All teams received lower-than-expected strength scores.

## Root Cause

The `points` variable was initialised but never updated during match evaluation.

## Solution

Implemented proper football point allocation:

- Win = 3 points
- Draw = 1 point
- Loss = 0 points

## Outcome

Recent form and strength score calculations became accurate.

---

# Challenge 8: API and Dashboard Synchronisation

## Problem

The dashboard occasionally returned outdated responses after API changes.

## Symptoms

- Internal Server Errors
- Missing endpoints
- Dashboard displaying outdated information

## Root Cause

An existing Uvicorn process was still running, preventing the updated API from starting.

## Solution

- Terminated stale Uvicorn processes.
- Restarted the FastAPI server.
- Verified endpoints using Swagger before testing the Streamlit dashboard.

## Outcome

The dashboard consistently communicated with the latest API version.

---

# Lessons Learned

Throughout the development process, several software engineering principles became evident:

- Separate business logic into dedicated service classes.
- Avoid circular dependencies between services.
- Keep dependency injection consistent throughout the application.
- Use descriptive package names that do not conflict with Python modules.
- Validate backend endpoints independently before debugging frontend components.
- Keep database environments standardised to avoid configuration conflicts.
- Small business logic mistakes can significantly impact analytical accuracy.
- Layered architecture greatly improves maintainability and scalability.

---

# Overall Outcome

Addressing these challenges resulted in several architectural improvements:

- Cleaner layered architecture.
- Better separation of concerns.
- Improved dependency management.
- More maintainable service layer.
- Stable database configuration.
- Robust FastAPI backend.
- Reliable Streamlit dashboard integration.
- Stronger software engineering practices for future development.

These challenges significantly improved both the quality of the application and the overall software engineering process followed during the project.

---

### API Response Naming Mismatch

#### Problem
The Team Comparison dashboard raised a `KeyError` when displaying head-to-head statistics.

#### Cause
The backend API returned keys such as:

- `team_1_wins`
- `team_2_wins`

while the Streamlit dashboard attempted to access:

- `team_one_wins`
- `team_two_wins`

Because the dictionary keys did not exist, Streamlit raised a `KeyError`.

#### Solution
Updated the dashboard to use the same field names returned by the API:

- `team_1_wins`
- `team_2_wins`
- `team_1_goals`
- `team_2_goals`
- `team_1_win_rate`
- `team_2_win_rate`

#### Lesson Learned
Maintain consistent naming conventions between API responses and frontend code to prevent runtime errors and simplify maintenance.

## Challenge: Creating the World Cup History Database

### Problem

The application raised an `IndexError` when attempting to display World Cup history. Investigation showed that the `world_cups` table existed in the codebase but had never been created or populated in the PostgreSQL database.

Additionally, running the importer produced several errors:

- `relation "world_cups" does not exist`
- `FileNotFoundError` because the CSV path was incorrect when the importer was executed from a different working directory.
- `KeyError: 'Year'` even though the CSV visibly contained a **Year** column.

### Cause

Multiple issues contributed to the problem:

- The `WorldCup` model had been created, but `Base.metadata.create_all()` had not been executed after adding the model.
- The importer was using a relative file path that depended on the current working directory.
- The CSV file contained a UTF-8 Byte Order Mark (BOM), causing the first column to be read as `\ufeffYear` instead of `Year`.

### Solution

The following fixes were applied:

- Created the `world_cups` table by executing:

```python
Base.metadata.create_all(bind=engine)
```

- Updated the importer to reference the correct CSV location.
- Changed the CSV encoding from:

```python
encoding="utf-8"
```

to:

```python
encoding="utf-8-sig"
```

which automatically removes the UTF-8 BOM and restores the correct column names.

### Outcome

- The `world_cups` table was successfully created in PostgreSQL.
- Historical World Cup data (1930–2018) imported successfully.
- The importer completed without errors.
- The World Cup History feature can now retrieve tournament information directly from the database.