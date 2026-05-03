from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr

from src.auth.jwt import create_access_token
from src.auth.password import verify_password, hash_password

router = APIRouter(prefix="/auth", tags=["auth"])


# --- Schemas ---
class RegisterRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


# Stub in-memory store — replace with DB repo
_USERS: dict[str, str] = {}


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(body: RegisterRequest) -> dict:
    if body.email in _USERS:
        raise HTTPException(status_code=409, detail="Email already registered")
    _USERS[body.email] = hash_password(body.password)
    return {"message": "User created"}


@router.post("/token", response_model=TokenResponse)
async def login(body: RegisterRequest) -> TokenResponse:
    hashed = _USERS.get(body.email)
    if not hashed or not verify_password(body.password, hashed):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(body.email)
    return TokenResponse(access_token=token)
