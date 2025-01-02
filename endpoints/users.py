import fastapi
from database.models.users import UserAuth, UserResponseType


router = fastapi.APIRouter()

# import the user types here

users = []

# Add a user
@router.post("/users")
async def create_user(user: UserAuth):
    users.append(user)
    return {"message": "User added successfully", "status": "ok"}

# Get all users
@router.get("/users", response_model=UserResponseType)
async def get_all_users():
    return {"data": users, "total_count": len(users), "status": "ok"}

# Get a user
@router.get("/users/{user_id}")
async def get_user_by_id(user_id: int):
    if 0 <= user_id < len(users):
        return {"data": users[user_id], "message": "success", "status": "ok"}
    else:
        return {"message": "Invalid user id", "status": "error"}