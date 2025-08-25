import streamlit as st
import pandas as pd
import os
import plotly.express as px
from pages.home import home
from script.tratamento import tratar_dados

# --- 🔹 # Carregar Dataframe ja tratado | arquivo tratamento.pys ---
df = pd.read_csv("data/data_sales_bmw.csv")

# --- 🔹 Função para carregar CSS ---
def load_css(file_path):
    try:
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Arquivo CSS não encontrado: {file_path}")

# --- 🔹 Função para Navbar ---
def navbar(df):

    logo_path = os.path.abspath("img/logo.png")
    if os.path.exists(logo_path):
        st.logo(logo_path)
    else:
        st.warning("Logo não encontrado em: img/logo.png")

    pages = [
        st.Page(lambda: home(df), title="Home"),
        st.Page("pages/formacao_experiencia.py", title="Formação e Experiência"),
        st.Page("pages/skills.py", title="Minhas Skills"),
        st.Page("pages/analise_dados.py", title="Análise de Dados"),
        st.Page("pages/dashboard.py", title="Dashboard"),
    ]

    pg = st.navigation(pages)
    pg.run()

# --- 🔹 Função principal ---
def main():
    # Configurar layout
    st.set_page_config(page_title="BMW Sales Dashboard", layout="wide")
    # Carregar CSS uma única vez
    load_css("styles/styles.css")
    # Executar navegação
    navbar(df)

# Rodar aplicação
if __name__ == "__main__":
    main()