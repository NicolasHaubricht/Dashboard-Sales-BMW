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

def vendas_x_receita(df: pd.DataFrame):
    # Calcula a receita estimada
    df["Price_Orc"] = df["Price_USD"] * df["Sales_Volume"]

    # Agrupa por ano e agrega as colunas necessárias
    vendas_ano = df.groupby("Year", as_index=False).agg({
        "Sales_Volume": "sum",
        "Price_Orc": "sum"
    })

    # Define uma paleta de tons de cinza para as barras
    num_anos = len(vendas_ano)
    cores_barras = [f"rgb({50 + i * (150 / max(1, num_anos-1))}, {50 + i * (150 / max(1, num_anos-1))}, {50 + i * (150 / max(1, num_anos-1))})" for i in range(num_anos)]

    # Cria o gráfico
    fig = go.Figure()

    # Adiciona as barras para o volume de vendas
    fig.add_trace(go.Bar(
        x=vendas_ano["Year"],
        y=vendas_ano["Sales_Volume"],
        name="Vendas (Volume)",
        marker_color="#C9C9C9",
        yaxis="y1",
        text=[formatar_valor(v) for v in vendas_ano["Sales_Volume"]],
        textposition="outside",
        textfont=dict(size=12, color="#E0E0E0")
    ))

    # Adiciona a linha para a receita estimada
    fig.add_trace(go.Scatter(
        x=vendas_ano["Year"],
        y=vendas_ano["Price_Orc"],
        name="Receita (USD)",
        mode="lines+markers+text",
        line=dict(color="#2CCD00", width=3),
        marker=dict(size=8),
        yaxis="y2",
        text=["$"+formatar_valor(v) for v in vendas_ano["Price_Orc"]],
        textposition="top center",
        textfont=dict(size=9, color="#00500C")
    ))

    # Atualiza o layout para tema escuro, fundo transparente e eixos Y invisíveis
    fig.update_layout(
        template="plotly_dark",
        title=dict(
            text=f"Vendas x Receita ({df['Year'].min()} - {df['Year'].max()})",
            font=dict(size=20, color="#E0E0E0"),
            x=0,
        ),
        xaxis=dict(
            title="Ano",
            tickmode="linear",
            tick0=vendas_ano["Year"].min(),
            dtick=1,
            titlefont=dict(size=14, color="#E0E0E0"),
            tickfont=dict(size=12, color="#E0E0E0")
        ),
        yaxis=dict(
            title="",
            side="left",
            titlefont=dict(size=14, color="#E0E0E0"),
            tickfont=dict(size=12, color="#E0E0E0"),
            showline=False,  # Oculta a linha do eixo
            showgrid=False,  # Oculta as linhas de grade
            showticklabels=False,  # Oculta os rótulos dos ticks
            zeroline=False  # Oculta a linha de zero
        ),
        yaxis2=dict(
            title="",
            overlaying="y",
            side="right",
            titlefont=dict(size=14, color="#E0E0E0"),
            tickfont=dict(size=12, color="#E0E0E0"),
            showline=False,  # Oculta a linha do eixo
            showgrid=False,  # Oculta as linhas de grade
            showticklabels=False,  # Oculta os rótulos dos ticks
            zeroline=False,  # Oculta a linha de zero
            tickformat="$,.0s"
        ),
        legend=dict(
            x=0,
            y=1.15,
            orientation="h",
            font=dict(size=12, color="#E0E0E0"),
            bgcolor="rgba(0,0,0,0)"
        ),
        barmode="group",
        bargap=0.3,
        height=500,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig, use_container_width=True)