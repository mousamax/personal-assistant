import streamlit as st

st.set_page_config(page_title="familymind", page_icon="🧠", layout="centered")


generate_todos_pg = st.Page("./st_pages/1_generate_todos.py", title="Generate Todos", icon="🧠")

pages = st.navigation([generate_todos_pg])

pages.run()
