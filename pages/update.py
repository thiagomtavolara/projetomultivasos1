    # importa biblitecas gerais
from dash import dcc, html, Input, Output, State, callback, MATCH, ALL
import dash
import dash_bootstrap_components as dbc

# importa bibliotecas próprias
from utils import graficos
from assets.style .style import *

# Obrigatório! Adiciona a página na aplicação. Mudar o nome e o caminho para a página
dash.register_page(__name__, path='/update', title='Update')


#%% Cards bootstrap - elementos básicos da página

# gráfico simple
layout_grafico_atualizado = dbc.Card([
    # título do card
    dbc.CardHeader("Gráfico atualizado".upper()),
    # coporto do card - aqui podemos adiciar qualquer elemento HTML
    dbc.CardBody([
            dcc.Graph(id="grafico_atualizado", figure={}),
        ])
    ],
)

layout_configuracoes = dbc.Card([
    dbc.CardHeader("Configurações".upper()),
    dbc.CardBody([

        # inicia fomulário
        dbc.Form([

                html.Div(
                    [
                    dbc.Checkbox(id="checkbox-dados-atuais", 
                        value=True, 
                        label="Atualizar em Tempo Real"),
                    ],
                    # adiciona margem abaixo
                    className="mb-3",
                ),


                html.Div(
                    [
                        dbc.Label("Número de pontos plotados", html_for="variaveis"),
                        dbc.Input(id="input-num-pontos", 
                                value=100, 
                                type="number", 
                                placeholder="Número de Pontos", 
                                min=10, 
                                step=1),
                                ],
                    # adiciona margem abaixo
                    className="mb-3",
                ),

        ])
    ])
])

#%% Layout - organiza os cards na página
layout = dbc.Container(
    [
    # elemento responsável pela atualização do dash em tempo real
    dcc.Interval(
        id="trigger_classe",
        disabled=False,
        interval=1*1000,  # taxa de atualização em ms
        n_intervals=0,
    ),
    
    # adicina uma linha 
    dbc.Row(
        [
            # adiciona uma nova coluna com o gráfico
            dbc.Col(layout_grafico_atualizado, md=8),
            # adicionar uma nova coluna com o formulário
            dbc.Col(layout_configuracoes, md=4),
        ],
        style=ROW_STYLE,
        ),
    dcc.Store(id='data-store') # Adicionando dcc.Store para armazenar dados
    ],
    fluid=True,
)

#%% Callbacks
# Callback para atualizar os dados
@callback(
    Output('data-store', 'data'),
    Input('trigger_classe', 'n_intervals'),
    State('data-store', 'data'))
def update_data(n_intervals, stored_data):
    if stored_data is None:
        x, y = graficos.initial_data()  # Obtém dados iniciais
    else:
        x, y = stored_data['x'], stored_data['y']
        x, y = graficos.update_data(x, y)  # Atualiza dados

    return {'x': x, 'y': y}


# Callback para atualizar o gráfico com base no estado do checkbox
@callback(
    Output('grafico_atualizado', 'figure'),
    [Input('data-store', 'data'), Input('checkbox-dados-atuais', 'value')],
    [State('input-num-pontos', 'value')])
def update_graph_with_live_update(data, is_live_update, num_pontos):
    if data is None or not is_live_update:
        return dash.no_update

    x, y = data['x'], data['y']

    # Se a atualização em tempo real não estiver ativa, limita os pontos
    if num_pontos is not None:
        x, y = x[-num_pontos:], y[-num_pontos:]

    return graficos.plot_grafico_simples_online(x, y)

