from fastapi import FastAPI,HTTPException
from models import CreateTask,Task
from database import tasks
app=FastAPI()
#CREATING A TASK
@app.post('/tasks/',response_model=Task)
async def create_task(task:CreateTask):
    new_id=len(tasks)+1
    new_task=Task(id=new_id,**task.dict())
    tasks.append(new_task)
    return new_task
#STATS
@app.get('/tasks/stats')
async def show_stat():
     total_tasks=len(tasks)
     completed_tasks=sum(1 for i in tasks if i.completed)
     pending_tasks=total_tasks-completed_tasks
     percentage=(completed_tasks/total_tasks*100) if total>0 else 0
     return{
        'Total Tasks':total_tasks,
        'Completed Tasks':completed_tasks,
        'Pending Tasks':pending_tasks,
        'Percentage of Completed tasks':percentage
     }
#SELECT TASK 
@app.get('/tasks/{id}',response_model=Task)
async def select(id:int):
    for task in tasks:
        if task.id==id:
            return task
    raise HTTPException(status_code=404,detail='task not found')
#SHOW ALL TASKS
@app.get('/tasks/')
async def showAll():
    return tasks
#UPDATE TASKS
@app.put('/tasks/{id}',response_model=Task)
async def update(id:int,updated:CreateTask):
    for i,task in enumerate(tasks):
        if task.id==id:
            tasks[i]=Task(id=id,**updated.dict())
            return tasks[i]
    raise HTTPException(status_code=404,detail='task not found')
#DELETE TASK
@app.delete('/tasks/{id}')
async def delete(id:int):
    for i,task in enumerate(tasks):
        if task.id==id:
            tasks.pop(i)
            return{'message':f'Successfully deleted task(id={id})'}
    raise HTTPException(status_code=404,detail='task not found')
