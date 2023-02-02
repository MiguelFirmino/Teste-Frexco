import pandas as pd


def prever_demanda(dados, dias_seguintes, ponderacao, cor):
    """
    Realizar a previsão de demanda por meio de Suavização Exponencial Simples,
    Gerar a previsão para os dias seguintes com base nos últimos cinco dias previstos 
    anteriormente (decidi usar esse parâmetro devido ao padrão nos dados de pico/vale 
    mais ou menos a cada cinco dias)
    Printar os valores previstos
    """
    demanda_historica = dados["Vendas"]
    # A primeira previsão é o valor real do primeiro dia
    demanda_prevista = [demanda_historica[0]]

    # Prever a demanda de cada dia com base no histórico já existente
    for index, demanda in enumerate(demanda_historica[1:], start=1):
        demanda_anterior = demanda_historica[index - 1]
        previsao_anterior = demanda_prevista[-1]

        previsao = previsao_anterior + ponderacao * (demanda_anterior - previsao_anterior)
        demanda_prevista.append(previsao)

    # Prever a demanda para os dias seguintes
    for _ in range(0, dias_seguintes):
        demanda_anterior = demanda_prevista[-5]
        previsao_anterior = demanda_prevista[-1]

        nova_previsao = previsao_anterior + ponderacao * (demanda_anterior - previsao_anterior)
        demanda_prevista.append(nova_previsao)
        print(nova_previsao)

filepath = "Dados.xlsx"
df = pd.read_excel(filepath, engine='openpyxl')  # Acessar e ler os dados

prever_demanda(dados=df, dias_seguintes=5, ponderacao=0.8, cor="r")