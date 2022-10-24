from  pydantic import BaseModel, constr, Field


class UserBase(BaseModel):
    username: constr(min_length = 3, max_length = 32) = Field(..., examole="john")


class UserOut(UserBase):
    id: int = Field(..., example = 123)


class UserIn(UserBase):
    """
    Create user
    """
    friends = []