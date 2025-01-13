import fastapi
from models.users import UserAuth, UserResponseType

user_router = fastapi.APIRouter()

users = []

# Add a user
@user_router.post("")
async def create_user(user: UserAuth):
    users.append(user)
    return {"message": "User added successfully", "status": "ok"}

# Get all users
@user_router.get("", response_model=UserResponseType)
async def get_all_users():
    return {"data": users, "total_count": len(users), "status": "ok"}

# Get a user by id
@user_router.get("/{user_id}")
async def get_user_by_id(user_id: int):
    if 0 <= user_id < len(users):
        return {"data": users[user_id], "message": "success", "status": "ok"}
    else:
        return {"message": "Invalid user id", "status": "error"}
