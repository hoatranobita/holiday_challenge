from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash
from apps import general, about, services, contract, predict

FA = "https://use.fontawesome.com/releases/v5.12.1/css/all.css"
FA2 = "https://use.fontawesome.com/releases/v6.0.0/css/all.css"
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app = dash.Dash(__name__,
                suppress_callback_exceptions=True,
                meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
                external_stylesheets=[dbc.themes.LUX,FA,FA2,dbc_css],
                title='Holiday Challenge'
                )

server = app.server

app.layout = html.Div(children=html.Div(
    [dcc.Location(id="url"),
        dbc.NavbarSimple(
            children=[
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Menu",
                align_end=True,
                children=[
                    dbc.DropdownMenuItem("Home", href='/'),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Analysis by Services", href='/page-2'),
                    dbc.DropdownMenuItem("Analysis by Contracts", href='/page-3'),
                    dbc.DropdownMenuItem("Churn Prediction", href='/page-4'),
                    dbc.DropdownMenuItem("About", href='/page-5')
                ],
        )
            ],
            brand="Holiday Challenge",
            color="primary",
            dark=True,
        ),
        html.Div(id="page-content")
    ])
)

@app.callback(Output("page-content", "children"),
              [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/page-1"]:  # if pathname in ["/", "/page-1"]:
        return general.layout
    elif pathname == "/page-2":
        return services.layout
    elif pathname == "/page-3":
        return contract.layout
    elif pathname == "/page-4":
        return predict.layout
    elif pathname == "/page-5":
        return about.layout
if __name__ == '__main__':
    app.run_server(debug=True)



