import streamlit as st

st.set_page_config(
    page_title="Proteus App",
)

st.title("Proteus Water AI")
st.sidebar.success("Select a page above.")


if "project_name" not in st.session_state:
    st.session_state["project_name"] = ""

project_name = st.text_input(
    "What is the name of the project?", st.session_state["project_name"])


submit = st.button("Submit")
if submit:
    st.session_state["project_name"] = project_name
    st.write("The project name is ", project_name)
