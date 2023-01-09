import plotly.express as px
from dash import dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from dash_bootstrap_templates import ThemeSwitchAIO
from dash import html,callback
import plotly.graph_objects as go
from data import df

template_theme1 = "lux"
template_theme2 = "slate"

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            ThemeSwitchAIO(aio_id="theme_3", themes=[dbc.themes.LUX, dbc.themes.SLATE])
        ], xs=6, lg=6, md=6, style={'text-align': 'left'}),
        dbc.Col([
            dbc.DropdownMenu(
                [dbc.RadioItems(
                    options=[
                        {"label": "gender", "value": 'gender'},
                        {"label": "SeniorCitizen", "value": "SeniorCitizen"},
                        {"label": 'Partner', "value": 'Partner'},
                        {"label": 'Dependents', "value": 'Dependents'}
                    ],
                    value='gender',
                    id="radioitems-input-3",
                    inline=True,
                ),
                ],
                label="Customer Type",
                size="sm"
            )
        ], xs=6, lg=6, md=6, style={'text-align': 'right'})
    ], className='p-2 align-items-center sticky-top'),
    dbc.Row([
        dbc.Col([
            html.H5('III. Analysis by contracts', style={'text-align': 'left', 'padding-top': 15})
        ])
    ], className='p-2 align-items-center'),
    dbc.Row([
        dbc.Col([
            html.H6('1.1 Contracts Situation', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dbc.Spinner(children=[dcc.Graph(figure={}, id='figure_27', style={'height': 350})],
                                color='dark')
                ])
            ])
        ], xs=12, lg=3, md=6),
        dbc.Col([
            html.H6('1.2 Churn by Contracts Type', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dbc.Spinner(children=[dcc.Graph(figure={}, id='figure_28', style={'height': 350})],
                                color='dark')
                ])
            ])
        ], xs=12, lg=3, md=6),
        dbc.Col([
            html.H6('2.1 PaperlessBilling Situation', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dbc.Spinner(children=[dcc.Graph(figure={}, id='figure_29', style={'height': 350})],
                                color='dark')
                ])
            ])
        ], xs=12, lg=3, md=6),
        dbc.Col([
            html.H6('2.2 Churn by PaperlessBilling Type', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dbc.Spinner(children=[dcc.Graph(figure={}, id='figure_30', style={'height': 350})],
                                color='dark')
                ])
            ])
        ], xs=12, lg=3, md=6)

    ], className='p-2 align-items-center'),
    dbc.Row([
        dbc.Col([
            html.H6('3.1 PaymentMethod Situation', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dbc.Spinner(children=[dcc.Graph(figure={}, id='figure_31', style={'height': 350})],
                                color='dark')
                ])
            ])
        ], xs=12, lg=3, md=6),
        dbc.Col([
            html.H6('3.2 Churn by PaymentMethod', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dbc.Spinner(children=[dcc.Graph(figure={}, id='figure_32', style={'height': 350})],
                                color='dark')
                ])
            ])
        ], xs=12, lg=3, md=6),
    ], className='p-2 align-items-center')
], fluid=True)


@callback([Output("figure_27", "figure"),
               Output("figure_28", "figure"),
               Output("figure_29", "figure"),
               Output("figure_30", "figure"),
               Output("figure_31", "figure"),
               Output("figure_32", "figure")],
              [Input("radioitems-input-3", "value"),
               Input(ThemeSwitchAIO.ids.switch("theme_3"), "value")])

def update_graph(radio, theme):
    template = template_theme1 if theme else template_theme2
    if radio:
        # Data for fig_27, fig_28
        df25 = df.groupby(['Contract', radio])[radio].count().reset_index(name='counts')
        fig_27 = px.bar(df25, x=radio, y='counts', color='Contract',
                       color_discrete_sequence=px.colors.qualitative.Safe, text='counts', barmode='group')
        fig_27.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_27.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_27.update_xaxes(showline=False, showgrid=False, exponentformat="none")
        fig_27.update_traces(width=0.25, texttemplate='%{text:,.0f}', textposition='inside')

        df26 = df.groupby(['Contract', radio, 'Churn'])[radio].count().reset_index(name='counts')
        y = df26[radio].unique()
        y1 = y[0]
        y2 = y[1]
        df26_1 = df26[df26[radio] == y1]
        df26_2 = df26[df26[radio] == y2]
        y3 = radio + ' ' + y1
        y4 = radio + ' ' + y2
        fig_28 = go.Figure()
        fig_28.add_trace(go.Bar(name=y3, x=[tuple(df26_1['Churn']), tuple(df26_1['Contract'])],
                               y=list(df26_1['counts'])),
                        )
        fig_28.add_trace(go.Bar(name=y4,x=[tuple(df26_2['Churn']), tuple(df26_2['Contract'])],
                               y=list(df26_2['counts'])),
                        )
        fig_28.update_layout(barmode='stack')
        fig_28.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_28.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_28.update_xaxes(showline=False, showgrid=False, exponentformat="none")

        # Data for fig_29, fig_30
        df27 = df.groupby(['PaperlessBilling', radio])[radio].count().reset_index(name='counts')
        fig_29 = px.bar(df27, x=radio, y='counts', color='PaperlessBilling',
                       color_discrete_sequence=px.colors.qualitative.Safe, text='counts', barmode='group')
        fig_29.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_29.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_29.update_xaxes(showline=False, showgrid=False, exponentformat="none")
        fig_29.update_traces(width=0.25, texttemplate='%{text:,.0f}', textposition='inside')

        df28 = df.groupby(['PaperlessBilling', radio, 'Churn'])[radio].count().reset_index(name='counts')
        df28_1 = df28[df28[radio] == y1]
        df28_2 = df28[df28[radio] == y2]

        fig_30 = go.Figure()
        fig_30.add_trace(go.Bar(name=y3,x=[tuple(df28_1['Churn']), tuple(df28_1['PaperlessBilling'])],
                               y=list(df28_1['counts'])),
                        )
        fig_30.add_trace(go.Bar(name=y4,x=[tuple(df28_2['Churn']), tuple(df28_2['PaperlessBilling'])],
                               y=list(df28_2['counts'])),
                        )
        fig_30.update_layout(barmode='stack')
        fig_30.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_30.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_30.update_xaxes(showline=False, showgrid=False, exponentformat="none")

        # Data for fig_31, fig_32
        df29 = df.groupby(['PaymentMethod', radio])[radio].count().reset_index(name='counts')
        fig_31 = px.bar(df29, x=radio, y='counts', color='PaymentMethod',
                       color_discrete_sequence=px.colors.qualitative.Safe, text='counts', barmode='group')
        fig_31.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_31.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_31.update_xaxes(showline=False, showgrid=False, exponentformat="none")
        fig_31.update_traces(width=0.25, texttemplate='%{text:,.0f}', textposition='inside')
        df30 = df.groupby(['PaymentMethod', radio, 'Churn'])[radio].count().reset_index(name='counts')
        df30_1 = df30[df30[radio] == y1]
        df30_2 = df30[df30[radio] == y2]

        fig_32 = go.Figure()
        fig_32.add_trace(go.Bar(name=y3,x=[tuple(df30_1['Churn']), tuple(df30_1['PaymentMethod'])],
                               y=list(df30_1['counts'])),
                        )
        fig_32.add_trace(go.Bar(name=y4,x=[tuple(df30_2['Churn']), tuple(df30_2['PaymentMethod'])],
                               y=list(df30_2['counts'])),
                        )
        fig_32.update_layout(barmode='stack')
        fig_32.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_32.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_32.update_xaxes(showline=False, showgrid=False, exponentformat="none")

        return fig_27, fig_28, fig_29, fig_30, fig_31, fig_32

    else:
        raise PreventUpdate