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


async def retrieve_todos():
    todos = []
    async for todo in todo_collection.find():
        todos.append(todo)
    return todos
