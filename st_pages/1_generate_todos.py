import streamlit as st
from st_components.todos import todos_view
from agents.tasks_agent import TasksAgent

# Initialize the TasksAgent
tasks_agent = TasksAgent()

# Streamlit app
st.title("Smart Family Task List: Turn Your Family Situation into Actionable Steps")

st.markdown("Welcome to the Smart Family Task List! Managing a family situation can be overwhelming, but we’re here to help. Simply describe a situation you’re facing, and we’ll generate a personalized list of tasks with categories to help you stay organized and focus on what matters most – your family.")

st.markdown("### Let's get started! :rocket:")

st.divider()

# Collect user input
user_query = st.text_input("Tell us what’s happening (e.g., “The kindergarten called and my child is sick”)", placeholder="Explain your situation here...")

# Generate todos when the user submits a query
if st.button(":sparkles: Generate my smart task list"):
    if user_query:
        with st.spinner("familymind is generating your smart task list... :beer:"):
            #st.image("https://media.giphy.com/media/kyLYXonQYYfwYDIeZl/giphy.gif?cid=790b7611cicsergdo02m9pzp1t9v6sl3tjf8b72n0a5gotw8&ep=v1_gifs_trending&rid=giphy.gif&ct=g", use_column_width=True)
            todos = tasks_agent.generate_todos(user_query)
            todos_view(todos)
    else:
        st.error("Please enter a prompt.")

