import streamlit as st

import pandas as pd

import plotly.express as px
 
st.set_page_config(

    page_title="Dashboard de Dados",

    layout="wide"

)
 
# Título

st.title("Despesa de Consumo Média Mensal Familiar")

st.subheader("São Paulo - 2008")
 
st.write(

    "Este dashboard apresenta uma análise das despesas de consumo "

    "média mensal das famílias de São Paulo no ano de 2008."

)
 
st.write(

    "O objetivo é identificar quais categorias apresentam os maiores "

    "e menores valores de despesas."

)
 
# Dados

dados = {

    "Categoria": [

        "Alimentação",

        "Habitação",

        "Vestuário",

        "Transporte",

        "Higiene e cuidados pessoais",

        "Assistência à saúde",

        "Educação",

        "Recreação e cultura",

        "Fumo",

        "Serviços pessoais",

        "Despesas diversas"

    ],
 
    "Valor": [

        508.11,

        972.82,

        132.29,

        547.81,

        57.50,

        220.72,

        97.25,

        58.31,

        18.16,

        32.71,

        83.00

    ]

}
 
df = pd.DataFrame(dados)
 
# Indicadores

quantidade_registros = len(df)

quantidade_categorias = df["Categoria"].nunique()

media_despesas = df["Valor"].mean()

maior_despesa = df["Valor"].max()
 
st.header("Indicadores")
 
col1, col2, col3, col4 = st.columns(4)
 
col1.metric(

    "Quantidade de registros",

    quantidade_registros

)
 
col2.metric(

    "Quantidade de categorias",

    quantidade_categorias

)
 
col3.metric(

    "Média das despesas",

    f"R$ {media_despesas:.2f}"

)
 
col4.metric(

    "Maior despesa",

    f"R$ {maior_despesa:.2f}"

)
 
# Verificação dos dados

st.header("Verificação dos dados")
 
col1, col2, col3 = st.columns(3)
 
col1.metric(

    "Valores nulos",

    df.isnull().sum().sum()

)
 
col2.metric(

    "Valores duplicados",

    df.duplicated().sum()

)
 
col3.write("Tipos de dados:")

col3.write(df.dtypes)
 
# Tabela

st.header("Dados das despesas")
 
st.dataframe(

    df,

    use_container_width=True

)
 
# Gráfico de barras

st.header("Despesas médias mensais por categoria")
 
fig = px.bar(

    df,

    x="Categoria",

    y="Valor",

    title="Despesas médias mensais por categoria em 2008",

    labels={

        "Categoria": "Categoria",

        "Valor": "Valor (R$)"

    }

)
 
fig.update_layout(

    xaxis_tickangle=-45

)
 
st.plotly_chart(

    fig,

    use_container_width=True

)
 
# Observações

st.subheader("O que podemos observar?")
 
st.write(

    "O gráfico mostra os valores das despesas médias mensais das "

    "famílias em diferentes categorias no ano de 2008."

)
 
st.write(

    "A categoria Habitação apresenta o maior valor, com R$ 972,82."

)
 
st.write(

    "Em seguida aparecem Transporte, com R$ 547,81, e Alimentação, "

    "com R$ 508,11."

)
 
st.write(

    "A menor despesa apresentada é Fumo, com R$ 18,16."

)
 
st.write(

    "Esses resultados mostram apenas os valores registrados na base "

    "de dados e não permitem afirmar o motivo dessas diferenças."

)
 
# Histograma

st.header("Distribuição dos valores das despesas")
 
fig_hist = px.histogram(

    df,

    x="Valor",

    nbins=6,

    title="Distribuição das despesas em 2008",

    labels={

        "Valor": "Valor (R$)",

        "count": "Quantidade de categorias"

    }

)
 
st.plotly_chart(

    fig_hist,

    use_container_width=True

)
 
# Observações do histograma

st.subheader("O que podemos observar?")
 
st.write(

    "O histograma mostra como os valores das diferentes categorias "

    "de despesas estão distribuídos."

)
 
st.write(

    "É possível perceber que existem categorias com valores bem "

    "menores e algumas com valores mais altos."

)
 
st.write(

    "A maior parte dos valores está abaixo de R$ 600, enquanto "

    "Habitação apresenta um valor bem mais alto, de R$ 972,82."

)
 
st.write(

    "O gráfico ajuda a visualizar a diferença entre os valores "

    "das categorias."

)
 
# Conclusão

st.header("Conclusão")
 
st.write(

    "Os dados analisados mostram que, em 2008, as categorias de "

    "despesas apresentam valores diferentes entre si."

)
 
st.write(

    "Habitação foi a categoria com maior valor registrado, enquanto "

    "Fumo apresentou o menor valor."

)
 
st.write(

    f"A média das despesas entre as 11 categorias analisadas foi de "

    f"R$ {media_despesas:.2f}."

)
 
# Fonte

st.header("Fonte dos dados")
 
st.write(

    "Fonte: IBGE - Pesquisa de Orçamentos Familiares (POF). "

    "Os dados utilizados apresentam as despesas de consumo média "

    "mensal familiar para São Paulo em 2008."

)
 
# Uso da IA

st.header("Uso da Inteligência Artificial")
 
st.write(

    "A Inteligência Artificial foi utilizada para auxiliar na "

    "organização do código Python, na criação dos gráficos com "

    "Plotly e na interpretação dos resultados apresentados no dashboard."

)
 
st.write(

    "Os resultados foram conferidos com os valores presentes na base de dados."

)
 
# Validação

st.header("Validação do dashboard")
 
st.write("O dashboard foi verificado considerando:")
 
st.write("""

- os dados utilizados;

- os valores das despesas;

- os gráficos apresentados;

- os títulos;

- os indicadores;

- as explicações dos gráficos;

- a fonte dos dados.

""")
 
st.write(

    "As informações apresentadas foram baseadas nos valores disponíveis "

    "na base de dados."

)
 