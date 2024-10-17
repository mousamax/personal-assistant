import streamlit as st

def todos_view(todos):
    # Group todos by category
    grouped_todos = {}
    for todo in todos:
        category = todo['category']
        if category not in grouped_todos:
            grouped_todos[category] = []
        grouped_todos[category].append(todo['description'])

    # Display todos grouped by category
    with st.form("my_form"):
        for category, descriptions in grouped_todos.items():
            st.header(category)
            for description in descriptions:
                st.checkbox(description)
        st.form_submit_button("Done :beer:")