from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base
from app.config import settings

# Create the database engine using settings
engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to create tables
def create_tables():
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f'The following error has occurred: {e}')

if __name__ == "__main__":
    create_tables()
