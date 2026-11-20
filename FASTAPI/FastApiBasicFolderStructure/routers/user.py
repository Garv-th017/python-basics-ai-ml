from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
def get_users():
    return {"message": "Get all users"}


@router.get("/{user_id}")
def get_user(user_id: int):
    return {"message": f"Get user {user_id}"}


@router.post("/")
def create_user():
    return {"message": "User created successfully"}
