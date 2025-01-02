
from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlmodel import Session, create_engine

# sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"

APP_DATABASE_URL = "postgresql+psycopg2://user:password@localhost/fast_db"
CONNECT_ARGS = {}

engine = create_engine(APP_DATABASE_URL, connect_args=CONNECT_ARGS, future=True)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

# Base = declarative_base()


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]