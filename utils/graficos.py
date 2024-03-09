# importa estilos utilizados no dashboard
import assets.style.style as stl


def initial_data(seed=123):
    import numpy as np

    ### cria dados iniciais
    np.random.seed(seed=seed)
    x = np.arange(100)
    y = np.random.randn(100)

    return x, y

def update_data(x, y):
    import numpy as np

    # Adiciona um novo ponto
    new_x = x[-1] + 1
    new_y = np.random.randn(1)

    x = np.append(x, new_x)
    y = np.append(y, new_y)

    return x, y

def plot_grafico_simples(x, y):
    """
    Retorna um gráfico simples estático
    """
    import plotly.express as px
    import numpy as np
    import pandas as pd

    df = pd.DataFrame(zip(x, y), columns=['x', 'y'])

    ### plota o gráfico
    fig = px.scatter(df, x='x', y='y', color_discrete_sequence=stl.COLORS)

    # Padronização de design do gráfico
    fig.update_layout(
        xaxis_title="Tempo",
        yaxis_title="",
    )

    return fig

def plot_grafico_simples_online(x, y):
    import plotly.express as px
    import pandas as pd

    df = pd.DataFrame(zip(x, y), columns=['x', 'y'])

    # Plota o gráfico
    fig = px.scatter(df, x='x', y='y', color_discrete_sequence=stl.COLORS)

    # Padronização de design do gráfico
    fig.update_layout(
        xaxis_title="Tempo",
        yaxis_title="",
        xaxis=dict(
            rangeslider=dict(
                visible=True
            ),
            type="linear"
        )
    )

    return fig


import os
import plotly.express as px
import numpy as np
import pandas as pd
import plotly.graph_objects as go

def plot_grafico_config(data_experimento_selecionada, variavel):
    # Define o diretório de trabalho para o diretório onde o arquivo está localizado
    directory_path = r"C:\Users\usuario\Documents\multivasos - testes\experimentos"
    os.chdir(directory_path)

    # Obtém o caminho completo do arquivo
    file_path = os.path.join(directory_path, data_experimento_selecionada + ".npz")

    # Verifica se o arquivo existe
    if not os.path.exists(file_path):
        return px.scatter(title="Arquivo não encontrado: ")

    # Carrega os dados do arquivo
    dados = np.load(file_path)
    df = pd.DataFrame({key: dados[key].flatten() for key in dados.files})

    # Verifica se os dados estão vazios
    if df.empty:
        return px.scatter(title="Dados vazios")

    # Plotagem do gráfico
    contador = 0
    acabou = False
    while not acabou:
        flag = False
        for k in dados:
            if (k != "T0_sp") and (k != "T1_sp") and (k != "T2_sp") and (k != "T3_sp") and (k != "PWM") and (k != "B1") and (k != "B2") and (k != "B3"):
                if (dados[k][contador] != 0) and (k != "listatempo"):
                    acabou = False
                    flag = True
                elif flag == False:
                    acabou = True
        contador += 1

    if variavel == "Pesos":
        graficopeso = px.line(title = "Massas vs Tempo", height = 400, width = 900)
        graficopeso.update_yaxes(title = "Massa (g)")
        graficopeso.update_xaxes(title = "Tempo (min)")
        graficopeso.add_trace(go.Scatter(x=(dados["listatempo"][:contador-1])/60, y=dados["P0"][:contador], name="P0"),secondary_y=False,)
        graficopeso.add_trace(go.Scatter(x=(dados["listatempo"][:contador-1])/60, y=dados["P1"][:contador], name="P1"),secondary_y=False,)
        graficopeso.add_trace(go.Scatter(x=(dados["listatempo"][:contador-1])/60, y=dados["P2"][:contador], name="P2"),secondary_y=False,)
        graficopeso.add_trace(go.Scatter(x=(dados["listatempo"][:contador-1])/60, y=dados["P3"][:contador], name="P3"),secondary_y=False,)
        return graficopeso

    if variavel == "Temperatura":
        graficotemperatura = px.line(title = "Temperatura vs Tempo", height = 400, width = 900)
        graficotemperatura.update_yaxes(title = "Temperatura (°C)")
        graficotemperatura.update_xaxes(title = "Tempo (min)")
        graficotemperatura.add_trace(go.Scatter(x=(dados["listatempo"][:contador-1])/60, y=dados["T0"][:contador], name="T0"),secondary_y=False,)
        graficotemperatura.add_trace(go.Scatter(x=(dados["listatempo"][:contador-1])/60, y=dados["T1"][:contador], name="T1"),secondary_y=False,)
        graficotemperatura.add_trace(go.Scatter(x=(dados["listatempo"][:contador-1])/60, y=dados["T2"][:contador], name="T2"),secondary_y=False,)
        graficotemperatura.add_trace(go.Scatter(x=(dados["listatempo"][:contador-1])/60, y=dados["T3"][:contador], name="T3"),secondary_y=False,)
        graficotemperatura.add_trace(go.Scatter(x=(dados["listatempo"][:contador-1])/60, y=dados["T0_sp"][:contador], name="T0_sp", line = dict(width=2, dash='dot', color ='gray')),secondary_y=False)
        graficotemperatura.add_trace(go.Scatter(x=(dados["listatempo"][:contador-1])/60, y=dados["T1_sp"][:contador], name="T1_sp",line = dict(width=2, dash='dashdot', color ='gray')),secondary_y=False)
        graficotemperatura.add_trace(go.Scatter(x=(dados["listatempo"][:contador-1])/60, y=dados["T2_sp"][:contador], name="T2_sp",line = dict(width=2, dash='dash', color ='gray')),secondary_y=False)
        graficotemperatura.add_trace(go.Scatter(x=(dados["listatempo"][:contador-1])/60, y=dados["T3_sp"][:contador], name="T3_sp",line = dict(width=2, dash='longdash', color ='gray')),secondary_y=False)
        return graficotemperatura

    if variavel == "Vazoes":
        graficovazoes = px.line(title = "Vazões vs Tempo", height = 400, width = 900)
        graficovazoes.update_yaxes(title = "Vazões")
        graficovazoes.update_xaxes(title = "Tempo (min)")
        graficovazoes.add_trace(go.Scatter(x=(dados["listatempo"][:contador-1])/60, y=dados["PWM"][:contador], name="PWM relé"),secondary_y=False,)
        graficovazoes.add_trace(go.Scatter(x=(dados["listatempo"][:contador-1])/60, y=dados["B1"][:contador], name="V1"),secondary_y=False,)
        graficovazoes.add_trace(go.Scatter(x=(dados["listatempo"][:contador-1])/60, y=dados["B2"][:contador], name="V2"),secondary_y=False,)
        graficovazoes.add_trace(go.Scatter(x=(dados["listatempo"][:contador-1])/60, y=dados["B3"][:contador], name="V3"),secondary_y=False,)

        return graficovazoes
