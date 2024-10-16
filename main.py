from typing import List
from models.member import Member
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.tasks_agent import TasksAgent


class MembersRequest(BaseModel):
    user_query: str
    members: List[Member]

app = FastAPI()

tasks_agent = TasksAgent()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/generate-todos/{user_query}")
def generate_todos(user_query: str):
    todos = tasks_agent.generate_todos(user_query)

    if todos is None:
        raise HTTPException(status_code=404, detail="Unable to generate todos for the given query.")

    return {"todos": todos}

@app.post("/generate-todos/")
def generate_todos_with_members(request: MembersRequest):
    user_query = request.user_query
    members = request.members
    todos = tasks_agent.generate_todos_with_members(user_query, members)

    if todos is None:
        raise HTTPException(status_code=404, detail="Unable to generate todos for the given members.")

    return {"todos": todos}