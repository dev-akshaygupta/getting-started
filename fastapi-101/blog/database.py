from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlmodel import Session

SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'
connect_args = {"check_same_thread": False}

# Create a DB engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args = connect_args)

# Bind DB engine with the session
SessionLocal = sessionmaker(bind=engine, autoflush=False, class_=Session)

# A factory function provided by SQLAlchemy that creates a base class for all your ORM models.
Base = declarative_base()

# Get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    