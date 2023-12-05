from typing import Optional
from pydantic import BaseModel, Field


class TodoSchema(BaseModel):
    title: str = Field(...)
    description: str = Field(...)
    is_important: bool = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "Lorem",
                "description": "this is the description",
                "is_important": True,
            }
        }


class UpdateTodoModel(BaseModel):
    title: Optional[str]
    description: Optional[str]
    is_important: Optional[bool]

    class Config:
        schema_extra = {
            "example": {
                "title": "Lorem",
                "description": "this is the description",
                "is_important": False,
            }
        }


def ResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message
    }


def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message,
    }
