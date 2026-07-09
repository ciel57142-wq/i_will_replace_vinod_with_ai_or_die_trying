from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="PM Assistant")

class Task(BaseModel):
    title: str
    description: str | None = None
    priority: int = 3

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/tasks")
def create_task(task: Task):
    # your logic here
    return {"received": task}