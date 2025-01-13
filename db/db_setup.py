from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, create_engine
import os
from dotenv import load_dotenv

load_dotenv()

APP_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(APP_DATABASE_URL, future=True)

def get_session():
    try:
        with Session(engine) as session:
            yield session
    except Exception as e:
        print(f"Session error: {e}")
        raise

SessionDep = Annotated[Session, Depends(get_session)]