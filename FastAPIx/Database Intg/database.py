# db setup

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# "___//username:password@ip:port/dbname"
DATABASE_URL="postgresql+psycopg2://postgres:postgres@localhost:5432/commondb"

engine = create_engine(
        DATABASE_URL,
        echo=True
)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class for declarative models
Base = declarative_base()
