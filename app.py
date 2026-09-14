from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app=FastAPI()

class TaskCreate(BaseModel):
    title:str

#we are not using database so these variables will keep track of the tasks and their ids in our in-memory storage
tasks=[]
next_id=1

@app.get("/")
def home():
    return {"Message":"TODO API is running"}

@app.post("/tasks")
def add_task(task:TaskCreate):
    global next_id

    new_task={
        "id":next_id,
        "title":task.title,
        "done": False
    }

    tasks.append(new_task)
    next_id+=1
    return new_task

@app.get("/tasks")
def list_tasks():
    return tasks

@app.patch("/tasks/{task_id}/done")
def mark_task_done(task_id:int):
    for task in tasks:
        if task["id"]==task_id:
            task["done"]= True
            return task

    raise HTTPException(status_code=404,detail="Task id not found")