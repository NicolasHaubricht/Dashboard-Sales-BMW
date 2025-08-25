import streamlit as st
import pandas as pd

def home(df: pd.DataFrame):
    
    st.markdown("""
    <style>
        body {
            overflow: hidden;
        }
        .main > .block-container {
            overflow: hidden !important;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0;
            padding: 0;
        }
        .center-text {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            text-align: center;
            margin: 0;
        }
        .bmw-logo {
            width: 100px;
            height: auto;
            margin-bottom: 15px;
        }
    </style>
    <div class='center-text'>
        <img src='https://upload.wikimedia.org/wikipedia/commons/4/44/BMW.svg' class='bmw-logo' alt='BMW Logo'>
        <h1 style='color: white; font-size: 2.5em; margin-bottom: 10px;'>BMW Dashboard</h1>
        <p style='color: gray; font-size: 1.2em;'>Análise de vendas (2010-2024)</p>
    </div>
    """, unsafe_allow_html=True)