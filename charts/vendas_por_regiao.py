import plotly.express as px
import pandas as pd
import streamlit as st

def vendas_por_regiao(df):
    vendas_region = df.groupby("Region", as_index=False)["Sales_Volume"].sum()
    vendas_region = vendas_region.sort_values("Sales_Volume", ascending=True)

    # Renomear coluna para mudar a legenda
    vendas_region = vendas_region.rename(columns={"Sales_Volume": "Vendas"}) 

    fig = px.bar(
        vendas_region,
        x="Vendas",
        y="Region",
        orientation="h",
        text="Vendas",
        color="Vendas",
    )

    # formatação K / M nos textos
    fig.update_traces(
        texttemplate='%{x:.3s}',  # usa notação SI → 1.2k, 3.4M
        textposition="outside"
    )

    # formatação K / M no eixo também
    fig.update_layout(
        title=dict(
            text="Total de Vendas por Continente",
            font=dict(size=20, color="#E0E0E0"),
            x=0,
        ),
        xaxis=dict(
            showticklabels=False, 
            title='',
            range=[0, vendas_region["Vendas"].max() * 1.2],
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)
