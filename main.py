from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel


app = FastAPI(
    title="User Management System",
    description="A simple user management system using FastAPI. This API allows you to create, retrieve, and manage users.",
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

users = []

# Define user data model

class User(BaseModel):
    name: str
    is_active: bool
    username: Optional[str] = None


# define user response model
class UserResponse(BaseModel):
    data: List[User]
    total_count: int
    status: str


# Add a user

@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return {"message": "User added successfully", "status": "ok"}


# Get all users
@app.get("/users", response_model=UserResponse)
async def get_all_users():
    return {"data": users, "total_count": len(users), "status": "ok"}

# get a user

@app.get("/users/{user_id}")
async def get_user_by_id(user_id: int = Path(..., description="Enter a valid user id", gt=0),
                         query: Optional[str] = Query(None, description="Enter a valid query string", min_length=3)
                         ):
    if user_id < len(users) or user_id >= len(users):
        return {"data": users[user_id], "message": "success", "status": "ok"}
    else:
        return {"message": "Invalid user id", "status": "error"}

    