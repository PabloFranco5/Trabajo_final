from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr


class UserBase(BaseModel):
    email: EmailStr = Field(...
    )
    username: str = Field(
        ...,
        min_length=3,
        max_length=50
    )


class User(UserBase):
    id: int = Field(...
    )


class UserRegister(UserBase):
    password: str = Field(
        ...,
        min_length=4,
        max_length=64
    )