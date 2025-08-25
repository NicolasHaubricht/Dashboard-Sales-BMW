import streamlit as st
import pandas as pd
# from script.tratamento import tratar_dados
from charts.vendas_x_receita import vendas_x_receita
from charts.vendas_por_modelo import vendas_por_modelo
from charts.composicao_ano_modelo import composicao_ano_modelo
from charts.top3_modelos_vendas_preco import top3_modelos_vendas_preco
from charts.gerar_kpis import gerar_kpis
from charts.mapa_region import gerar_mapa_vendas
from charts.vendas_por_regiao import vendas_por_regiao

try:
    # Carregar Dataframe ja tratado | arquivo tratamento.py
    df = pd.read_csv("data/data_sales_bmw.csv")

    # Criar filtros na sidebar
    st.sidebar.header("Filtros")

    # Definir colunas que terão filtros
    filtros = {
        "Year": "anos",
        "Region": "regiões",
        "Model": "modelos",
        "Color": "cores",
        "Transmission": "transmissão",
        "Sales_Classification": "classificação de vendas"
    }

    # Criar um dicionário para armazenar a seleção do usuário
    selecoes = {}

    for coluna, label in filtros.items():
        opcoes = sorted(df[coluna].unique())
        selecoes[coluna] = st.sidebar.multiselect(
            f"Selecione {label}:",
            options=opcoes,
            default=opcoes
        )

    # Aplicar filtros de forma dinâmica
    df_filtrado = df.copy()
    for coluna, valores in selecoes.items():
        df_filtrado = df_filtrado[df_filtrado[coluna].isin(valores)]

    # --- 🔹 KPI ---
    gerar_kpis(df_filtrado)

    # --- 🔹 Gráfico Vendas X Receita ---
    vendas_x_receita(df_filtrado)

    # --- 🔹 Gráfico composição ano/modelo ---
    composicao_ano_modelo(df_filtrado)

    # Criar colunas
    col1, col2 = st.columns(2)

    with col1:
        # --- 🔹 Gráfico Barra dos Top 3 Modelos Mais Vendidos ---
        top3_modelos_vendas_preco(df_filtrado)
        # --- 🔹 Gráfico Mapa de Vendas por Continente ---
        gerar_mapa_vendas(df_filtrado)

    with col2:
        # --- 🔹 Gráfico Barra Vendas por Modelo ---
        vendas_por_modelo(df_filtrado)
        # --- 🔹 Gráfico Barra Venda por Continente ---
        vendas_por_regiao(df_filtrado)


    # --- 🔹 Tabela analítico ---
    df_analitico = df_filtrado.rename(columns={
        "Model": "Modelo",
        "Year": "Ano",
        "Region": "Região",
        "Color": "Cor",
        "Fuel_Type": "Tipo de Combustível",
        "Transmission": "Transmissão",
        "Engine_Size_L": "Economia (L)",
        "Mileage_KM": "Quilometragem (KM)",
        "Price_USD": "Preço (USD)",
        "Sales_Volume": "Volume de Vendas",
        "Sales_Classification": "Classificação de Vendas",
    })

    st.subheader("Analítico")
    st.dataframe(df_analitico[['Modelo', 'Ano', 'Região', 'Cor', 'Tipo de Combustível', 'Transmissão', 'Economia (L)', 'Quilometragem (KM)', 'Preço (USD)', 'Volume de Vendas', 'Classificação de Vendas']])

except FileNotFoundError:
    st.error("❌ Arquivo de dados não encontrado.")
