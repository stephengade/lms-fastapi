from typing import Annotated
from fastapi import Depends, FastAPI
from sqlmodel import SQLModel, Session
from endpoints import users, courses

from database.db_setup import engine


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]


app = FastAPI(
    title="User Management System",
    description="A simple user management system. This API allows you to create, retrieve, and manage users.",
    version="0.0.1",
    terms_of_service="http://stephengade.com/work/",
    contact={
        "name": "Stephen Gbolagade",
        "url": "https://stephengade.com/contact/",
        "email": "hello@stephengade.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "http://www.apache.org/licenses/LICENSE-2.0.html",
    },
    redoc_url=None
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(users.router)
app.include_router(courses.router)
