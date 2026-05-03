"""
Pure business logic — no HTTP, no DB I/O here.
DB calls are injected via the repository pattern.
"""
from dataclasses import dataclass

from src.auth.password import hash_password, verify_password


@dataclass
class UserCreateDTO:
    email: str
    password: str


@dataclass
class UserDTO:
    id: int
    email: str
    is_active: bool


class UserService:
    """Orchestrates user domain logic."""

    @staticmethod
    def hash_new_password(dto: UserCreateDTO) -> str:
        return hash_password(dto.password)

    @staticmethod
    def authenticate(plain_password: str, hashed_password: str) -> bool:
        return verify_password(plain_password, hashed_password)
