#!/bin/sh

echo "Waiting for PostgreSQL..."

until python -c "
import psycopg2
try:
    psycopg2.connect(
        host='postgres',
        database='world_cup_prediction',
        user='postgres',
        password='postgres'
    )
    print('Database ready')
except Exception:
    raise SystemExit(1)
"
do
    echo "PostgreSQL not ready..."
    sleep 2
done

echo "Running database setup..."

python -m scripts.setup_database

echo "Starting FastAPI..."

exec uvicorn app.main:app --host 0.0.0.0 --port 8000