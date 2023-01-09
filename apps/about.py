from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            ThemeSwitchAIO(aio_id="theme", themes=[dbc.themes.LUX, dbc.themes.CYBORG])
        ], xs=6, lg=6, md=6, style={'text-align': 'left'}),
    ], className='p-2 align-items-center'),
    dbc.Row([
        dbc.Col([
            html.H1('About', style={'textAlign': 'center'})
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('''This dashboard is about Customer Churn Analysis and it was created with Dash Plotly.
            This dashboard was created for [Holiday Community App-Building Challenge](https://community.plotly.com/t/holiday-community-app-building-challenge/70393) that
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
            dcc.Markdown('''- [Page 1](https://holiday-challenge-plotly.onrender.com/) is about analysis by tenure and charges.'''),
            dcc.Markdown('''- [Page 2](https://holiday-challenge-plotly.onrender.com/page-2) is about analysis by services.'''),
            dcc.Markdown('''- [Page 3](https://holiday-challenge-plotly.onrender.com/page-3) is about analysis by contracts.'''),
            dcc.Markdown('''- [Page 4](https://holiday-challenge-plotly.onrender.com/page-4) helps you to predict churn Yes or No.'''),
            dcc.Markdown('''- [Page 5](https://holiday-challenge-plotly.onrender.com/page-5) is about me''')
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
], fluid=True)