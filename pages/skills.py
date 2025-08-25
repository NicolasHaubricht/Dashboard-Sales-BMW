import streamlit as st
from app import load_css

load_css("styles/styles.css")

# Cabeçalho
st.markdown("""
    <div class='center-text'>
        <h1 style='color: white; font-size: 2.5em; margin-bottom: 10px;'>Minhas Skills</h1>
    </div>
    """, 
unsafe_allow_html=True)

# Skills
st.markdown("""
    <div>
        <h2>Habilidades Técnicas</h2>
        <ul>
            <li>AWS</li>
            <li>Python</li>
            <li>SQL</li>
            <li>Git e GitHub</li>
        </ul>
    </div>
    """, unsafe_allow_html=True
)

# Idiomas
st.markdown("""
    <div>
        <h2>Idiomas</h2>
        <ul>
            <li>Inglês: intermediário</li>
            <li>Espanhol: básico</li>
        </ul>
    </div>
    """, unsafe_allow_html=True
)