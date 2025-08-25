import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def gerar_kpis(df):
    # Garantir que as colunas necessárias existem
    """
    Calcula e exibe KPIs a partir do dataframe de vendas.

    KPIs:
    1. YTD (Total de vendas até a última data disponível)
    2. YoY (comparação % entre os dois últimos anos - número de vendas)
    3. YoY (comparação % entre os dois últimos anos - receita)

    Parâmetros:
    - df (pandas.DataFrame): dataframe com as colunas 'Year', 'Sales_Volume' e 'Price_USD'

    Retorna:
    None
    """
    if not all(col in df.columns for col in ["Year", "Sales_Volume", "Price_USD"]):
        st.warning("Colunas 'Year', 'Sales_Volume' ou 'Price_USD' não encontradas no dataframe.")
        return

    # --- KPI 1: YTD (Total de vendas até a última data disponível) ---
    ytd_total = df["Sales_Volume"].sum()

    # --- KPI 2: YoY (comparação % entre os dois últimos anos - número de vendas) ---
    vendas_por_ano = df.groupby("Year")["Sales_Volume"].sum().sort_index()
    if len(vendas_por_ano) >= 2:
        ano_atual, ano_anterior = vendas_por_ano.index[-1], vendas_por_ano.index[-2]
        vendas_atual = vendas_por_ano.loc[ano_atual]
        vendas_anterior = vendas_por_ano.loc[ano_anterior]
        yoy_vendas_pct = ((vendas_atual - vendas_anterior) / vendas_anterior) * 100
        yoy_vendas_diff = vendas_atual - vendas_anterior
    else:
        yoy_vendas_pct = 0
        yoy_vendas_diff = 0
        ano_atual, ano_anterior = None, None


    # --- KPI 3: YoY (comparação % entre os dois últimos anos - receita) ---
    df["Revenue"] = df["Sales_Volume"] * df["Price_USD"]
    receita_por_ano = df.groupby("Year")["Revenue"].sum().sort_index()
    if len(receita_por_ano) >= 2:
        receita_atual = receita_por_ano.loc[ano_atual]
        receita_anterior = receita_por_ano.loc[ano_anterior]
        yoy_receita_pct = ((receita_atual - receita_anterior) / receita_anterior) * 100
        yoy_receita_diff = receita_atual - receita_anterior
    else:
        yoy_receita_pct = 0
        yoy_receita_diff = 0
        ano_atual, ano_anterior = None, None


    # --- Layout dos KPIs ---
    st.subheader("Indicadores de Desempenho (KPIs)")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label=f"YTD {df['Year'].max()} | Número de Vendas Totais",
            value=f"{ytd_total:,.0f}"
        )

    with col2:
        if ano_atual and ano_anterior:
            st.metric(
                label=f"YoY | {ano_anterior} → {ano_atual} | Número de Vendas",
                value=f"{vendas_atual:,.0f}",
                delta=f"{yoy_vendas_diff:+,.0f} vendas ({yoy_vendas_pct:.2f}%)",
                delta_color="normal"
            )
        else:
            st.metric(label="YoY Vendas", value="Dados insuficientes")


    with col3:
        if ano_atual and ano_anterior:
            st.metric(
                label=f"YoY | {ano_anterior} → {ano_atual} | Receita (USD)",
                value=f"${receita_atual:,.2f}",
                # aqui o Streamlit interpreta automaticamente positivo/negativo
                delta=f"{yoy_receita_diff:,.2f} ({yoy_receita_pct:.2f}%)",
                delta_color="normal"  
            )
        else:
            st.metric(label="YoY Receita", value="Dados insuficientes")


