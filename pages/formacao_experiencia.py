import streamlit as st
from app import load_css

load_css("styles/styles.css")

st.markdown("<div class='section-container'>", unsafe_allow_html=True)

# Sobre mim
st.markdown("<h2 class='section-title'>Sobre Mim</h2>", unsafe_allow_html=True)
st.markdown(f"""
<div class='card'>
    <p class= 'text-justify'>
        Estudante de Engenharia de Software na FIAP (3º semestre) com foco em Desenvolvimento Full Stack, Integração de Sistemas IoT e Análise de Dados. Apaixonado por tecnologia desde 2016, iniciei minha jornada no Design Gráfico e, em 2023, ampliei meu conhecimento para desenvolvimento de software. Tenho experiência em projetos acadêmicos voltados para captação e visualização de dados. Busco oportunidades desafiadoras que promovam meu crescimento técnico e me permitam criar soluções inovadoras
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Formação
st.markdown("<h2 class='section-title'>Formação</h2>", unsafe_allow_html=True)
formation = [
    {"role": "Engenharia de Software", "company": "FIAP (Faculdade de Informática e Administração Paulista)", "period": "2024-2028"},
]
for form in formation:
    st.markdown(f"""
    <div class='card'>
        <h3>{form['role']}</h3>
        <p><strong>Faculdade:</strong> {form['company']}</p>
        <p><strong>Período:</strong> {form['period']}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# Experiencias
st.markdown("<h2 class='section-title'>Experiências</h2>", unsafe_allow_html=True)
experiences = [
    {
        "role": "Estágio em Análise de Dados", 
        "company": "ITAU Unibanco", "period": "Julho 2025 - atualmente", 
        "description": "Desenvolvimento de dashboards interativos utilizando Quicksight AWS, análise de grandes volumes de dados, criação de relatórios para suporte à tomada de decisão."
    },
]
for exp in experiences:
    st.markdown(f"""
    <div class='card'>
        <h3>{exp['role']}</h3>
        <p><strong>Empresa:</strong> {exp['company']}</p>
        <p><strong>Período:</strong> {exp['period']}</p>
        <p><strong>Descrição:</strong> {exp['description']}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# Certificados
st.markdown("<h2 class='section-title'>Certificados</h2>", unsafe_allow_html=True)
certificates = [
    {"title": "Python para Data Science", "issuer": "Alura", "year": "Novembro 2024"},
    {"title": "Analisando Dados com Pandas & SQL", "issuer": "Asimov Academy", "year": " Janeiro 2025"},
    {"title": "Fundamentos de AI e Machine Learning", "issuer": "Asimov Academy", "year": "Maio 2025"},
]
for cert in certificates:
    st.markdown(f"""
    <div class='card'>
        <h3>{cert['title']}</h3>
        <p><strong>Emissor:</strong> {cert['issuer']}</p>
        <p><strong>Ano:</strong> {cert['year']}</p>
    </div>
    """, unsafe_allow_html=True)

# Portfolio
st.markdown("<h2 class='section-title'>Portfolio</h2>", unsafe_allow_html=True)
portifolio = [
    {"role": "Portfolio", "link": "https://portfolio-nicolas-haubricht-silk.vercel.app/"},
]
for port in portifolio:
    st.markdown(f"""
    <div class='card'>
        <h3>{port['role']}</h3>
        <p><strong>Link de acesso:</strong> <a href="{port['link']}">{port['link']}</a></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

