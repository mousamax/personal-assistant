import streamlit as st
from st_components.todos import todos_view
from agents.tasks_agent import TasksAgent

# Initialize the TasksAgent
tasks_agent = TasksAgent()

# Streamlit app
st.title("Todo List Generator")

# Collect user input
user_query = st.text_input("Enter your prompt:")

# Generate todos when the user submits a query
if st.button("Generate Todos"):
    if user_query:
        todos = tasks_agent.generate_todos(user_query)
        todos_view(todos)
    else:
        st.error("Please enter a prompt.")

