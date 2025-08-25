import pandas as pd
import numpy as np
import streamlit as st

def tratar_dados(df: pd.DataFrame) -> pd.DataFrame:

    '''
    Função para tratar o dataset de vendas da BMW.
    Realiza as seguintes operações:
    - Verificar colunas com valores ausentes
    - Verificar linhas totalmente vazias
    - Verificar colunas totalmente vazias
    - Verificar se há índices NaN
    - Criar flags principais
    - Criar flags de preços
    - Criar flags de vendas
    - Converter tipos de dados
    - Retornar o DataFrame tratado
    '''

    # --- Cria cópia do dataset ---
    df_copy = df.copy()

    # # --- Verificar colunas com valores ausentes ---
    # missing = df.isnull().sum()
    # st.write("🔎 Valores ausentes por coluna:", missing)

    # # --- Verificar linhas totalmente vazias ---
    # empty_rows = df_copy[df_copy.isnull().all(axis=1)]
    # st.write("🔎 Total de linhas completamente vazias:", len(empty_rows))

    # # --- Verificar colunas totalmente vazias ---
    # empty_cols = df_copy.columns[df_copy.isnull().all()]
    # st.write("🔎 Total de linhas completamente vazias:", list(empty_cols))

    # # --- Verificar se há índices NaN ---
    # nan_index = df_copy.index[df_copy.index.isnull()]
    # st.write("🔎 Índices NaN encontrados:", len(nan_index))

    df_copy['id'] = df_copy.reset_index(drop=True).index
    
    # --- Flags principais ---
    df_copy["Flag_New"] = df_copy["Mileage_KM"].apply(lambda x: 1 if x < 1000 else 0)
    df_copy["Flag_Old"] = df_copy["Year"].apply(lambda x: 1 if x < 2019 else 0)
    df_copy["Flag_Recent"] = df_copy["Year"].apply(lambda x: 1 if x >= 2020 else 0)
    df_copy["Flag_EcoEngine"] = df_copy["Engine_Size_L"].apply(lambda x: 1 if x < 1.8 else 0)

    # --- Flags Preço ---
    median_price = df_copy["Price_USD"].median()
    df_copy["Flag_Luxury"] = df_copy["Price_USD"].apply(lambda x: 1 if x > median_price else 0)

    # --- Flags Vendas ---
    percent_75 = df_copy["Sales_Volume"].quantile(0.75)
    percent_25 = df_copy["Sales_Volume"].quantile(0.25)
    df_copy["Flag_TopSeller"] = df_copy["Sales_Volume"].apply(lambda x: 1 if x > percent_75 else 0)
    df_copy["Flag_LowSeller"] = df_copy["Sales_Volume"].apply(lambda x: 1 if x < percent_25 else 0)

    # --- Conversão de tipos ---
    df_copy["Model"] = df_copy["Model"].astype(str)
    df_copy["Sales_Classification"] = df_copy["Sales_Classification"].astype(str)
    df_copy["Year"] = df_copy["Year"].astype(int)
    df_copy["Mileage_KM"] = df_copy["Mileage_KM"].astype(int)
    df_copy["Sales_Volume"] = df_copy["Sales_Volume"].astype(int)
    df_copy["Engine_Size_L"] = df_copy["Engine_Size_L"].astype(float)
    df_copy["Price_USD"] = df_copy["Price_USD"].astype(float)

    return df_copy