import pandas as pd
import streamlit as st

def carregar_arquivo():
    uploaded_file = st.file_uploader("Escolha um arquivo .csv ou .txt", type=["csv", "txt"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file, sep=';', encoding='latin1')
        return df
    return None