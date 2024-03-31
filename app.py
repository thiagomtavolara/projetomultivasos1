from dash import html
import dash
import dash_bootstrap_components as dbc

# instancia a aplicação e define configurações
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True, pages_folder="pages",
    suppress_callback_exceptions=True, assets_folder="assets")

# título da aplicação
app.title = 'multivasos-dashboard'

server = app.server
app.layout = html.Div([
    dbc.NavbarSimple(
        children=[
        # Adiciona logos
        dbc.NavItem(dbc.NavLink(
            html.A(
            html.Img(
                src=app.get_asset_url('figures/gimscop.png'),
                style={
                    'height' : '28px',
                }),
                href="https://www.ufrgs.br/gimscop/",
                ),
            )
        ),

        # Adiciona página ao dropdown
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Home", href=dash.page_registry['pages.home']['path']),
                dbc.DropdownMenuItem("Tempo Real", href=dash.page_registry['pages.update']['path']),
                dbc.DropdownMenuItem("Sobre", href=dash.page_registry['pages.sobre']['path']),
            ],
            # adiciona dropdown de navegação
            nav=True,
            in_navbar=True,
            label="Mais páginas",
        ),

        ],

        # Branding
        brand="Multivasos",
        brand_href=dash.page_registry['pages.home']['path'],
        color="dark",
        dark=True,
    ),

    # adiciona páginas
    dash.page_container
    ],
)


if __name__ == "__main__":
    # faz com que seja possível acessar o serviço por computador externo ao que está executando
    import socket
    host = socket.gethostbyname(socket.gethostname())

    # roda a aplicação
    app.run_server(debug=True, host=host, dev_tools_ui=True)

