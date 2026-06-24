from sqlalchemy import create_engine
from services.config.settings import DATABASE_URL
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    DATABASE_URL,
    echo=True
)
SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
)