import pandas as pd
import numpy as np
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
            ThemeSwitchAIO(aio_id="theme_2", themes=[dbc.themes.LUX, dbc.themes.SLATE])
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
                    id="radioitems-input-2",
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
            html.H5('II. Analysis by services', style={'text-align': 'left', 'padding-top': 15})
        ])
    ], className='p-2 align-items-center'),
    dbc.Row([
        dbc.Col([
            html.H6('1.1 Internet Service Situation', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dbc.Spinner(children=[dcc.Graph(figure={}, id='figure_9', style={'height': 350})],
                                color='dark')
                ])
            ])
        ], xs=12, lg=3, md=6),
        dbc.Col([
            html.H6('1.2 Churn by Internet Service Type', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dbc.Spinner(children=[dcc.Graph(figure={}, id='figure_10', style={'height': 350})],
                                color='dark')
                ])
            ])
        ], xs=12, lg=3, md=6),
        dbc.Col([
            html.H6('2.1 Multiple Lines Situation', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dbc.Spinner(children=[dcc.Graph(figure={}, id='figure_11', style={'height': 350})],
                                color='dark')
                ])
            ])
        ], xs=12, lg=3, md=6),
        dbc.Col([
            html.H6('2.2 Churn by Multiple Lines Type', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dbc.Spinner(children=[dcc.Graph(figure={}, id='figure_12', style={'height': 350})],
                                color='dark')
                ])
            ])
        ], xs=12, lg=3, md=6)

    ], className='p-2 align-items-center'),
    dbc.Row([
        dbc.Col([
            html.H6('3.1 Phone Service Situation', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dbc.Spinner(children=[dcc.Graph(figure={}, id='figure_13', style={'height': 350})],
                                color='dark')
                ])
            ])
        ], xs=12, lg=3, md=6),
        dbc.Col([
            html.H6('3.2 Churn by Phone Service', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dbc.Spinner(children=[dcc.Graph(figure={}, id='figure_14', style={'height': 350})],
                                color='dark')
                ])
            ])
        ], xs=12, lg=3, md=6),
        dbc.Col([
            html.H6('4.1 Online Security Situation', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dbc.Spinner(children=[dcc.Graph(figure={}, id='figure_15', style={'height': 350})],
                                color='dark')
                ])
            ])
        ], xs=12, lg=3, md=6),
        dbc.Col([
            html.H6('4.2 Churn by Online Security', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dbc.Spinner(children=[dcc.Graph(figure={}, id='figure_16', style={'height': 350})],
                                color='dark')
                ])
            ])
        ], xs=12, lg=3, md=6),
    ], className='p-2 align-items-center'),
    dbc.Row([
        dbc.Col([
            html.H6('5.1 OnlineBackup Situation', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dbc.Spinner(children=[dcc.Graph(figure={}, id='figure_17', style={'height': 350})],
                                color='dark')
                ])
            ])
        ], xs=12, lg=3, md=6),
        dbc.Col([
            html.H6('5.2 Churn by OnlineBackup', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dbc.Spinner(children=[dcc.Graph(figure={}, id='figure_18', style={'height': 350})],
                                color='dark')
                ])
            ])
        ], xs=12, lg=3, md=6),
        dbc.Col([
            html.H6('6.1 DeviceProtection Situation', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dbc.Spinner(children=[dcc.Graph(figure={}, id='figure_19', style={'height': 350})],
                                color='dark')
                ])
            ])
        ], xs=12, lg=3, md=6),
        dbc.Col([
            html.H6('6.2 Churn by DeviceProtection', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dbc.Spinner(children=[dcc.Graph(figure={}, id='figure_20', style={'height': 350})],
                                color='dark')
                ])
            ])
        ], xs=12, lg=3, md=6),
    ], className='p-2 align-items-center'),
    dbc.Row([
        dbc.Col([
            html.H6('7.1 TechSupport Situation', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dbc.Spinner(children=[dcc.Graph(figure={}, id='figure_21', style={'height': 350})],
                                color='dark')
                ])
            ])
        ], xs=12, lg=3, md=6),
        dbc.Col([
            html.H6('7.2 Churn by TechSupport', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dbc.Spinner(children=[dcc.Graph(figure={}, id='figure_22', style={'height': 350})],
                                color='dark')
                ])
            ])
        ], xs=12, lg=3, md=6),
        dbc.Col([
            html.H6('8.1 StreamingTV Situation', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dbc.Spinner(children=[dcc.Graph(figure={}, id='figure_23', style={'height': 350})],
                                color='dark')
                ])
            ])
        ], xs=12, lg=3, md=6),
        dbc.Col([
            html.H6('8.2 Churn by StreamingTV', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dbc.Spinner(children=[dcc.Graph(figure={}, id='figure_24', style={'height': 350})],
                                color='dark')
                ])
            ])
        ], xs=12, lg=3, md=6),
    ], className='p-2 align-items-center'),
    dbc.Row([
        dbc.Col([
            html.H6('9.1 StreamingMovies Situation', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dbc.Spinner(children=[dcc.Graph(figure={}, id='figure_25', style={'height': 350})],
                                color='dark')
                ])
            ])
        ], xs=12, lg=3, md=6),
        dbc.Col([
            html.H6('9.2 Churn by StreamingMovies', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dbc.Spinner(children=[dcc.Graph(figure={}, id='figure_26', style={'height': 350})],
                                color='dark')
                ])
            ])
        ], xs=12, lg=3, md=6),
    ], className='p-2 align-items-center')
], fluid=True)

@callback([Output("figure_9", "figure"),
               Output("figure_10", "figure"),
               Output("figure_11", "figure"),
               Output("figure_12", "figure"),
               Output("figure_13", "figure"),
               Output("figure_14", "figure"),
               Output("figure_15", "figure"),
               Output("figure_16", "figure"),
               Output("figure_17", "figure"),
               Output("figure_18", "figure"),
               Output("figure_19", "figure"),
               Output("figure_20", "figure"),
               Output("figure_21", "figure"),
               Output("figure_22", "figure"),
               Output("figure_23", "figure"),
               Output("figure_24", "figure"),
               Output("figure_25", "figure"),
               Output("figure_26", "figure")],
              [Input("radioitems-input-2", "value"),
               Input(ThemeSwitchAIO.ids.switch("theme_2"), "value")])

def update_graph(radio, theme):
    template = template_theme1 if theme else template_theme2
    if radio:
        # Data for fig_9, fig_10
        df7 = df.groupby(['InternetService', radio])[radio].count().reset_index(name='counts')
        fig_9 = px.bar(df7, x=radio, y='counts', color='InternetService',
                       color_discrete_sequence=px.colors.qualitative.Safe, text='counts', barmode='group')
        fig_9.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_9.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_9.update_xaxes(showline=False, showgrid=False, exponentformat="none")
        fig_9.update_traces(width=0.25, texttemplate='%{text:,.0f}', textposition='inside')

        df8 = df.groupby(['InternetService', radio, 'Churn'])[radio].count().reset_index(name='counts')
        z = df8[radio].unique()
        z1 = z[0]
        z2 = z[1]
        df8_1 = df8[df8[radio] == z1]
        df8_2 = df8[df8[radio] == z2]
        z3 = radio + ' ' + z1
        z4 = radio + ' ' + z2
        fig_10 = go.Figure()
        fig_10.add_trace(go.Bar(name=z3, x=[tuple(df8_1['Churn']), tuple(df8_1['InternetService'])],
                               y=list(df8_1['counts'])),
                        )
        fig_10.add_trace(go.Bar(name=z4,x=[tuple(df8_2['Churn']), tuple(df8_2['InternetService'])],
                               y=list(df8_2['counts'])),
                        )
        fig_10.update_layout(barmode='stack')
        fig_10.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_10.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_10.update_xaxes(showline=False, showgrid=False, exponentformat="none")

        # Data for fig_11, fig_12
        df9 = df.groupby(['MultipleLines', radio])[radio].count().reset_index(name='counts')
        fig_11 = px.bar(df9, x=radio, y='counts', color='MultipleLines',
                       color_discrete_sequence=px.colors.qualitative.Safe, text='counts', barmode='group')
        fig_11.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_11.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_11.update_xaxes(showline=False, showgrid=False, exponentformat="none")
        fig_11.update_traces(width=0.25, texttemplate='%{text:,.0f}', textposition='inside')

        df10 = df.groupby(['MultipleLines', radio, 'Churn'])[radio].count().reset_index(name='counts')
        df10_1 = df10[df10[radio] == z1]
        df10_2 = df10[df10[radio] == z2]

        fig_12 = go.Figure()
        fig_12.add_trace(go.Bar(name=z3,x=[tuple(df10_1['Churn']), tuple(df10_1['MultipleLines'])],
                               y=list(df10_1['counts'])),
                        )
        fig_12.add_trace(go.Bar(name=z4,x=[tuple(df10_2['Churn']), tuple(df10_2['MultipleLines'])],
                               y=list(df10_2['counts'])),
                        )
        fig_12.update_layout(barmode='stack')
        fig_12.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_12.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_12.update_xaxes(showline=False, showgrid=False, exponentformat="none")

        # Data for fig_13, fig_14
        df11 = df.groupby(['PhoneService', radio])[radio].count().reset_index(name='counts')
        fig_13 = px.bar(df11, x=radio, y='counts', color='PhoneService',
                       color_discrete_sequence=px.colors.qualitative.Safe, text='counts', barmode='group')
        fig_13.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_13.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_13.update_xaxes(showline=False, showgrid=False, exponentformat="none")
        fig_13.update_traces(width=0.25, texttemplate='%{text:,.0f}', textposition='inside')
        df12 = df.groupby(['PhoneService', radio, 'Churn'])[radio].count().reset_index(name='counts')
        df12_1 = df12[df12[radio] == z1]
        df12_2 = df12[df12[radio] == z2]

        fig_14 = go.Figure()
        fig_14.add_trace(go.Bar(name=z3,x=[tuple(df12_1['Churn']), tuple(df12_1['PhoneService'])],
                               y=list(df12_1['counts'])),
                        )
        fig_14.add_trace(go.Bar(name=z4,x=[tuple(df12_2['Churn']), tuple(df12_2['PhoneService'])],
                               y=list(df12_2['counts'])),
                        )
        fig_14.update_layout(barmode='stack')
        fig_14.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_14.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_14.update_xaxes(showline=False, showgrid=False, exponentformat="none")

        # Data for fig_15, fig_16
        df13 = df.groupby(['OnlineSecurity', radio])[radio].count().reset_index(name='counts')
        fig_15 = px.bar(df13, x=radio, y='counts', color='OnlineSecurity',
                       color_discrete_sequence=px.colors.qualitative.Safe, text='counts', barmode='group')
        fig_15.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_15.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_15.update_xaxes(showline=False, showgrid=False, exponentformat="none")
        fig_15.update_traces(width=0.25, texttemplate='%{text:,.0f}', textposition='inside')
        df14 = df.groupby(['OnlineSecurity', radio, 'Churn'])[radio].count().reset_index(name='counts')
        df14_1 = df14[df14[radio] == z1]
        df14_2 = df14[df14[radio] == z2]

        fig_16 = go.Figure()
        fig_16.add_trace(go.Bar(name=z3,x=[tuple(df14_1['Churn']), tuple(df14_1['OnlineSecurity'])],
                               y=list(df14_1['counts'])),
                        )
        fig_16.add_trace(go.Bar(name=z4,x=[tuple(df14_2['Churn']), tuple(df14_2['OnlineSecurity'])],
                               y=list(df14_2['counts'])),
                        )
        fig_16.update_layout(barmode='stack')
        fig_16.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_16.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_16.update_xaxes(showline=False, showgrid=False, exponentformat="none")

        # Data for fig_17, fig_18
        df15 = df.groupby(['OnlineBackup', radio])[radio].count().reset_index(name='counts')
        fig_17 = px.bar(df15, x=radio, y='counts', color='OnlineBackup',
                       color_discrete_sequence=px.colors.qualitative.Safe, text='counts', barmode='group')
        fig_17.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_17.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_17.update_xaxes(showline=False, showgrid=False, exponentformat="none")
        fig_17.update_traces(width=0.25, texttemplate='%{text:,.0f}', textposition='inside')
        df16 = df.groupby(['OnlineBackup', radio, 'Churn'])[radio].count().reset_index(name='counts')
        df16_1 = df16[df16[radio] == z1]
        df16_2 = df16[df16[radio] == z2]

        fig_18 = go.Figure()
        fig_18.add_trace(go.Bar(name=z3,x=[tuple(df16_1['Churn']), tuple(df16_1['OnlineBackup'])],
                               y=list(df16_1['counts'])),
                        )
        fig_18.add_trace(go.Bar(name=z4,x=[tuple(df16_2['Churn']), tuple(df16_2['OnlineBackup'])],
                               y=list(df16_2['counts'])),
                        )
        fig_18.update_layout(barmode='stack')
        fig_18.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_18.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_18.update_xaxes(showline=False, showgrid=False, exponentformat="none")

        # Data for fig_19, fig_20
        df17 = df.groupby(['DeviceProtection', radio])[radio].count().reset_index(name='counts')
        fig_19 = px.bar(df17, x=radio, y='counts', color='DeviceProtection',
                       color_discrete_sequence=px.colors.qualitative.Safe, text='counts', barmode='group')
        fig_19.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_19.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_19.update_xaxes(showline=False, showgrid=False, exponentformat="none")
        fig_19.update_traces(width=0.25, texttemplate='%{text:,.0f}', textposition='inside')
        df18 = df.groupby(['DeviceProtection', radio, 'Churn'])[radio].count().reset_index(name='counts')
        df18_1 = df18[df18[radio] == z1]
        df18_2 = df18[df18[radio] == z2]

        fig_20 = go.Figure()
        fig_20.add_trace(go.Bar(name=z3,x=[tuple(df18_1['Churn']), tuple(df18_1['DeviceProtection'])],
                               y=list(df18_1['counts'])),
                        )
        fig_20.add_trace(go.Bar(name=z4,x=[tuple(df18_2['Churn']), tuple(df18_2['DeviceProtection'])],
                               y=list(df18_2['counts'])),
                        )
        fig_20.update_layout(barmode='stack')
        fig_20.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_20.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_20.update_xaxes(showline=False, showgrid=False, exponentformat="none")

        # Data for fig_21, fig_22
        df19 = df.groupby(['TechSupport', radio])[radio].count().reset_index(name='counts')
        fig_21 = px.bar(df19, x=radio, y='counts', color='TechSupport',
                       color_discrete_sequence=px.colors.qualitative.Safe, text='counts', barmode='group')
        fig_21.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_21.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_21.update_xaxes(showline=False, showgrid=False, exponentformat="none")
        fig_21.update_traces(width=0.25, texttemplate='%{text:,.0f}', textposition='inside')
        df20 = df.groupby(['TechSupport', radio, 'Churn'])[radio].count().reset_index(name='counts')
        df20_1 = df20[df20[radio] == z1]
        df20_2 = df20[df20[radio] == z2]

        fig_22 = go.Figure()
        fig_22.add_trace(go.Bar(name=z3,x=[tuple(df20_1['Churn']), tuple(df20_1['TechSupport'])],
                               y=list(df20_1['counts'])),
                        )
        fig_22.add_trace(go.Bar(name=z4,x=[tuple(df20_2['Churn']), tuple(df20_2['TechSupport'])],
                               y=list(df20_2['counts'])),
                        )
        fig_22.update_layout(barmode='stack')
        fig_22.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_22.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_22.update_xaxes(showline=False, showgrid=False, exponentformat="none")

        # Data for fig_23, fig_24
        df21 = df.groupby(['StreamingTV', radio])[radio].count().reset_index(name='counts')
        fig_23 = px.bar(df21, x=radio, y='counts', color='StreamingTV',
                       color_discrete_sequence=px.colors.qualitative.Safe, text='counts', barmode='group')
        fig_23.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_23.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_23.update_xaxes(showline=False, showgrid=False, exponentformat="none")
        fig_23.update_traces(width=0.25, texttemplate='%{text:,.0f}', textposition='inside')
        df22 = df.groupby(['StreamingTV', radio, 'Churn'])[radio].count().reset_index(name='counts')
        df22_1 = df22[df22[radio] == z1]
        df22_2 = df22[df22[radio] == z2]

        fig_24 = go.Figure()
        fig_24.add_trace(go.Bar(name=z3,x=[tuple(df22_1['Churn']), tuple(df22_1['StreamingTV'])],
                               y=list(df22_1['counts'])),
                        )
        fig_24.add_trace(go.Bar(name=z4,x=[tuple(df22_2['Churn']), tuple(df22_2['StreamingTV'])],
                               y=list(df22_2['counts'])),
                        )
        fig_24.update_layout(barmode='stack')
        fig_24.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_24.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_24.update_xaxes(showline=False, showgrid=False, exponentformat="none")

        # Data for fig_25, fig_26
        df23 = df.groupby(['StreamingMovies', radio])[radio].count().reset_index(name='counts')
        fig_25 = px.bar(df23, x=radio, y='counts', color='StreamingMovies',
                       color_discrete_sequence=px.colors.qualitative.Safe, text='counts', barmode='group')
        fig_25.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_25.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_25.update_xaxes(showline=False, showgrid=False, exponentformat="none")
        fig_25.update_traces(width=0.25, texttemplate='%{text:,.0f}', textposition='inside')
        df24 = df.groupby(['StreamingMovies', radio, 'Churn'])[radio].count().reset_index(name='counts')
        df24_1 = df24[df24[radio] == z1]
        df24_2 = df24[df24[radio] == z2]

        fig_26 = go.Figure()
        fig_26.add_trace(go.Bar(name=z3,x=[tuple(df24_1['Churn']), tuple(df24_1['StreamingMovies'])],
                               y=list(df24_1['counts'])),
                        )
        fig_26.add_trace(go.Bar(name=z4,x=[tuple(df24_2['Churn']), tuple(df24_2['StreamingMovies'])],
                               y=list(df24_2['counts'])),
                        )
        fig_26.update_layout(barmode='stack')
        fig_26.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_26.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_26.update_xaxes(showline=False, showgrid=False, exponentformat="none")


        return fig_9, fig_10, fig_11, fig_12, fig_13, fig_14, fig_15, fig_16, fig_17, \
               fig_18, fig_19, fig_20, fig_21, fig_22, fig_23, fig_24, fig_25, fig_26

    else:
        raise PreventUpdate