from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
def get_all_users():
    return {"message": "Here is all Users"}
