"""
This module initializes the database by setting up the engine and session,
and provides a function to initialize the database schema.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, Student, Group

# Define the database URL
DATABASE_URL = "sqlite:///my_db.sql"

# Set up the database engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)


def init_db(db_engine=engine):
    """
    Initialize the database by dropping all existing tables and creating new ones.

    Args:
        db_engine: The SQLAlchemy engine to use for the database operations.
    """
    Base.metadata.drop_all(db_engine)
    Base.metadata.create_all(db_engine)
