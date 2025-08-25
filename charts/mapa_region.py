import streamlit as st
import pandas as pd
import plotly.express as px

def gerar_mapa_vendas(df: pd.DataFrame):
    """
    Gera um mapa interativo com Plotly mostrando a quantidade de veículos vendidos por região.
    
    Parâmetros:
    - df: DataFrame com colunas 'Region' e 'Sales_Volume'
    """
    # Verifica se as colunas necessárias estão no DataFrame
    if not all(col in df.columns for col in ["Region", "Sales_Volume"]):
        st.error("DataFrame deve conter as colunas: Region, Sales_Volume")
        return

    # Agrega Sales_Volume por Region
    sales_by_region = df.groupby("Region")["Sales_Volume"].sum().reset_index()
    
    # Renomear coluna para mudar a legenda
    sales_by_region = sales_by_region.rename(columns={"Sales_Volume": "Vendas"}) 

    region_mapping = {
        "Africa": [
            "DZA","AGO","BEN","BWA","BFA","BDI","CPV","CMR","CAF","TCD","COM","COG","COD","CIV",
            "DJI","EGY","GNQ","ERI","SWZ","ETH","GAB","GMB","GHA","GIN","GNB","KEN","LSO","LBR",
            "LBY","MDG","MWI","MLI","MRT","MUS","MYT","MAR","MOZ","NAM","NER","NGA","REU","RWA",
            "STP","SEN","SYC","SLE","SOM","ZAF","SSD","SDN","TZA","TGO","TUN","UGA","ESH","ZMB","ZWE"
        ],
        "Asia": [
            "AFG","ARM","AZE","BHR","BGD","BTN","BRN","KHM","CHN","GEO","IND","IDN","IRN",
            "JPN","KAZ","KWT","KGZ","LAO","MYS","MDV","MNG","MMR","NPL","PRK",
            "PAK","PHL","QAT","SGP","KOR","LKA","TWN","TJK","THA","TKM",
            "UZB","VNM"
        ],
        "Europe": [
            "ALB","AND","AUT","BLR","BEL","BIH","BGR","HRV","CYP","CZE","DNK","EST","FIN","FRA","DEU",
            "GRC","HUN","ISL","IRL","ITA","LVA","LIE","LTU","LUX","MLT","MDA","MCO","MNE","NLD","MKD",
            "NOR","POL","PRT","ROU","RUS","SMR","SRB","SVK","SVN","ESP","SWE","CHE","UKR","GBR","VAT"
        ],
        "North America": [
            "ATG","BHS","BRB","BLZ","CAN","CRI","CUB","DMA","DOM","SLV","GRD","GTM","HTI","HND","JAM",
            "MEX","NIC","PAN","KNA","LCA","VCT","TTO","USA"
        ],
        "South America": [
            "ARG","BOL","BRA","CHL","COL","ECU","GUY","PRY","PER","SUR","URY","VEN"
        ],
        "Middle East": [
            "BHR","CYP","IRN","IRQ","ISR","JOR","KWT","LBN","OMN","PSE","QAT","SAU","SYR","TUR","ARE","YEM"
        ]
    }


    # Cria uma lista para o DataFrame do mapa
    map_data = []
    for _, row in sales_by_region.iterrows():
        region = row["Region"]
        sales = row["Vendas"]
        if region in region_mapping:
            for iso_code in region_mapping[region]:
                map_data.append({"Region": region, "Vendas": sales, "iso_alpha": iso_code})

    map_df = pd.DataFrame(map_data)

    # Cria o mapa coroplético com Plotly
    fig = px.choropleth(
        map_data,
        locations="iso_alpha",
        color="Vendas",
        color_continuous_scale="Blues_r", 
        hover_name="Region",
        projection="natural earth"
    )

    fig.update_geos(
        showcountries=False,
        showcoastlines=False,
        showland=True,
        fitbounds="locations" 
    )

    # Atualiza o layout para tema escuro
    fig.update_layout(
        title=dict(
            text="Mapa com Número de Vendas por Continente",
            font=dict(size=20, color="#E0E0E0"),
            x=0,
        ),

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        geo=dict(
            bgcolor="rgba(0,0,0,0)",
            landcolor="rgba(255,255,255,0.1)",
            showframe=False,
            projection_type="natural earth"
        ),
        margin={"r": 0, "t": 50, "l": 0, "b": 0},
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)
