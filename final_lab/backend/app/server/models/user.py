from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    vip_level: int = Field(..., gt=0, lt=9)
    score: float = Field(..., le=4.0)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Đỗ Minh Đăng",
                "email": "dominhdang@gmail.com",
                "vip_level": 3,
                "score": "2.0",
            }
        }


class UpdateUserModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    vip_level: Optional[int]
    score: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Đỗ Minh Đăng",
                "email": "dominhdang@gmail.com",
                "vip_level": 5,
                "score": "4.0",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message,
    }
