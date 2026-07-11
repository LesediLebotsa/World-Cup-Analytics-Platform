# Deployment Challenges & Troubleshooting

This document records the major technical challenges encountered while developing and deploying the World Cup Analytics & Prediction Platform. It serves as a reference for future deployments and demonstrates practical debugging and problem-solving skills.

---

# 1. PostgreSQL Connection Failure

## Problem

The API failed to connect to PostgreSQL with the error:

```text
connection to server at "localhost", port 5432 failed:
FATAL: role "postgres" does not exist
```

## Root Cause

The PostgreSQL installation on macOS was configured with the default user:

```text
dell
```

instead of

```text
postgres
```

The application configuration assumed the database user was `postgres`.

## Solution

Updated the database connection string to use the correct PostgreSQL role.

```python
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://dell:<password>@localhost:5432/world_cup_prediction"
)
```

## Lesson Learned

Never assume the default PostgreSQL role exists. Always verify existing roles using:

```sql
\du
```

---

# 2. SQLAlchemy Connection Errors

## Problem

Requests returned HTTP 500 errors immediately after deployment.

## Root Cause

The application was attempting to connect using an incorrect database URL.

## Solution

Verified:

- PostgreSQL service
- database name
- username
- password
- environment variables

before restarting the application.

---

# 3. FastAPI Rate Limiting

## Problem

SlowAPI raised:

```text
No "request" argument found on endpoint
```

## Root Cause

Rate-limited endpoints must accept a `Request` parameter.

## Solution

Updated every rate-limited endpoint.

Before

```python
def predict(team1: str, team2: str):
```

After

```python
def predict(
    request: Request,
    team1: str,
    team2: str
):
```

## Lesson Learned

SlowAPI decorators inspect endpoint signatures.

---

# 4. Redis Connection Refused

## Problem

```text
Connection refused localhost:6379
```

## Root Cause

Redis server was not running.

## Solution

Installed Redis locally and started the service before launching the API.

## Lesson Learned

Installing the Redis Python package does not install the Redis server itself.

---

# 5. Render Logging Failure

## Problem

Deployment failed with:

```text
FileNotFoundError: logs/api.log
```

## Root Cause

Render containers do not preserve local log directories.

## Solution

Replaced file-based logging with stdout logging.

Before

```python
logging.basicConfig(filename="logs/api.log")
```

After

```python
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
```

## Lesson Learned

Cloud platforms expect applications to write logs to stdout/stderr.

---

# 6. Missing Database Tables on Render

## Problem

API returned:

```text
relation "teams" does not exist
```

## Root Cause

The managed PostgreSQL database was empty after deployment.

## Solution

Executed the database setup script to:

- create tables
- import teams
- import matches
- import World Cup history

## Lesson Learned

Deploying an application does not automatically populate the database.

---

# 7. Streamlit Import Errors

## Problem

Streamlit Cloud raised:

```text
ModuleNotFoundError:
No module named 'dashboard'
```

and later

```text
ModuleNotFoundError:
No module named 'client'
```

## Root Cause

The dashboard was deployed using:

```text
dashboard/1_Home.py
```

When Streamlit launches using a file inside the `dashboard` directory, that directory becomes the working directory.

Using imports such as:

```python
from dashboard.client import APIClient
```

caused Python to search for a nested `dashboard` package that did not exist.

## Solution

Changed imports to reference modules relative to the dashboard directory.

Before

```python
from dashboard.client import APIClient
```

After

```python
from client import APIClient
```

Similarly,

Before

```python
from dashboard.config import BASE_URL
```

After

```python
from config import BASE_URL
```

## Troubleshooting Process

The issue was initially misdiagnosed because the IDE highlighted:

```python
from client import APIClient
```

as an unresolved import.

This suggested that the import itself was incorrect.

However, deployment logs showed the real issue occurred after `client.py` was imported, where it attempted to import `dashboard.config`.

Reviewing the deployment environment and understanding Streamlit's working directory behaviour revealed that the IDE warning was misleading and that the import paths should be relative to the dashboard directory.

## Lesson Learned

Always trust deployment logs over IDE warnings.

An IDE may report unresolved imports while the runtime environment resolves modules differently.

Understanding the application's working directory is essential when deploying Python applications.

---

# 8. Redis Deployment Decision

## Problem

Render no longer provides a free Redis instance.

## Decision

Redis caching was retained in the project because it demonstrates caching architecture and backend engineering skills.

For cloud deployment, caching is disabled unless a Redis service is available.

## Lesson Learned

Portfolio projects should demonstrate engineering practices even if certain production infrastructure is unavailable on free hosting tiers.

---

# Overall Outcome

The project successfully demonstrates:

- FastAPI backend development
- Layered software architecture
- PostgreSQL integration
- SQLAlchemy ORM
- Docker and Docker Compose
- Request logging
- Rate limiting
- Redis caching
- Cloud deployment (Render)
- Streamlit deployment
- Systematic debugging and troubleshooting of production issues