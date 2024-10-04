from fastapi import FastAPI, HTTPException
from tasks_agent import TasksAgent

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