from fastapi import APIRouter

from .schemas import UserOut, UserIn

router = APIRouter(
    prefix = "/users",
    tags = ["Users"],
)


@router.get("", response_model = list[UserOut])
def list_users() -> list[UserOut]:
    return [UserOut(id = 1, username = "john")]


@router.post("", response_model = UserOut)
def create_user(user_in: UserIn) -> UserOut:
    return UserOut(id = 0, **user_in.dict())
