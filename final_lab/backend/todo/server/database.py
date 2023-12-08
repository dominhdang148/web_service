from bson.objectid import ObjectId
import motor.motor_asyncio

MONGO_DATABASE = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DATABASE)
database = client.todo
todo_collection = database.get_collection("todo_collection")


# Helper


def todo_helper(todo):
    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "description": todo["description"]
    }


# Get all todos
async def get_todos():
    todos = []
    async for todo in todo_collection.find():
        todos.append(todo)
    return todos


# Add new todo
async def add_todo(todo_data: dict):
    todo = await todo_collection.insert_one(todo_data)
    new_todo = await todo_collection.find_one({"_id": todo.inserted_id})
    return todo_helper(new_todo)


# Get a todo matched with given ID
async def get_todo(id: str):
    todo = await todo_collection.find_one({"_id": ObjectId(id)})
    if todo:
        return todo_helper(todo)


# Update a todo with a matching ID
async def update_todo(id: str, data: dict):
    if len(data) < 1:
        return False
    student = await todo_collection.find_one({"_id": ObjectId(id)})
