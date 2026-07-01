from services.config.database import engine
from services.models.base import Base


Base.metadata.create_all(bind=engine)

print("Tables created successfully.")