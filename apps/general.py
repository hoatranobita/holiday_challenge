import pandas as pd
import numpy as np
import plotly.express as px
from dash import dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
from dash_bootstrap_templates import ThemeSwitchAIO
import dash_extensions as de
from dash import html,callback
import plotly.graph_objects as go
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/telco-customer-churn-by-IBM.csv')

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df['SeniorCitizen'] = df['SeniorCitizen'].astype(str)

template_theme1 = "lux"
template_theme2 = "slate"

options = dict(loop=True, autoplay=True)

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            ThemeSwitchAIO(aio_id="theme", themes=[dbc.themes.LUX, dbc.themes.CYBORG])
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
                    id="radioitems-input",
                    inline=True,
                ),
                ],
                label="Customer Type",
                size="sm"
            )
        ], xs=6, lg=6, md=6, style={'text-align': 'right'})
    ], className='p-2 align-items-center'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.Div(id='card_title_1'), style={'background': '#dbdcf8', 'padding-top': 15}),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            de.Lottie(options=options, width="100%", height="100%",
                                      url="https://assets8.lottiefiles.com/packages/lf20_5wWg42QXf3.json")
                        ], width={'size': 3}, style={'text-align': 'center'}),
                        dbc.Col([
                            html.Div(id='customer_indicator', style={'padding-top': 20}),
                            html.Div(id='customer_indicator2')
                        ], width={'size': 9}, style={'text-align': 'left'})
                    ])
                ])
            ], style={'height': '25vh', "border": "none"}, className="shadow")
        ], xs=12, lg=4, md=6, style={'text-align': 'center'}),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.Div(id='card_title_2'), style={'background': '#f7d7da', 'padding-top': 15}),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            de.Lottie(options=options, width="75%", height="75%",
                                      url="https://assets8.lottiefiles.com/packages/lf20_38Mchs.json")
                        ], width={'size': 3}, style={'text-align': 'center'}),
                        dbc.Col([
                            html.Div(id='churn_indicator'),
                            html.Div(id='churn_indicator2'),
                            html.Div(id='churn_indicator3'),
                            html.Div(id='churn_indicator4')
                        ], width={'size': 9}, style={'text-align': 'left'})
                    ])
                ])
            ], style={'height': '25vh', "border": "none"}, className="shadow")
        ], xs=12, lg=4, md=6, style={'text-align': 'center'}),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.Div(id='card_title_3'), style={'background': '#d7f0dd', 'padding-top': 15}),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            de.Lottie(options=options, width="100%", height="100%",
                                      url="https://assets10.lottiefiles.com/packages/lf20_vvpxhboz.json")
                        ], width={'size': 3}, style={'text-align': 'center'}),
                        dbc.Col([
                            html.Div(id='charge_indicator', style={'padding-top': 20}),
                            html.Div(id='charge_indicator2')
                        ], width={'size': 9}, style={'text-align': 'left'})
                    ])
                ])
            ], style={'height': '25vh', "border": "none"}, className="shadow")
        ], xs=12, lg=4, md=6, style={'text-align': 'center'}),
    ], className='p-2 align-items-center'),

    dbc.Row([
        dbc.Col([
            html.H5('I. Analysis by tenure and charges', style={'text-align': 'left', 'padding-top': 15})
        ])
    ], className='p-2 align-items-center'),

    dbc.Row([
        dbc.Col([
            html.H6('1. Customer Classification', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dcc.Loading(children=[dcc.Graph(figure={}, id='figure_1', style={'height': 280})],
                                color='rgba(50, 171, 96, 0.6)', type='dot')
                ])
            ]),
            html.Div(id='customer_ratio', style={'text-align': 'left', 'height': 100})
        ], xs=12, lg=3, md=6),
        dbc.Col([
            html.H6('2. Churn Ratio', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dcc.Loading(children=[dcc.Graph(figure={}, id='figure_2', style={'height': 280})],
                                color='rgba(50, 171, 96, 0.6)', type='dot')
                ])
            ]),
            html.Div(id='churn_ratio', style={'text-align': 'left', 'height': 100})
        ], xs=12, lg=3, md=6),
        dbc.Col([
            html.H6('3.1 Tenure histogram', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dcc.Loading(children=[dcc.Graph(figure={}, id='figure_3', style={'height': 280})],
                                color='rgba(50, 171, 96, 0.6)', type='dot')
                ])
            ]),
            html.Div(id='tenure_ratio_1', style={'text-align': 'left', 'height': 100})
        ], xs=12, lg=3, md=6),
        dbc.Col([
            html.H6('3.2 Tenure box', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dcc.Loading(children=[dcc.Graph(figure={}, id='figure_4', style={'height': 280})],
                                color='rgba(50, 171, 96, 0.6)', type='dot')
                ])
            ]),
            html.Div(id='tenure_ratio_2', style={'text-align': 'left', 'height': 100})
        ], xs=12, lg=3, md=6)
    ], className='p-2 align-items-center'),
    dbc.Row([
        dbc.Col([
            html.H6('4.1. Monthly Charge', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dcc.Loading(children=[dcc.Graph(figure={}, id='figure_5', style={'height': 280})],
                                color='rgba(50, 171, 96, 0.6)', type='dot')
                ])
            ]),
            html.Div(id='monthly_ratio_1', style={'text-align': 'left', 'height': 100})
        ], xs=12, lg=3, md=6),
        dbc.Col([
            html.H6('4.2. Monthly Charge Box', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dcc.Loading(children=[dcc.Graph(figure={}, id='figure_6', style={'height': 280})],
                                color='rgba(50, 171, 96, 0.6)', type='dot')
                ])
            ]),
            html.Div(id='monthly_ratio_2', style={'text-align': 'left', 'height': 100})
        ], xs=12, lg=3, md=6),
        dbc.Col([
            html.H6('5.1 Total Charges', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dcc.Loading(children=[dcc.Graph(figure={}, id='figure_7', style={'height': 280})],
                                color='rgba(50, 171, 96, 0.6)', type='dot')
                ])
            ]),
            html.Div(id='total_ratio_1', style={'text-align': 'left', 'height': 100})
        ], xs=12, lg=3, md=6),
        dbc.Col([
            html.H6('5.2 Total Charges Box', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dcc.Loading(children=[dcc.Graph(figure={}, id='figure_8', style={'height': 280})],
                                color='rgba(50, 171, 96, 0.6)', type='dot')
                ])
            ]),
            html.Div(id='total_ratio_2', style={'text-align': 'left', 'height': 100})
        ], xs=12, lg=3, md=6)
    ], className='p-2 align-items-center'),
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
                    dcc.Loading(children=[dcc.Graph(figure={}, id='figure_9', style={'height': 350})],
                                color='rgba(50, 171, 96, 0.6)', type='dot')
                ])
            ])
        ], xs=12, lg=3, md=6),
        dbc.Col([
            html.H6('1.2 Churn by Internet Service Type', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dcc.Loading(children=[dcc.Graph(figure={}, id='figure_10', style={'height': 350})],
                                color='rgba(50, 171, 96, 0.6)', type='dot')
                ])
            ])
        ], xs=12, lg=3, md=6),
        dbc.Col([
            html.H6('2.1 Multiple Lines Situation', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dcc.Loading(children=[dcc.Graph(figure={}, id='figure_11', style={'height': 350})],
                                color='rgba(50, 171, 96, 0.6)', type='dot')
                ])
            ])
        ], xs=12, lg=3, md=6),
        dbc.Col([
            html.H6('2.2 Churn by Multiple Lines Type', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dcc.Loading(children=[dcc.Graph(figure={}, id='figure_12', style={'height': 350})],
                                color='rgba(50, 171, 96, 0.6)', type='dot')
                ])
            ])
        ], xs=12, lg=3, md=6)

    ], className='p-2 align-items-center'),
    dbc.Row([
        dbc.Col([
            html.H6('3.1 Phone Service Situation', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dcc.Loading(children=[dcc.Graph(figure={}, id='figure_13', style={'height': 350})],
                                color='rgba(50, 171, 96, 0.6)', type='dot')
                ])
            ])
        ], xs=12, lg=3, md=6),
        dbc.Col([
            html.H6('3.2 Churn by Phone Service', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dcc.Loading(children=[dcc.Graph(figure={}, id='figure_14', style={'height': 350})],
                                color='rgba(50, 171, 96, 0.6)', type='dot')
                ])
            ])
        ], xs=12, lg=3, md=6),
        dbc.Col([
            html.H6('4.1 Online Security Situation', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dcc.Loading(children=[dcc.Graph(figure={}, id='figure_15', style={'height': 350})],
                                color='rgba(50, 171, 96, 0.6)', type='dot')
                ])
            ])
        ], xs=12, lg=3, md=6),
        dbc.Col([
            html.H6('4.2 Churn by Online Security', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dcc.Loading(children=[dcc.Graph(figure={}, id='figure_16', style={'height': 350})],
                                color='rgba(50, 171, 96, 0.6)', type='dot')
                ])
            ])
        ], xs=12, lg=3, md=6)

    ], className='p-2 align-items-center')

], fluid=True)


@callback([Output('card_title_1', 'children'),
               Output('customer_indicator', 'children'),
               Output('customer_indicator2', 'children'),
               Output('card_title_2', 'children'),
               Output('churn_indicator', 'children'),
               Output('churn_indicator2', 'children'),
               Output('churn_indicator3', 'children'),
               Output('churn_indicator4', 'children'),
               Output('card_title_3', 'children'),
               Output('charge_indicator', 'children'),
               Output('charge_indicator2', 'children'),
               Output('customer_ratio', 'children'),
               Output('churn_ratio', 'children'),
           Output('tenure_ratio_1', 'children'),
           Output('tenure_ratio_2', 'children'),
           Output('monthly_ratio_1', 'children'),
           Output('monthly_ratio_2', 'children'),
           Output('total_ratio_1', 'children'),
           Output('total_ratio_2', 'children'),
               Output("figure_1", "figure"),
               Output("figure_2", "figure"),
               Output("figure_3", "figure"),
               Output("figure_4", "figure"),
           Output("figure_5", "figure"),
               Output("figure_6", "figure"),
               Output("figure_7", "figure"),
               Output("figure_8", "figure"),
               Output("figure_9", "figure"),
               Output("figure_10", "figure"),
               Output("figure_11", "figure"),
               Output("figure_12", "figure"),
               Output("figure_13", "figure"),
               Output("figure_14", "figure"),
               Output("figure_15", "figure"),
               Output("figure_16", "figure")],
              [Input("radioitems-input", "value"),
               Input(ThemeSwitchAIO.ids.switch("theme"), "value")])
def update_graph(radio, theme):
    template = template_theme1 if theme else template_theme2
    if radio:
        df2 = df.groupby(radio)[radio].count().reset_index(name='counts')
        df2['Percentage'] = (df2['counts'] / df2['counts'].sum() * 100).round(decimals=2)
        fig = px.pie(values=df2['counts'], names=df2[radio], hole=0.7,
                     color_discrete_sequence=px.colors.qualitative.Safe)
        fig.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig.update_yaxes(showline=True, showgrid=True, exponentformat="none")
        fig.update_xaxes(showline=True, showgrid=True, exponentformat="none")

        customer_type_1 = df2[radio].iloc[0]
        customer_type_2 = df2[radio].iloc[-1]
        count_1 = df2['counts'].iloc[0]
        count_2 = df2['counts'].iloc[-1]
        count_1 = f'{count_1:,.0f}'
        count_2 = f'{count_2:,.0f}'

        ratio_1 = df2['Percentage'].iloc[0]
        ratio_2 = df2['Percentage'].iloc[1]

        df3 = df.groupby(['Churn', radio])[radio].count().reset_index(name='counts')
        df3['Percentage'] = (df3['counts'] / df3['counts'].sum() * 100).round(decimals=2)
        # fig_2 = px.bar(df3, x=radio, y="counts", color="Churn", color_discrete_sequence=px.colors.qualitative.Safe)
        fig_2 = px.sunburst(df3, path=['Churn', radio], values='counts', color='Churn',
                            color_discrete_sequence=px.colors.qualitative.Safe)
        fig_2.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_2.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_2.update_xaxes(showline=False, showgrid=False, exponentformat="none")
        # fig_2.update_traces(width=0.3)

        customer_type_3 = df3[radio].iloc[0]
        customer_type_4 = df3[radio].iloc[1]
        customer_type_5 = df3[radio].iloc[2]
        customer_type_6 = df3[radio].iloc[3]

        churn_type_3 = df3['Churn'].iloc[0]
        churn_type_4 = df3['Churn'].iloc[1]
        churn_type_5 = df3['Churn'].iloc[2]
        churn_type_6 = df3['Churn'].iloc[3]

        count_3 = df3['counts'].iloc[0]
        count_4 = df3['counts'].iloc[1]
        count_5 = df3['counts'].iloc[2]
        count_6 = df3['counts'].iloc[3]

        count_3 = f'{count_3:,.0f}'
        count_4 = f'{count_4:,.0f}'
        count_5 = f'{count_5:,.0f}'
        count_6 = f'{count_6:,.0f}'

        ratio_3 = df3['Percentage'].iloc[0]
        ratio_4 = df3['Percentage'].iloc[1]
        ratio_5 = df3['Percentage'].iloc[2]
        ratio_6 = df3['Percentage'].iloc[3]

        df4 = df.groupby(['tenure', radio])[radio].count().reset_index(name='counts')
        df4.loc[df4['tenure'].between(0, 10), 'tenure_group'] = '0-10'
        df4.loc[df4['tenure'].between(11, 20), 'tenure_group'] = '11-20'
        df4.loc[df4['tenure'].between(21, 30), 'tenure_group'] = '21-30'
        df4.loc[df4['tenure'].between(31, 40), 'tenure_group'] = '31-40'
        df4.loc[df4['tenure'].between(41, 50), 'tenure_group'] = '41-50'
        df4.loc[df4['tenure'].between(51, 60), 'tenure_group'] = '51-60'
        df4.loc[df4['tenure'].between(61, 70), 'tenure_group'] = '61-70'
        df4.loc[df4['tenure'].between(71, 80), 'tenure_group'] = '71-80'
        df4_1 = pd.pivot_table(df4, ('counts'), index=['tenure_group'], aggfunc=np.sum).reset_index()
        df4_1 = df4_1.sort_values(['counts'],ascending=[False])
        tenure_most = df4_1['tenure_group'].iloc[0]

        df4_2 = df.groupby([radio, 'Churn'])['tenure'].agg('median').reset_index()
        customer_type_9 = df4_2[radio].iloc[1]
        customer_type_10 = df4_2[radio].iloc[3]
        median_1 = df4_2['tenure'].iloc[1]
        median_2 = df4_2['tenure'].iloc[3]

        fig_3 = px.histogram(df4, x='tenure', y='counts', color=radio,
                             color_discrete_sequence=px.colors.qualitative.Safe)
        # fig_3 = px.sunburst(df3,path=['Churn',radio],values='counts',color='Churn', color_discrete_sequence=px.colors.qualitative.Safe)
        fig_3.update_layout(template=template, margin=dict(l=20, r=20, t=20, b=20), showlegend=True, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))

        fig_4 = px.box(df, x='Churn', y='tenure', color=radio, color_discrete_sequence=px.colors.qualitative.Safe)

        fig_4.update_layout(template=template, margin=dict(l=20, r=20, t=20, b=20), legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_4.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_4.update_xaxes(showline=False, showgrid=False, exponentformat="none")

        # Monthly Charges Chart
        df5 = pd.pivot_table(df, ('MonthlyCharges'), index=[radio], aggfunc=np.sum).reset_index()
        customer_type_11 = df5[radio].iloc[0]
        customer_type_12 = df5[radio].iloc[1]
        monthly_charge_1 = df5['MonthlyCharges'].iloc[0]
        monthly_charge_2 = df5['MonthlyCharges'].iloc[1]
        monthly_charge_1 = f'{monthly_charge_1:,.2f}'
        monthly_charge_2 = f'{monthly_charge_2:,.2f}'
        df5_2 = df.groupby([radio, 'Churn'])['MonthlyCharges'].agg('median').reset_index()
        customer_type_13 = df5_2[radio].iloc[1]
        customer_type_14 = df5_2[radio].iloc[3]
        median_3 = df5_2['MonthlyCharges'].iloc[1]
        median_4 = df5_2['MonthlyCharges'].iloc[3]
        median_3 = f'{median_3:,.2f}'
        median_4 = f'{median_4:,.2f}'
        fig_5 = px.bar(df5, x=radio, y='MonthlyCharges', color=radio, text='MonthlyCharges',color_discrete_sequence=px.colors.qualitative.Safe)
        fig_5.update_layout(template=template, margin=dict(l=20, r=20, t=20, b=20), legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_5.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_5.update_xaxes(showline=False, showgrid=False, exponentformat="none")
        fig_5.update_traces(width=0.3, texttemplate='%{text:,.2f}', textposition='inside')

        fig_6 = px.box(df, x='Churn', y='MonthlyCharges', color=radio, color_discrete_sequence=px.colors.qualitative.Safe)
        fig_6.update_layout(template=template, margin=dict(l=20, r=20, t=20, b=20), legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_6.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_6.update_xaxes(showline=False, showgrid=False, exponentformat="none")
        # Total Charges Chart
        df6 = pd.pivot_table(df, ('TotalCharges'), index=[radio], aggfunc=np.sum).reset_index()
        customer_type_15 = df6[radio].iloc[0]
        customer_type_16 = df6[radio].iloc[1]
        total_charge_1 = df6['TotalCharges'].iloc[0]
        total_charge_2 = df6['TotalCharges'].iloc[1]
        total_charge_1 = f'{total_charge_1:,.2f}'
        total_charge_2 = f'{total_charge_2:,.2f}'

        df6_2 = df.groupby([radio, 'Churn'])['TotalCharges'].agg('median').reset_index()
        customer_type_17 = df6_2[radio].iloc[1]
        customer_type_18 = df6_2[radio].iloc[3]
        median_5 = df6_2['TotalCharges'].iloc[1]
        median_6 = df6_2['TotalCharges'].iloc[3]
        median_5 = f'{median_5:,.2f}'
        median_6 = f'{median_6:,.2f}'
        fig_7 = px.bar(df6, x=radio, y='TotalCharges', text='TotalCharges',color=radio, color_discrete_sequence=px.colors.qualitative.Safe)
        fig_7.update_layout(template=template, margin=dict(l=20, r=20, t=20, b=20), legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_7.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_7.update_xaxes(showline=False, showgrid=False, exponentformat="none")
        fig_7.update_traces(width=0.3, texttemplate='%{text:,.2f}', textposition='inside')
        fig_8 = px.box(df, x='Churn', y='TotalCharges', color=radio, color_discrete_sequence=px.colors.qualitative.Safe)
        fig_8.update_layout(template=template, margin=dict(l=20, r=20, t=20, b=20), legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_8.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_8.update_xaxes(showline=False, showgrid=False, exponentformat="none")

        customer_type_7 = df6[radio].iloc[0]
        customer_type_8 = df6[radio].iloc[1]

        count_7 = df6['TotalCharges'].iloc[0]
        count_8 = df6['TotalCharges'].iloc[1]

        count_7 = f'{count_7:,.0f}'
        count_8 = f'{count_8:,.0f}'

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

        return html.H6(f'Customer amount by {radio}', style={'color': '#7172ba'}), \
               html.H6(f'{radio} {customer_type_1}: {count_1}'), \
               html.H6(f'{radio} {customer_type_2}: {count_2}'), \
               html.H6(f'Churn Yes/No by {radio}', style={'color': '#b95d61', 'fontWeight': 'bold'}), \
               html.H6(f'{radio} {customer_type_3} churn {churn_type_3}: {count_3}'), \
               html.H6(f'{radio} {customer_type_4} churn {churn_type_4}: {count_4}'), \
               html.H6(f'{radio} {customer_type_5} churn {churn_type_5}: {count_5}'), \
               html.H6(f'{radio} {customer_type_6} churn {churn_type_6}: {count_6}'), \
               html.H6(f'Total Charge Amount by {radio}', style={'color': '#69aa75'}), \
               html.H6(f'{radio} {customer_type_7}: $ {count_7}'), \
               html.H6(f'{radio} {customer_type_8}: $ {count_8}'), \
               html.Div([html.Span(f'{radio} {customer_type_1} ratio is: {ratio_1}%'), \
                         html.Span(f'{radio} {customer_type_2} ratio is: {ratio_2}%')], className="d-grid"), \
               html.Div([html.Span(f'{radio} {customer_type_3} churn {churn_type_3} ratio is: {ratio_3}%'), \
                        html.Span(f'{radio} {customer_type_4} churn {churn_type_4} ratio is: {ratio_4}%'), \
                        html.Span(f'{radio} {customer_type_5} churn {churn_type_5} ratio is: {ratio_5}%'), \
                        html.Span(f'{radio} {customer_type_6} churn {churn_type_6} ratio is: {ratio_6}%')], className="d-grid"), \
               html.Div([html.Span(f'Customers tend to use services with tenure groups from {tenure_most}')],
                        className="d-grid"), \
               html.Div([html.Span(f'{radio} {customer_type_9} churn Yes median tenure is {median_1}'), \
                         html.Span(f'{radio} {customer_type_10} churn Yes median tenure is {median_2}')],
                        className="d-grid"), \
               html.Div([html.Span(f'{radio} {customer_type_11} monthly charge amount is $ {monthly_charge_1}'), \
                         html.Span(f'{radio} {customer_type_12} monthly charge amount is $ {monthly_charge_2}')],
                        className="d-grid"), \
               html.Div([html.Span(f'{radio} {customer_type_13} churn Yes median monthly charge is $ {median_3}'), \
                         html.Span(f'{radio} {customer_type_14} churn Yes median monthly charge is $ {median_4}')],
                        className="d-grid"), \
               html.Div([html.Span(f'{radio} {customer_type_15} total charge amount is $ {total_charge_1}'), \
                         html.Span(f'{radio} {customer_type_16} total charge amount is $ {total_charge_2}')],
                        className="d-grid"), \
               html.Div([html.Span(f'{radio} {customer_type_17} churn Yes median total charge is $ {median_5}'), \
                         html.Span(f'{radio} {customer_type_18} churn Yes median total charge is $ {median_6}')],
                        className="d-grid"),\
               fig, fig_2, fig_3, fig_4, fig_5, fig_6, fig_7, fig_8, fig_9, fig_10, fig_11, fig_12, fig_13, fig_14, fig_15, fig_16

    else:
        raise PreventUpdate

