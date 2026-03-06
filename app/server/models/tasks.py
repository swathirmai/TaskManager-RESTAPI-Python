from pydantic import BaseModel, Field
from typing import Optional, Union
from datetime import datetime


class TasksSchema(BaseModel):
   name: str = Field(...)
   description: str = Field(...)
   task_status: str = Field(...)
   priority: str = Field(...)
   due_date: str = Field(...)
   created_at: Union[datetime, None] = None
   updated_at: Union[datetime, None] = None

   class Config:
      json_schema_extra = {
         "example": [
            {
               "name":"Read a Book",
               "description":"Read a book on entreprenurship for 2 hours",
               "task_status":"completed",
               "priority":"p1",
               "due_date": "2023-09-10",
               "created_at":"2023-09-10T23:23:35.403+00:00",
               "updated_at":"2023-09-10T23:23:35.403+00:00"
            }
         ]
      }

class UpdateTasksSchema(BaseModel):
   name: str = Field(...)
   description: str = Field(...)
   task_status: str = Field(...)
   priority: str = Field(...)
   due_date: str = Field(...)
   updated_at: Union[datetime, None] = None

   class Config:
      json_schema_extra = {
         "example": [
            {
               "name":"Read a Book",
               "description":"Read a book on entreprenurship for 2 hours",
               "task_status":"completed",
               "priority":"p1",
               "due_date": "2023-09-10",
            }
         ]
      }