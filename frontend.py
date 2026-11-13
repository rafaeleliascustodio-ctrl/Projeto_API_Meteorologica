
import streamlit as st

# Importa a função do consumidor
from consumidor_api import obter_dados_meteorologicos

# Configuração da página
st.set_page_config(
    page_title="Estação Meteorológica",
    page_icon="🌡️",
    layout="wide"
)

# Título da aplicação
st.title("🌡️ Estação Meteorológica")

st.write("Monitoramento meteorológico")

st.caption("Jaraguá do Sul — Santa Catarina")

# Tenta consultar e apresentar os dados
try:

    # Indica que os dados estão sendo buscados
    with st.spinner("Buscando informações..."):

        dados = obter_dados_meteorologicos()

    # Informa que a consulta funcionou
    st.success("Consulta realizada com sucesso!")

    st.subheader("Condições meteorológicas")

    # Primeira linha de indicadores
    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Temperatura",
        f"{dados['temperatura']} °C"
    )

    col2.metric(
        "Umidade",
        f"{dados['umidade']} %"
    )

    col3.metric(
        "Sensação térmica",
        f"{dados['sensacao']} °C"
    )

    # Segunda linha de indicadores
    col4, col5 = st.columns(2)

    col4.metric(
        "Precipitação",
        f"{dados['precipitacao']} mm"
    )

    col5.metric(
        "Velocidade do vento",
        f"{dados['vento']} km/h"
    )

    # Apresenta o horário informado pela API
    st.subheader("Horário da informação")

    st.write(dados["horario"])

# Trata erros durante a consulta ou apresentação
except Exception as erro:

    st.error(f"Não foi possível obter os dados: {erro}")
