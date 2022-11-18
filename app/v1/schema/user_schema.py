from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr


class UserBase(BaseModel):
    username: str = Field(
        ...,
        min_length=3,
        max_length=50
    )
    email: EmailStr = Field(
        ...,
        example="myemail@cosasdedevs.com"
    )
    punto_de_salida: str = Field(
        ...,
        min_length=3,
        max_length=50
    )
    punto_de_llegada: str = Field(
        ...,
        min_length=3,
        max_length=50
    )


class User(UserBase):
    id: int = Field(...
    )


