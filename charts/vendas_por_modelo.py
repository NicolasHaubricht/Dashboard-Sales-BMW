import plotly.express as px
import streamlit as st

def vendas_por_modelo(df):
    vendas_modelo = df.groupby("Model", as_index=False)["Sales_Volume"].sum()
    vendas_modelo = vendas_modelo.sort_values("Sales_Volume", ascending=True) 

    # Renomear coluna para mudar a legenda
    vendas_modelo = vendas_modelo.rename(columns={"Sales_Volume": "Vendas"})

    fig = px.bar(
        vendas_modelo,
        x="Vendas",
        y="Model",
        orientation="h",
        text="Vendas",
        title="Total de Vendas por Modelo",
        color="Vendas",  # legenda será "Vendas"
    )

    # Formatação dos números em K/M no texto da barra
    fig.update_traces(
        texttemplate='%{x:.3s}',  # mantém K/M
        textposition="outside"
    )

    # Layout: remover ticks e título do eixo X
    fig.update_layout(
        xaxis=dict(
            showticklabels=False,  # remove os números
            title='',         # remove o título
            range=[0, vendas_modelo["Vendas"].max() * 1.2],
        ),
        yaxis=dict(title='Modelo'),
        title=dict(
            text="Total de Vendas por Modelo",
            font=dict(size=20, color="#E0E0E0"),
            x=0,
        ),
    )
    
    st.plotly_chart(fig, use_container_width=True)
