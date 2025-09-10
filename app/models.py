from pydantic import BaseModel,Field
from typing import Optional,Annotated
from datetime import date
class CreateTask(BaseModel):
    title:str
    description:str|None=Field(
            default=None,
            title='this is the description of the task',
            max_length=300
          )
    due_date:Optional[date]=None
    completed:bool=Field(
        default=False
         )
class Task(CreateTask):
    id:int