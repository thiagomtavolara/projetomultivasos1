# Importação das bibliotecas necessárias
from dash import dcc, html, Input, Output, State, callback
import dash
import dash_bootstrap_components as dbc
from datetime import date, datetime
from utils import graficos
from assets.style.style import *  # Importe seu estilo personalizado aqui
from utils.graficos import plot_grafico_config

# Registro da página na aplicação
dash.register_page(__name__, path='/', title='Home')

# Geração de dados iniciais
x, y = graficos.initial_data()

# Layout dos cards
layout_grafico = dbc.Card([
    dbc.CardHeader("Gráfico".upper()),
    dbc.CardBody([
        dcc.Graph(id="grafico_config", figure={}, responsive=True),
    ])
])

layout_formulario = dbc.Card([
    dbc.CardHeader("Configurações".upper()),
    dbc.CardBody([
        dbc.Form([
            html.Div([
                html.Label('Selecione a variável:'),
                dcc.Dropdown(
                    id='variavel-dropdown',
                    options=[
                        {'label': 'Pesos', 'value': 'Pesos'},
                        {'label': 'Temperatura', 'value': 'Temperatura'},
                        {'label': 'Vazões', 'value': 'Vazoes'}
                    ],
                    value='Pesos'
                )
            ], style={'columnCount': 1}),
            html.Div([
                html.Label('Selecione a data do experimento:'),
                dcc.DatePickerSingle(
                    id='data-input',
                    date=date.today(),
                    display_format='DD/MM/YYYY',
                ),
            ], style={'columnCount': 1}),
            html.Div([
                html.Button('Aplicar', id='aplicar-config'),
            ],
                className="mb-3",
            ),
        ])
    ])
])

layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.Div([
            html.H5("Abaixo é possível escolher o experimento que deseja analisar, basta escolher a data do mesmo e o tipo de variável, depois só clicar no botão 'Aplicar'. Se quiser mudar o gráfico basta fazer o mesmo processo. Bom proveito!!!!",
                    style={"font-family": "Courier New", "margin-top": "20px", "font-size": "16px"}
                    ),
        ]), width={"size": 8, "offset": 2}, style={"margin-bottom": "20px", "text-align": "center"})
    ]),
    dbc.Row([
        dbc.Col(layout_grafico, md=8),
        dbc.Col(layout_formulario, md=4),
    ], style=ROW_STYLE),
], fluid=True)

# Callbacks para atualização do gráfico
@callback(
    Output('grafico_config', 'figure'),
    [Input('aplicar-config', 'n_clicks')],
    [State('data-input', 'date'),
     State('variavel-dropdown', 'value')],
    prevent_initial_call=True
)
def update_graph(n_clicks, data_experimento_selecionada, variavel):
    if n_clicks is None:
        raise dash.exceptions.PreventUpdate

    data_experimento_selecionada = datetime.strptime(data_experimento_selecionada, '%Y-%m-%d').strftime('%d-%m-%y')
    fig = plot_grafico_config(data_experimento_selecionada, variavel)
    return fig

# Execução da aplicação
if __name__ == '__main__':
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = layout
    app.run_server(debug=True)
