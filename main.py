from typing import Annotated
from fastapi import Depends, FastAPI
from sqlmodel import SQLModel, Session
from routes import users, courses


from db.db_setup import engine
from utils import api_versions


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
    redoc_url=None,
    docs_url="/documentation"
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Include the routers
app.include_router(users.user_router,  prefix=f"/users", tags=["Users"])
app.include_router(courses.course_router, prefix=f"/courses", tags=["Courses"])
