
import requests

# Endereço da API meteorológica
url = "http://127.0.0.1:8000/v1/forecast"

# Coordenadas de Jaraguá do Sul
parametros = {
    "latitude": -26.4851,
    "longitude": -49.0713
}

# Função responsável por buscar os dados
def obter_dados_meteorologicos():

    # Faz a requisição HTTP GET
    resposta = requests.get(
        url,
        params=parametros,
        timeout=15
    )

    # Verifica se ocorreu erro HTTP
    resposta.raise_for_status()

    # Converte a resposta JSON para Python
    dados = resposta.json()

    # Acessa as condições meteorológicas atuais
    atual = dados["current"]

    # Organiza os dados em um dicionário
    resultado = {
        "temperatura": atual["temperature_2m"],
        "umidade": atual["relative_humidity_2m"],
        "sensacao": atual["apparent_temperature"],
        "precipitacao": atual["precipitation"],
        "vento": atual["wind_speed_10m"],
        "horario": atual["time"]
    }

    # Devolve os dados para o frontend
    return resultado
