import streamlit as st
from app import load_css

load_css("styles/styles.css")

# Cabeçalho com logo, título e subtítulo
st.markdown("""
    <div class='center-text'>
        <h1 style='color: white; font-size: 2.5em; margin-bottom: 10px;'>BMW Análise de Dados</h1>
        <p style='color: gray; font-size: 1.2em;'>Análise de vendas (2010-2024)</p>
    </div>
    """, 
unsafe_allow_html=True)

# Contextualização: Contextualização
st.markdown("""
    <div>
        <h2>Contextualização</h2>
        <p class='text-justify'>
            A análise de resultados de vendas é essencial para empresas como a BMW, líder no setor automotivo de luxo. 
            Compreender as tendências de vendas ao longo do tempo permite identificar padrões de mercado, avaliar o desempenho de produtos 
            e estratégias de precificação, além de apoiar a tomada de decisões estratégicas. Para a BMW, que opera em um mercado competitivo 
            e global, monitorar métricas como volume de vendas e receita estimada é crucial para otimizar operações, planejar lançamentos de 
            novos modelos e manter a liderança no segmento premium. Este dashboard oferece uma visão clara desses indicadores, facilitando 
            insights acionáveis para o negócio.
        </p>
    </div>
    """, unsafe_allow_html=True
)

# Citação da fonte dos dados
st.markdown("""
    <div>
        <h2>Fonte dos Dados</h2>
        <p class='text-justify'>
            Os dados utilizados neste dashboard foram extraídos do Kaggle: 
            (<a href='https://www.kaggle.com/datasets/y0ussefkandil/bmw-sales2010-2024/'>www.kaggle.com</a>). Estes dados fornecem informações detalhadas sobre vendas globais e desempenho financeiro 
            entre 2010 e 2024. Para análises específicas, os dados foram agregados e tratados conforme descrito na seção a seguir.
        </p>
    </div>
    """, unsafe_allow_html=True
)

# Explicação sobre o tratamento de dados
st.markdown("""
    <div>
        <h2>Tratamento de Dados</h2>
        <p class='text-justify'>
            Os dados utilizados neste dashboard passaram por um processo rigoroso de tratamento para garantir precisão e confiabilidade. 
            As etapas incluíram:
            <ul>
                <li><strong>Limpeza de Dados:</strong> Verificação e remoção de valores nulos ou duplicados em todas as colunas.</li>
                <li><strong>Conversão dos Tipos de Dados:</strong> Conversão de colunas para tipos adequados, como int, float e string.</li>
                <li><strong>Criação de Novas Colunas:</strong> Criação de colunas derivadas, para auxiliar nas análises, como por exemplo: Flag_New, Flag_Old, Flag_Recent,Flag_EcoEngine, Flag_Luxury, Flag_TopSeller, Flag_LowSeller.</li>
                <li><strong>Validação:</strong> Verificação da consistência dos dados, como a ausência de valores negativos para volume de vendas ou preços.</li>
            </ul>
            Essas etapas asseguram que os dados estejam prontos para análises robustas, como as exibidas nos gráficos de vendas e receita.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Declaração dos tipos de variáveis
st.markdown("""
    <div>
        <h2>Tipos de Variáveis</h2>
        <p class='text-justify'>
            As colunas do conjunto de dados possuem os seguintes tipos de variáveis:
            <table class='variable-table'>
                <tr>
                    <th>Variável</th>
                    <th>Descrição</th>
                </tr>
                <tr>
                    <td>Model</td>
                    <td>Variável categórica nominal, indicando o modelo do veículo</td>
                </tr>
                <tr>
                    <td>Year</td>
                    <td>Variável numérica contínua, representando o ano de fabração do veículo</td>
                </tr>
                <tr>
                    <td>Region</td>
                    <td>Variável categórica nominal, indicando a região (Continente) de venda do veículo</td>
                </tr>
                <tr>
                    <td>Color</td>
                    <td>Variável categórica nominal, indicando a cor do veículo</td>
                </tr>
                <tr>
                    <td>Fuel_Type</td>
                    <td>Variável categórica nominal, indicando o tipo de combustível do veículo</td>
                </tr>
                <tr>
                    <td>Transmission</td>
                    <td>Variável categórica nominal, indicando a transmissão do veículo</td>
                </tr>
                <tr>
                    <td>Engine_Size_L</td>
                    <td>Variável numérica contínua, representando o tamanho do motor do veículo</td>
                </tr>
                <tr>
                    <td>Mileage_KM</td>
                    <td>Variável numérica contínua, representando a quilometragem em KM do veículo</td>
                </tr>
                <tr>
                    <td>Price_USD</td>
                    <td>Variável numérica contínua, representando o preço em USD da venda do veículo</td>
                </tr>
                <tr>
                    <td>Sales_Volume</td>
                    <td>Variável numérica contínua, representando o volume de vendas por modelo de veículo</td>
                </tr>
                <tr>
                    <td>Sales_Classification</td>
                    <td>Variável categórica ordinal, indicando a classificação de vendas do veículo</td>
                </tr>
            </table>
            Esses tipos de variáveis permitem análises temporais e financeiras detalhadas, como as exibidas no dashboard.
        </p>
    </div>
    """, unsafe_allow_html=True
)