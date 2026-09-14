from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class TaskCreate(BaseModel):
    title:str


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