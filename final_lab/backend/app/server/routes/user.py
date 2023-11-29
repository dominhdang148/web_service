from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder


from server.database import (
    add_user,
    delete_user,
    retrieve_user,
    retrieve_users,
    update_user,
)


from server.models.user import (
    ErrorResponseModel,
    ResponseModel,
    UserSchema,
    UpdateUserModel,
)

router = APIRouter()


@router.post("/", response_description="User data added into the database")
async def add_user_data(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    new_user = await add_user(user)
    return ResponseModel(new_user, "User added successfully")


@router.get("/", response_description="User retrieved")
async def get_users():
    users = await retrieve_users()
    if users:
        return ResponseModel(users, "Users data retrieved successfully")
    return ResponseModel(users, "Empty list returned")


@router.get("/{id}", response_description="User data retrieved")
async def get_user_data(id):
    user = await retrieve_user(id=id)
    if user:
        return ResponseModel(user, "User data retrieved successfully")
    return ErrorResponseModel("An error occured", 404, "Student doesn't exist")


@router.put("/{id}", response_description="User data updated")
async def update_user_data(id: str, req: UpdateUserModel = Body(...)):
    req = {k: v for k, v in req.model_dump().items() if v is not None}
    updated_user = await update_user(id, req)
    if updated_user:
        return ResponseModel(
            data="Student with ID: {} name updated is successful".format(id),
            message="Student name updated successfully",
        )
    return ErrorResponseModel(
        error="An Error occured",
        code=404,
        message="There was an error updateing the student data"
    )


@router.delete("/{id}", response_description="User data deleted from the database")
async def delete_user_data(id: str):
    deleted_user = await delete_user(id=id)
    if deleted_user:
        return ResponseModel(
            data="Student with ID: {} removed".format(
                id),
            message="Student deleted successfully"
        )
    return ErrorResponseModel(
        error="An error occurred",
        code=404,
        message="Student with id {0} doesn't exitst".format(id)
    )
