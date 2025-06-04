import streamlit as st
import functions

todos = functions.get_todos_from_file()

def add_todo():
    _todo = st.session_state["new_todo"] + '\n'
    todos.append(_todo)
    functions.write_todos_to_file(todos)
    st.session_state["new_todo"] = ""


st.title("My TODO App")
st.subheader("This is a todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos_to_file(todos)
        del st.session_state[todo] #This is needed for checkboxes
        st.rerun()


st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key="new_todo")