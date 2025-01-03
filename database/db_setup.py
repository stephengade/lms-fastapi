from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, create_engine

APP_DATABASE_URL = "postgresql+psycopg2://user:password@localhost/fast_db"

engine = create_engine(APP_DATABASE_URL, future=True)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
