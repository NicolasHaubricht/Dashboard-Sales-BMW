import plotly.graph_objects as go
import pandas as pd
import streamlit as st

def formatar_valor(valor):
    """Formata valores grandes com abreviações (K, M, B)."""
    if abs(valor) >= 1_000_000_000:
        return f"{valor / 1_000_000_000:,.1f}B"
    elif abs(valor) >= 1_000_000:
        return f"{valor / 1_000_000:,.1f}M"
    elif abs(valor) >= 1_000:
        return f"{valor / 1_000:,.1f}K"
    else:
        return f"{valor:,.0f}"

def top3_modelos_vendas_preco(df: pd.DataFrame):
    # Agrupa por modelo
    resumo = df.groupby("Model").agg({
        "Sales_Volume": "sum",
        "Price_USD": "mean"
    }).reset_index()

    # Seleciona os 3 mais vendidos
    top3 = resumo.sort_values("Sales_Volume", ascending=False).head(3)

    # Cria a figura
    fig = go.Figure()

    # Barras -> Vendas
    fig.add_trace(go.Bar(
        x=top3["Model"],
        y=top3["Sales_Volume"],
        name="Vendas",
        marker_color="#C9C9C9",
        text=[formatar_valor(v) for v in top3["Sales_Volume"]],
        textposition="outside",
        yaxis="y1"
    ))

    # Linha -> Preço médio
    fig.add_trace(go.Scatter(
        x=top3["Model"],
        y=top3["Price_USD"],
        name="Preço Médio (USD)",
        mode="lines+markers+text",
        marker=dict(color="#2CCD00", size=10),
        line=dict(color="#2CCD00", width=3),
        text=["$"+formatar_valor(v) for v in top3["Price_USD"]],
        textposition="top center",
        textfont=dict(size=10, color="#00500C"),
        yaxis="y2"
    ))

    # Layout com eixos ocultos e formatação
    fig.update_layout(
        title=dict(
            text="Top 3 Modelos Mais Vendidos x Preço Médio",
            font=dict(size=20, color="#E0E0E0"),
            x=0,
        ),
        xaxis=dict(
            title="Modelos",
            tickfont=dict(size=12, color="#E0E0E0")
        ),
        yaxis=dict(
            title="",
            showline=False,
            showgrid=False,
            showticklabels=False,
            zeroline=False
        ),
        yaxis2=dict(
            title="",
            overlaying="y",
            side="right",
            showline=False,
            showgrid=False,
            showticklabels=False,
            zeroline=False
        ),
        legend=dict(
            x=0,
            y=1.15,
            orientation="h",
            font=dict(size=12, color="#E0E0E0"),
            bgcolor="rgba(0,0,0,0)"
        ),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white"),
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)
