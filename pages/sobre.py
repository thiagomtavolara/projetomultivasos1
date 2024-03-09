from dash import html
import dash
import dash_bootstrap_components as dbc


dash.register_page(__name__, path='/sobre', title='Sobre')

layout = dbc.Container([

dbc.Row(
[
    dbc.Col([
        html.H1(children='Título da página'),
        html.Div(children='''
            Utilizar HTML para escrever sobre a aplicação.
        '''),

        html.H2(children='Subtítulo'),
        html.Div(children='''
            Continuar com a descrição.
        '''),
    ]
    ),
],
),

])
