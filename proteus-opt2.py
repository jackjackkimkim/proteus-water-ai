import pandas as pd
import plotly_express as px
import streamlit as st


st.set_page_config(page_title="Proteus Dashboard",
                   layout="wide")


df = pd.read_excel(
    io='proteus_python.xlsx',
    engine='openpyxl',
    sheet_name='Standard_Civil',
)


# --Sidebar----
st.sidebar.header("Please Filter Here:")
type = st.sidebar.multiselect(
    "Select the Type:",
    options=df["TYPE"].unique(),
    default=df["TYPE"].unique()
)

lv = st.sidebar.multiselect(
    "Select the LV:",
    options=df["LV"].unique(),
    default=df["LV"].unique()
)

input_mgd_min = st.sidebar.number_input(
    "Enter your minimum MGD", min_value=0.0, max_value=500.0, value=1.0, step=0.1,)

input_mgd_max = st.sidebar.number_input(
    "Enter your maximum MGD", min_value=0.0, max_value=500.0, value=1.0, step=0.1,)

# input_lv = st.sidebar.number_input(
#     "Enter your LV", min_value=4, max_value=20, value=4, step=1,)
# MGD == @input_mgd & LV = @input_lv


df_selection = df.query(
    "TYPE == @type & LV == @lv & @input_mgd_min <= MGD <= @input_mgd_max"
)

st.dataframe(df_selection)
