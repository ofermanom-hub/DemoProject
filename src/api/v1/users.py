from fastapi import APIRouter, Depends

from src.auth.jwt import get_current_user_id

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me")
async def get_me(user_id: str = Depends(get_current_user_id)) -> dict:
    return {"user_id": user_id}
