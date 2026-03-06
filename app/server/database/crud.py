from app.server.database.database_connection import tasks
from app.server.models.tasks import TasksSchema, UpdateTasksSchema
from bson.objectid import ObjectId

# Create the necessary endpoints to handle CRUD operations for tasks (Create, Read, Update, Delete).

# Create task
async def create_task_db(task: TasksSchema):
    task = task.model_dump()
    try:
        # print("Inside create task function")
        new_task = await tasks.insert_one(task)
        get_new_task = await tasks.find_one({"_id": new_task.inserted_id})
        return get_new_task
    except Exception as e:
        return {"Error_message":str(e)}

# Get one task
async def get_single_task_db(id: str):
    try:
        task = await tasks.find_one({"_id":ObjectId(id)})
        if task:
            return task
    except Exception as e:
        return {"Error_message": str(e)}

# Get all tasks
async def get_all_tasks_db():
    task_data = []
    try:
        get_all_tasks = tasks.find()
        if get_all_tasks:
            async for task in get_all_tasks:
                task_data.append(task)
            return task_data
    except Exception as e:
        return {"Error_message": str(e)}

# Update one task
async def update_single_task_db(id: str, task_data: UpdateTasksSchema):
    task = task_data.model_dump()
    try:
        update_task = await tasks.update_one({"_id":ObjectId(id)}, {"$set":{
            "name":task["name"],
            "description": task["description"],
            "priority": task["priority"],
            "task_status": task["task_status"],
            "due_date": task["due_date"],
            "updated_at": task["updated_at"]
        }})
        if update_task:
            get_task = await tasks.find_one({"_id":ObjectId(id)})
            return get_task
    except Exception as e:
        return {"Error_message": str(e)}
    
# Delete one task
async def delete_single_task_db(id: str):
    try:
        result = await tasks.delete_one({"_id":ObjectId(id)})
        return {"message":"Successfully Deleted task", "result":result}
    except Exception as e:
        return {"Error_message": str(e)}

# Delete all tasks
async def delete_all_tasks_db():
    try:
        result = await tasks.delete_many({})
        return {"message":"All Database Deleted"}
    except Exception as e:
        return {"Error_message": str(e)}