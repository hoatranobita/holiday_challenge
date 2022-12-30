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
            ], style={'height': '22vh', "border": "none"}, className="shadow")
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
            ], style={'height': '22vh', "border": "none"}, className="shadow")
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
            ], style={'height': '22vh', "border": "none"}, className="shadow")
        ], xs=12, lg=4, md=6, style={'text-align': 'center'}),
    ], className='p-2 align-items-center'),

    dbc.Row([
        dbc.Col([
            html.H5('I. Analysis by customer type', style={'text-align': 'left', 'padding-top': 15})
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
            html.H6('3. Tenure', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dcc.Loading(children=[dcc.Graph(figure={}, id='figure_3', style={'height': 280})],
                                color='rgba(50, 171, 96, 0.6)', type='dot')
                ])
            ]),
            html.Div(id='tenure_ratio', style={'text-align': 'left', 'height': 100})
        ], xs=12, lg=3, md=6),
        dbc.Col([
            html.H6('4. Total Charges', style={'text-align': 'left'}),
            dbc.Card([
                dbc.CardBody([
                    dcc.Loading(children=[dcc.Graph(figure={}, id='figure_4', style={'height': 280})],
                                color='rgba(50, 171, 96, 0.6)', type='dot')
                ])
            ]),
            html.Div(id='charge_ratio', style={'text-align': 'left', 'height': 100})
        ], xs=12, lg=3, md=6)
    ], className='p-2 align-items-center'),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Loading(children=[dcc.Graph(figure={}, id='figure_5', style={'height': 350})],
                                color='rgba(50, 171, 96, 0.6)', type='dot')
                ])
            ])
        ], xs=12, lg=3, md=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Loading(children=[dcc.Graph(figure={}, id='figure_6', style={'height': 350})],
                                color='rgba(50, 171, 96, 0.6)', type='dot')
                ])
            ])
        ], xs=12, lg=3, md=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Loading(children=[dcc.Graph(figure={}, id='figure_7', style={'height': 350})],
                                color='rgba(50, 171, 96, 0.6)', type='dot')
                ])
            ])
        ], xs=12, lg=3, md=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Loading(children=[dcc.Graph(figure={}, id='figure_8', style={'height': 350})],
                                color='rgba(50, 171, 96, 0.6)', type='dot')
                ])
            ])
        ], xs=12, lg=3, md=6)

    ], className='p-2 align-items-center'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Loading(children=[dcc.Graph(figure={}, id='figure_9', style={'height': 350})],
                                color='rgba(50, 171, 96, 0.6)', type='dot')
                ])
            ])
        ], xs=12, lg=3, md=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Loading(children=[dcc.Graph(figure={}, id='figure_10', style={'height': 350})],
                                color='rgba(50, 171, 96, 0.6)', type='dot')
                ])
            ])
        ], xs=12, lg=3, md=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Loading(children=[dcc.Graph(figure={}, id='figure_11', style={'height': 350})],
                                color='rgba(50, 171, 96, 0.6)', type='dot')
                ])
            ])
        ], xs=12, lg=3, md=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Loading(children=[dcc.Graph(figure={}, id='figure_12', style={'height': 350})],
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
               Output("figure_12", "figure")],
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
        df5 = pd.pivot_table(df, ('TotalCharges'), index=[radio], aggfunc=np.sum).reset_index()
        # fig_4 = px.bar(df5, x=radio, y='TotalCharges', color=radio, color_discrete_sequence=px.colors.qualitative.Safe,
        # text='TotalCharges')

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
        # fig_4.update_traces(width=0.3, texttemplate='%{text:,.2f}', textposition='inside')

        customer_type_7 = df5[radio].iloc[0]
        customer_type_8 = df5[radio].iloc[1]

        count_7 = df5['TotalCharges'].iloc[0]
        count_8 = df5['TotalCharges'].iloc[1]

        count_7 = f'{count_7:,.0f}'
        count_8 = f'{count_8:,.0f}'

        df6 = df.groupby(['InternetService', radio])[radio].count().reset_index(name='counts')
        fig_5 = px.bar(df6, x=radio, y='counts', color='InternetService',
                       color_discrete_sequence=px.colors.qualitative.Safe, text='counts', barmode='group')
        fig_5.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_5.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_5.update_xaxes(showline=False, showgrid=False, exponentformat="none")
        fig_5.update_traces(width=0.25, texttemplate='%{text:,.0f}', textposition='inside')

        df7 = df.groupby(['MultipleLines', radio])[radio].count().reset_index(name='counts')
        fig_6 = px.bar(df7, x=radio, y='counts', color='MultipleLines',
                       color_discrete_sequence=px.colors.qualitative.Safe, text='counts', barmode='group')
        fig_6.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_6.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_6.update_xaxes(showline=False, showgrid=False, exponentformat="none")
        fig_6.update_traces(width=0.25, texttemplate='%{text:,.0f}', textposition='inside')

        df8 = df.groupby(['OnlineSecurity', radio])[radio].count().reset_index(name='counts')
        fig_7 = px.bar(df8, x=radio, y='counts', color='OnlineSecurity',
                       color_discrete_sequence=px.colors.qualitative.Safe, text='counts', barmode='group')
        fig_7.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_7.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_7.update_xaxes(showline=False, showgrid=False, exponentformat="none")
        fig_7.update_traces(width=0.25, texttemplate='%{text:,.0f}', textposition='inside')

        df9 = df.groupby(['OnlineBackup', radio])[radio].count().reset_index(name='counts')
        fig_8 = px.bar(df9, x=radio, y='counts', color='OnlineBackup',
                       color_discrete_sequence=px.colors.qualitative.Safe, text='counts', barmode='group')
        fig_8.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_8.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_8.update_xaxes(showline=False, showgrid=False, exponentformat="none")
        fig_8.update_traces(width=0.25, texttemplate='%{text:,.0f}', textposition='inside')

        df10 = df.groupby(['PhoneService', radio])[radio].count().reset_index(name='counts')
        fig_9 = px.bar(df10, x=radio, y='counts', color='PhoneService',
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

        df11 = df.groupby(['DeviceProtection', radio])[radio].count().reset_index(name='counts')
        fig_10 = px.bar(df11, x=radio, y='counts', color='DeviceProtection',
                        color_discrete_sequence=px.colors.qualitative.Safe, text='counts', barmode='group')
        fig_10.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_10.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_10.update_xaxes(showline=False, showgrid=False, exponentformat="none")
        fig_10.update_traces(width=0.25, texttemplate='%{text:,.0f}', textposition='inside')

        df12 = df.groupby(['TechSupport', radio])[radio].count().reset_index(name='counts')
        fig_11 = px.bar(df12, x=radio, y='counts', color='TechSupport',
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

        df13 = df.groupby(['StreamingTV', radio])[radio].count().reset_index(name='counts')
        fig_12 = px.bar(df13, x=radio, y='counts', color='StreamingTV',
                        color_discrete_sequence=px.colors.qualitative.Safe, text='counts', barmode='group')
        fig_12.update_layout(template=template, legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        fig_12.update_yaxes(showline=False, showgrid=False, exponentformat="none")
        fig_12.update_xaxes(showline=False, showgrid=False, exponentformat="none")
        fig_12.update_traces(width=0.25, texttemplate='%{text:,.0f}', textposition='inside')

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
               html.Span(f'{radio} {customer_type_1} ratio is: {ratio_1}%, {radio} {customer_type_2} ratio is: {ratio_2}%'), \
               html.Span(f'{radio} {customer_type_3} churn {churn_type_3} ratio is: {ratio_3}%, {radio} {customer_type_4} churn {churn_type_4} ratio is: {ratio_4}%,  {radio} {customer_type_5} churn {churn_type_5} ratio is: {ratio_5}%, {radio} {customer_type_6} churn {churn_type_6} ratio is: {ratio_6}%'), \
               fig, fig_2, fig_3, fig_4, fig_5, fig_6, fig_7, fig_8, fig_9, fig_10, fig_11, fig_12

    else:
        raise PreventUpdate

