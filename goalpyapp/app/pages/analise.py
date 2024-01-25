import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="FVJ JOGOS DO DIA",
    page_icon=":bar_chart:",
    layout="wide",
)
st.title("Análise GoalPy ⚽")

st.markdown(
    """
    <span style="color: blue">**Faça aqui suas análises dos seus  jogos para suas estrátegia ⭐**</span><br>
    <span style="color: #FFC048">**Por Francisco Vito Júnior.**</span>  
    <span style="color: green">*boas análises!!!*</span>  
    """,
    unsafe_allow_html=True,
)


with st.sidebar:
    st.sidebar.header("Proximos Jogos")
    st.sidebar.image("goalpyapp/goalpy_texture_00092.tif", use_column_width=True)