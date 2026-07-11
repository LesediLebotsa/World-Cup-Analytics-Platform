# Docker & Deployment Challenges

## Overview

This document records the engineering challenges encountered while containerizing the World Cup Analytics Platform. These issues were resolved during Sprint 7 (DevOps & Deployment).

---

# Challenge 1 - Docker CLI Not Available

## Problem

Although the Python Docker package had been installed using:

```bash
pip install docker
```

the terminal returned:

```text
zsh: command not found: docker
```

## Root Cause

The Python package only provides a Python SDK.

It does **not** install the Docker Engine or Docker CLI.

## Solution

- Installed Docker Desktop.
- Verified installation.

```bash
docker --version
docker info
```

---

# Challenge 2 - Docker Desktop Startup Failure

## Problem

Docker Desktop failed to open with:

```text
Application "Docker" is not responding
```

## Root Cause

Docker Desktop failed to initialize correctly.

## Solution

- Restarted Docker Desktop.
- Restarted macOS.
- Confirmed daemon availability using:

```bash
docker info
```

---

# Challenge 3 - TLS Handshake Timeout

## Problem

Building the Docker image stalled while downloading the Python base image.

```text
TLS handshake timeout
```

## Root Cause

Docker Hub connectivity issue.

## Solution

- Verified internet connection.
- Pulled images manually.
- Rebuilt images after Docker networking recovered.

---

# Challenge 4 - Missing CSV Dataset

## Problem

Container startup failed because the importer could not locate:

```text
international_matches1.csv
```

## Root Cause

The dataset was not copied into the Docker image.

## Solution

- Updated Dockerfile.
- Verified COPY commands.
- Rebuilt images.

---

# Challenge 5 - PostgreSQL Authentication

## Problem

FastAPI returned:

```text
FATAL: role "postgres" does not exist
```

## Root Cause

The local PostgreSQL installation used the user:

```
dell
```

rather than:

```
postgres
```

Docker PostgreSQL used different credentials from the local installation.

## Solution

Configured different database URLs for:

- Local development
- Docker Compose

---

# Challenge 6 - Incorrect DATABASE_URL

## Problem

The application continued attempting to connect using:

```text
postgres
```

even after modifying the default value.

## Root Cause

The environment variable inside `.env` overrode the default value inside `settings.py`.

## Solution

Updated:

```
DATABASE_URL
```

inside the `.env` file and restarted the application.

---

# Challenge 7 - Dashboard Folder Missing

## Problem

Docker reported:

```text
dashboard/1_Home.py does not exist
```

## Root Cause

The `dashboard` directory had accidentally been excluded inside `.dockerignore`.

## Solution

Removed:

```
dashboard
```

from `.dockerignore` and rebuilt the images.

---

# Challenge 8 - Incorrect Dashboard Entry Point

## Problem

The dashboard container failed to start.

## Root Cause

The Dockerfile referenced an outdated Streamlit entry file.

The application had been renamed from:

```
home_app.py
```

to

```
1_Home.py
```

## Solution

Updated the Docker command to use the new entry point.

---

# Challenge 9 - Docker Port Conflicts

## Problem

Docker failed with:

```text
ports are not available
```

## Root Cause

Existing local applications were already using:

- 8000
- 8501
- 5432

## Solution

Mapped Docker containers to alternative host ports.

Example:

- 8001 → FastAPI
- 8502 → Streamlit
- 5433 → PostgreSQL

---

# Challenge 10 - Module Import Errors

## Problem

Container startup produced:

```text
ModuleNotFoundError
```

for the setup scripts.

## Root Cause

Python package imports were not resolved correctly during container execution.

## Solution

- Converted setup scripts to module execution.
- Added package initialization where required.
- Updated startup commands.

---

# Challenge 11 - HTTP 500 Errors

## Problem

Dashboard pages returned:

```
500 Internal Server Error
```

## Root Cause

FastAPI attempted to connect using an invalid PostgreSQL user because the local environment variables differed from Docker configuration.

## Solution

Updated the database connection configuration and restarted the application.

---

# Lessons Learned

The deployment process highlighted several important software engineering concepts:

- Docker networking differs from localhost development.
- Docker containers require independent filesystem management.
- Environment variables override application defaults.
- PostgreSQL roles differ across installations.
- Container startup order is important when services depend on databases.
- Docker Compose simplifies multi-container orchestration.
- Careful debugging of logs significantly reduces troubleshooting time.

---

# Outcome

The platform is now capable of running as a fully containerized application consisting of:

- PostgreSQL
- FastAPI REST API
- Streamlit Dashboard

The project can now be deployed consistently across different environments using Docker Compose.