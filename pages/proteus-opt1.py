import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(page_title="Proteus Dashboard",
                   layout="wide")

session_key = 'df'

df = pd.read_excel(
    io='proteus_python_one.xlsx',
    engine='openpyxl',
    sheet_name='Standard_Civil',
    usecols='A:H',
)

with st.sidebar.form("my_form"):
    input_mgd_min = st.number_input(
        "Enter your minimum MGD", min_value=0.0, max_value=500.0, value=1.0, step=0.1,)
    input_mgd_max = st.number_input(
        "Enter your maximum MGD", min_value=0.0, max_value=500.0, value=1.0, step=0.1,)

    input_lv = st.number_input(
        "Enter your LV", min_value=4, max_value=20, value=4, step=1,)

    type = st.sidebar.multiselect(
        "Select the Type:",
        options=df["TYPE"].unique(),
        default=df["TYPE"].unique()
    )

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.session_state["input_mgd_min"] = input_mgd_min
        st.session_state["input_mgd_max"] = input_mgd_max
        st.session_state["input_lv"] = input_lv


if "input_mgd_min" not in st.session_state:
    st.session_state["input_mgd_min"] = 1

if "input_mgd_max" not in st.session_state:
    st.session_state["input_mgd_max"] = 500


if "input_lv" not in st.session_state:
    st.session_state["input_lv"] = 4

df_selection = df.query(
    "TYPE == @type & LV == @input_lv & @input_mgd_min <= MGD <= @input_mgd_max "
)

st.dataframe(df_selection)
