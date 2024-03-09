# importa bibliotecas gerais
from dash import dcc, html, Input, Output, State, callback
import dash
import dash_bootstrap_components as dbc

# Importa a biblioteca de data
from datetime import date

# importa bibliotecas próprias
from utils import graficos
from assets.style.style import *
from utils.graficos import plot_grafico_config

# Obrigatório! Adiciona a página na aplicação. Mudar o nome e o caminho para a página
dash.register_page(__name__, path='/', title='Home')

# gera dados iniciais
x, y = graficos.initial_data()

#%% Cards bootstrap - elementos básicos da página
# gráfico simples - gráfico estático que não depende de entradas


# gráfico com callbacks
layout_grafico = dbc.Card([
    dbc.CardHeader("Gráfico".upper()),
    dbc.CardBody([
        dcc.Graph(id="grafico_config", figure={}),
    ])
])

# layout do formulário
layout_formulario = dbc.Card([
    dbc.CardHeader("Configurações".upper()),
    dbc.CardBody([
        # exemplo de descrição dentro do card

        # inicia formulário
        dbc.Form([
            # adiciona componentes para o formulário
            # dropdown para escolher a variável
            html.Div(
                [
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
                ], style={'columnCount': 1}
            ),
            # input para inserir a data do experimento
            html.Div(
                [
                    html.Label('Selecione a data do experimento:'),
                    dcc.DatePickerSingle(
                        id='data-input',
                        date=date.today(),
                        display_format='DD/MM/YYYY',
                    ),
                ], style={'columnCount': 1}
            ),
            # botão
            html.Div(
                [
                    html.Button('Aplicar', id='aplicar-config'),
                ],
                className="mb-3",
            ),
        ])
    ])
])



# Layout - organiza os cards na página
layout = dbc.Container(
    [
        # Adiciona o texto desejado acima dos gráficos
        dbc.Row(
            dbc.Col(
                html.Div(
                    [
                        html.H5("Abaixo é possível escolher o experimento que deseja analisar, basta escolher a data do mesmo e o tipo de variável, depois só clicar no botão 'Aplicar'. Se quiser mudar o gráfico basta fazer o mesmo processo. Bom proveito!!!!",
                                style={"font-family": "Courier New", "margin-top": "20px", "font-size": "16px"}
                                ),
                    ]
                ),
                width={"size": 8, "offset": 2},
                style={"margin-bottom": "20px", "text-align": "center"}
            )
        ),

        # Adiciona outra linha
        dbc.Row(
            [
                # Adiciona uma nova coluna - md representa quantas partes de 12 a coluna irá utilizar. Para md=8, o card utiliza 8/12 da linha
                dbc.Col(layout_grafico, md=8),
                # Para md=4, o card utiliza 4/12 da linha
                dbc.Col(layout_formulario, md=4),
            ],
            style=ROW_STYLE,
        ),
    ],
    fluid=True,
)





#%% Callbacks - executa quando existe alguma ação na página
from datetime import datetime

@callback(
    Output('grafico_config', 'figure'),
    [Input('aplicar-config', 'n_clicks')],
    [State('data-input', 'date'),
     State('variavel-dropdown', 'value')],
    prevent_initial_call=True
)
def update_graph(n_clicks, data_experimento_selecionada, variavel):
    """
    Executa a função plot_grafico_config sempre que o botão é pressionado. Utiliza a data do experimento como entrada para gerar o gráfico.
    """

    # Aqui você pode usar o número de cliques para determinar se o botão foi pressionado
    if n_clicks is None:
        raise dash.exceptions.PreventUpdate

    # Convertendo a data para o formato esperado
    data_experimento_selecionada = datetime.strptime(data_experimento_selecionada, '%Y-%m-%d').strftime('%d-%m-%y')

    # Chame a função para gerar o gráfico com os dados atualizados
    return plot_grafico_config(data_experimento_selecionada, variavel)


# Callback para atualizar o gráfico com tabs
@callback(
    Output('tabs-content-example-graph', 'children'),
    Input('tabs-example-graph', 'value')
)
def update_graph_tab(tab):
    """
    Recebe a tab selecionada e gera um gráfico com o layout baseado na seleção.
    """

    # se tab-1
    if tab == 'tab-1-example-graph':
        fig = graficos.plot_grafico_simples(x, y)

    # se tab-2
    else:
        fig = graficos.plot_grafico_simples(x, y)
        fig.update_traces(marker=dict(symbol='square', size=20, line=dict(width=3)))

    return html.Div([
        dcc.Graph(
            id="grafico_tab",
            figure=fig),
    ])

# execute a aplicação
if __name__ == '__main__':
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = layout
    app.run_server(debug=True)
