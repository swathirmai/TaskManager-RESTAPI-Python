from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from app.server.api.v1.endpoints.tasks import router as TasksRouter

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Application routes
app.include_router(TasksRouter, tags=["Tasks Management"], prefix="/tasks")

@app.get("/")
async def task_app():
   content = {"Message": "Your Task Manager for Daily Productivity...."}
   return JSONResponse(content=content, status_code=status.HTTP_200_OK)