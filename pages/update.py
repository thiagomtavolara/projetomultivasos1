import os
from dash import dcc, html, Input, Output, State, callback, MATCH, ALL
import dash
import dash_bootstrap_components as dbc

# importa bibliotecas próprias
from utils import graficos
from assets.style.style import *

# Obrigatório! Adiciona a página na aplicação. Mudar o nome e o caminho para a página
dash.register_page(__name__, path='/update', title='Update')

# Cards bootstrap - elementos básicos da página

# gráfico simples
layout_grafico_atualizado = dbc.Card([
    # título do card
    dbc.CardHeader("Gráfico atualizado".upper()),
    # corpo do card - aqui podemos adicionar qualquer elemento HTML
    dbc.CardBody([
        dcc.Graph(id="grafico_atualizado", figure={}),
    ])
])

# layout para solicitar informações ao usuário
layout_configuracoes = dbc.Card([
    dbc.CardHeader("Configurações".upper()),
    dbc.CardBody([
        # inicia formulário
        dbc.Form([
            html.Div([
                dbc.Label("P0 Inicial"),
                dbc.Input(id="input-p0-inicial", type="number", placeholder="P0 Inicial"),
            ], className="mb-3"),
            html.Div([
                dbc.Label("P1 Inicial"),
                dbc.Input(id="input-p1-inicial", type="number", placeholder="P1 Inicial"),
            ], className="mb-3"),
            html.Div([
                dbc.Label("P2 Inicial"),
                dbc.Input(id="input-p2-inicial", type="number", placeholder="P2 Inicial"),
            ], className="mb-3"),
            html.Div([
                dbc.Label("P3 Inicial"),
                dbc.Input(id="input-p3-inicial", type="number", placeholder="P3 Inicial"),
            ], className="mb-3"),
            html.Div([
                dbc.Label("T0 Mínimo"),
                dbc.Input(id="input-t0-minimo", type="number", placeholder="T0 Mínimo"),
            ], className="mb-3"),
            html.Div([
                dbc.Label("T0 Máximo"),
                dbc.Input(id="input-t0-maximo", type="number", placeholder="T0 Máximo"),
            ], className="mb-3"),
            html.Div([
                dbc.Label("T1 Mínimo"),
                dbc.Input(id="input-t1-minimo", type="number", placeholder="T1 Mínimo"),
            ], className="mb-3"),
            html.Div([
                dbc.Label("T1 Máximo"),
                dbc.Input(id="input-t1-maximo", type="number", placeholder="T1 Máximo"),
            ], className="mb-3"),
            html.Div([
                dbc.Label("T2 Mínimo"),
                dbc.Input(id="input-t2-minimo", type="number", placeholder="T2 Mínimo"),
            ], className="mb-3"),
            html.Div([
                dbc.Label("T2 Máximo"),
                dbc.Input(id="input-t2-maximo", type="number", placeholder="T2 Máximo"),
            ], className="mb-3"),
            html.Div([
                dbc.Label("T3 Mínimo"),
                dbc.Input(id="input-t3-minimo", type="number", placeholder="T3 Mínimo"),
            ], className="mb-3"),
            html.Div([
                dbc.Label("T3 Máximo"),
                dbc.Input(id="input-t3-maximo", type="number", placeholder="T3 Máximo"),
            ], className="mb-3"),
            # Botão de aplicar
            html.Div([
                dbc.Button("Aplicar", id="btn-aplicar", color="primary", className="mr-1"),
            ], className="mb-3")
        ])
    ])
])

# Layout - organiza os cards na página
layout = dbc.Container([
    # elemento responsável pela atualização do dash em tempo real
    dcc.Interval(
        id="trigger_classe",
        disabled=False,
        interval=1*1000,  # taxa de atualização em ms
        n_intervals=0,
    ),

    # adiciona uma linha
    dbc.Row([
        # adicionar uma nova coluna com o formulário
        dbc.Col(layout_configuracoes, md=4),
        # adiciona uma nova coluna com o gráfico
        dbc.Col(layout_grafico_atualizado, md=8),
    ]),
    dcc.Store(id='data-store') # Adicionando dcc.Store para armazenar dados
], fluid=True)

# Callbacks para criar ou atualizar o arquivo .txt
@callback(
    Output('data-store', 'data'),
    [Input('btn-aplicar', 'n_clicks')],
    [State('input-p0-inicial', 'value'),
     State('input-p1-inicial', 'value'),
     State('input-p2-inicial', 'value'),
     State('input-p3-inicial', 'value'),
     State('input-t0-minimo', 'value'),
     State('input-t0-maximo', 'value'),
     State('input-t1-minimo', 'value'),
     State('input-t1-maximo', 'value'),
     State('input-t2-minimo', 'value'),
     State('input-t2-maximo', 'value'),
     State('input-t3-minimo', 'value'),
     State('input-t3-maximo', 'value')]
)
def apply_settings(n_clicks, p0_inicial, p1_inicial, p2_inicial, p3_inicial, t0_min, t0_max, t1_min, t1_max, t2_min, t2_max, t3_min, t3_max):
    if n_clicks is not None:
        # Definindo o nome do arquivo
        filename = "informacoes.txt"

        # Criando ou atualizando o arquivo
        with open(filename, "w") as file:
            file.write(f"P0 Inicial: {p0_inicial}\n")
            file.write(f"P1 Inicial: {p1_inicial}\n")
            file.write(f"P2 Inicial: {p2_inicial}\n")
            file.write(f"P3 Inicial: {p3_inicial}\n")
            file.write(f"T0 Mínimo: {t0_min}\n")
            file.write(f"T0 Máximo: {t0_max}\n")
            file.write(f"T1 Mínimo: {t1_min}\n")
            file.write(f"T1 Máximo: {t1_max}\n")
            file.write(f"T2 Mínimo: {t2_min}\n")
            file.write(f"T2 Máximo: {t2_max}\n")
            file.write(f"T3 Mínimo: {t3_min}\n")
            file.write(f"T3 Máximo: {t3_max}\n")

    return {}

# Criando a aplicação Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Configurando o layout da página
app.layout = layout

# Rodando a aplicação
if __name__ == '__main__':
    app.run_server(debug=True)
