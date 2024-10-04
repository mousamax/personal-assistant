from fastapi import FastAPI
from tasks_agent import TasksAgent

app = FastAPI()

tasks_agent = TasksAgent()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/generate-todos/{user_query}")
def generate_todos(user_query: str):
    return {"todos": tasks_agent.generate_todos(user_query)}