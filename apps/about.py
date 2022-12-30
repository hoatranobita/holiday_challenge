from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Row([
        dbc.Col([
            html.H1('About', style={'textAlign': 'center'})
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('''This dashboard is about Iowa Liquor Sales and it was created with Dash Plotly.
            This dashboard was created for [Autumn Community App Challenge](https://community.plotly.com/t/autumn-community-app-challenge/66996) that
            organized by Plotly Community Forum. You can download data to create dashboard [here](https://raw.githubusercontent.com/plotly/datasets/master/liquor_iowa_2021.csv).''')
        ])
    ]),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            html.H1('About Dashboard', style={'textAlign': 'center'})
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('''This dashboard was created with 5 pages.'''),
            dcc.Markdown('''- [Page 1](https://multiple-page-app.herokuapp.com/) is about general information and charts based on wine category.'''),
            dcc.Markdown('''- [Page 2](https://multiple-page-app.herokuapp.com/page-2) is about charts based on wine item.'''),
            dcc.Markdown('''- [Page 3](https://multiple-page-app.herokuapp.com/page-3) is about charts based on store.'''),
            dcc.Markdown('''- [Page 4](https://multiple-page-app.herokuapp.com/page-4) helps you to find store based on latitude and longitude.'''),
            dcc.Markdown('''- [Page 5](https://multiple-page-app.herokuapp.com/page-5) helps you to filter and download data table'''),
            dcc.Markdown('''- [Page 6](https://multiple-page-app.herokuapp.com/page-5) is about us''')
        ])
    ]),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            html.H1('About me', style={'textAlign': 'center'})
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('''Hello, my name is Tran Khanh Hoa, I come from Vietnam. 
            I'm not a professional data analyst but I am interested in it and and I enjoy using Python as well as Plotly 
            to process data and create dashboard.''')
        ])
    ]),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            html.H1('Contact Me', style={'textAlign': 'center'})
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.Div(dbc.NavLink([html.I(className="fab fa-facebook"), " Facebook"],
                                    href="https://www.facebook.com/hoatranobita/",
                                    target="_blank"))
        ], width={"size": 3, 'offset': 2}),
        dbc.Col([
            html.Div(dbc.NavLink([html.I(className="fab fa-linkedin"), " LinkedIn"],
                                 href="https://www.linkedin.com/in/tran-hoa-8047b8111/",
                                 target="_blank"))
        ], width={"size": 3, 'offset': 0}),
        dbc.Col([
            html.Div(dbc.NavLink([html.I(className="fas fa-fire-alt"), " Fiverr"],
                                 href="https://www.fiverr.com/hoatran12c/create-a-interactive-plotly-dashboard-for-you",
                                 target="_blank"))
        ], width={"size": 3, 'offset': 0})
    ], justify="center"),
])