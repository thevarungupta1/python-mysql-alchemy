import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# we can also set these environment variables 
# DB_USER = os.getenv("DB_USER", "root")
# DB_PASS = os.getenv("DB_PASS", "root")
# DB_HOST = os.getenv("DB_HOST", "localhost")
# DB_NAME = os.getenv("DB_NAME", "test_db")

#DATABASE_URL = f"mysql+pymysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
DATABASE_URL = f"mysql+mysqlconnector://root:root@localhost/test_db"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)
# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

