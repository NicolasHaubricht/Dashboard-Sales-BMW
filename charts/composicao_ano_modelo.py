import plotly.graph_objects as go
import pandas as pd
import streamlit as st
import plotly.express as px


def composicao_ano_modelo(df: pd.DataFrame):
    # Agrupa por ano e modelo
    vendas_ano_modelo = df.groupby(["Year", "Model"], as_index=False).agg({
        "Sales_Volume": "sum"
    })

    # Calcula o total por ano e a % de cada modelo
    vendas_ano_modelo["Total_Ano"] = vendas_ano_modelo.groupby("Year")["Sales_Volume"].transform("sum")
    vendas_ano_modelo["Percent"] = (vendas_ano_modelo["Sales_Volume"] / vendas_ano_modelo["Total_Ano"]) * 100

    # Cria figura
    fig = go.Figure()
    modelos = vendas_ano_modelo["Model"].unique()
    cores = px.colors.qualitative.Safe  # paleta de cores limpa

    for i, modelo in enumerate(modelos):
        dados_modelo = vendas_ano_modelo[vendas_ano_modelo["Model"] == modelo]
        fig.add_trace(go.Bar(
            x=dados_modelo["Year"],
            y=dados_modelo["Percent"],
            name=modelo,
            marker_color=cores[i % len(cores)],
            text=[f"{p:.1f}%" if p >= 5 else "" for p in dados_modelo["Percent"]],  # só mostra % se for relevante
            textposition="inside",
            textfont=dict(size=11, color="#FFFFFF")
        ))

    # Layout refinado
    fig.update_layout(
        template="plotly_dark",
        title=dict(
            text=f"Composição (%) de Vendas por Ano e Modelo ({df['Year'].min()} - {df['Year'].max()})",
            font=dict(size=20, color="#E0E0E0"),
            x=0
        ),
        xaxis=dict(
            title="Ano",
            tickmode="linear",
            dtick=1,
            titlefont=dict(size=14, color="#E0E0E0"),
            tickfont=dict(size=12, color="#E0E0E0"),
            showline=False,
            showgrid=False
        ),
        yaxis=dict(
            title="Participação (%)",
            showline=False,
            showgrid=False,
            zeroline=False,
            tickfont=dict(size=12, color="#E0E0E0"),
            ticksuffix="%"  # eixo Y em %
        ),
        legend=dict(
            x=0,
            y=1.15,
            orientation="h",
            font=dict(size=12, color="#E0E0E0"),
            bgcolor="rgba(0,0,0,0)"
        ),
        barmode="stack",
        bargap=0.15,
        height=500,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig, use_container_width=True)
