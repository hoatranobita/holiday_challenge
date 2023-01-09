from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from data import df
from dash import dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash import html, callback
import dash_extensions as de
from dash_bootstrap_templates import ThemeSwitchAIO

options = dict(loop=True, autoplay=True)
inputs = df[['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'Contract', 'PaperlessBilling', 'PaymentMethod']]

targets = df['Churn']

le_gender = LabelEncoder()
le_SeniorCitizen = LabelEncoder()
le_Partner = LabelEncoder()
le_Dependents = LabelEncoder()
le_Contract = LabelEncoder()
le_PaperlessBilling = LabelEncoder()
le_PaymentMethod = LabelEncoder()

inputs['gender_n'] = le_gender.fit_transform(inputs['gender'])
inputs['SeniorCitizen_n'] = le_SeniorCitizen.fit_transform(inputs['SeniorCitizen'])
inputs['Partner_n'] = le_Partner.fit_transform(inputs['Partner'])
inputs['Dependents_n'] = le_Dependents.fit_transform(inputs['Dependents'])
inputs['Contract_n'] = le_Contract.fit_transform(inputs['Contract'])
inputs['PaperlessBilling_n'] = le_PaperlessBilling.fit_transform(inputs['PaperlessBilling'])
inputs['PaymentMethod_n'] = le_PaymentMethod.fit_transform(inputs['PaymentMethod'])

inputs_n = inputs.drop(['gender','SeniorCitizen','Partner','Dependents','Contract','PaperlessBilling','PaymentMethod'],axis='columns')

X = inputs_n.values[:, 0:8]
Y = df.values[:,-1]
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.3, random_state = 100)
clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100,max_depth=4, min_samples_leaf=5)
clf_entropy.fit(X_train, y_train)
y_pred_en = clf_entropy.predict(X_train)

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            ThemeSwitchAIO(aio_id="theme", themes=[dbc.themes.LUX, dbc.themes.CYBORG])
        ], xs=6, lg=6, md=6, style={'text-align': 'left'}),
    ], className='p-2 align-items-center'),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('''I decided to use the Decision Tree method to find out the possibility of continuing to use the service or not. 
            Since the amount of data is quite small, I also only used 7 inputs to find it out.'''),
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H6('Gender'),
            dcc.Dropdown(id='dropdown_1',
                         placeholder="Please select gender",
                         options=[{'label': x, 'value': x} for x in df.sort_values('gender')['gender'].unique()],
                         value=[],
                         multi=False,
                         disabled=False,
                         clearable=True,
                         searchable=True)
        ], xs=12, lg=3, md=6, style={'text-align': 'center'}),
        dbc.Col([
            html.H6('SeniorCitizen'),
            dcc.Dropdown(id='dropdown_2',
                         placeholder="SeniorCitizen",
                         options=[{'label': x, 'value': x} for x in
                                  df.sort_values('SeniorCitizen')['SeniorCitizen'].unique()],
                         value=[],
                         multi=False,
                         disabled=False,
                         clearable=True,
                         searchable=True)
        ],xs=12, lg=3, md=6, style={'text-align': 'center'}),
        dbc.Col([
            html.H6('Partner'),
            dcc.Dropdown(id='dropdown_3',
                         placeholder="Partner",
                         options=[{'label': x, 'value': x} for x in df.sort_values('Partner')['Partner'].unique()],
                         value=[],
                         multi=False,
                         disabled=False,
                         clearable=True,
                         searchable=True)
        ],  xs=12, lg=3, md=6, style={'text-align': 'center'}),
        dbc.Col([
            html.H6('Dependents'),
            dcc.Dropdown(id='dropdown_4',
                         placeholder="Dependents",
                         options=[{'label': x, 'value': x} for x in
                                  df.sort_values('Dependents')['Dependents'].unique()],
                         value=[],
                         multi=False,
                         disabled=False,
                         clearable=True,
                         searchable=True)
        ],xs=12, lg=3, md=6, style={'text-align': 'center'}),
    ], className='p-2 align-items-center'),
    dbc.Row([
        dbc.Col([
            html.H6('Contract'),
            dcc.Dropdown(id='dropdown_5',
                         placeholder="Contract",
                         options=[{'label': x, 'value': x} for x in df.sort_values('Contract')['Contract'].unique()],
                         value=[],
                         multi=False,
                         disabled=False,
                         clearable=True,
                         searchable=True)
        ], xs=12, lg=3, md=6, style={'text-align': 'center'}),
        dbc.Col([
            html.H6('PaperlessBilling'),
            dcc.Dropdown(id='dropdown_6',
                         placeholder="PaperlessBilling",
                         options=[{'label': x, 'value': x} for x in
                                  df.sort_values('PaperlessBilling')['PaperlessBilling'].unique()],
                         value=[],
                         multi=False,
                         disabled=False,
                         clearable=True,
                         searchable=True)
        ], xs=12, lg=3, md=6, style={'text-align': 'center'}),
        dbc.Col([
            html.H6('PaymentMethod'),
            dcc.Dropdown(id='dropdown_7',
                         placeholder="PaymentMethod",
                         options=[{'label': x, 'value': x} for x in df.sort_values('PaymentMethod')['PaymentMethod'].unique()],
                         value=[],
                         multi=False,
                         disabled=False,
                         clearable=True,
                         searchable=True)
        ], xs=12, lg=3, md=6, style={'text-align': 'center'}),
    ], className='p-2 align-items-center'),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dbc.Button("Submit", id="btn", color="dark", className="ms-2", size='sm')
        ],xs=12, lg=2, md=6, style={'text-align': 'right'}),
        dbc.Col([html.Span('Churn probability is: '),
                 html.Div(id='result', className="d-inline-flex")
                 ], xs=12, lg=10, md=6, style={'text-align': 'center'})
    ]),
], fluid=True)

@callback(Output('result', 'children'),
              [Input('btn', 'n_clicks')],
              [State('dropdown_1', 'value'),
               State('dropdown_2', 'value'),
               State('dropdown_3', 'value'),
               State('dropdown_4', 'value'),
               State('dropdown_5', 'value'),
               State('dropdown_6', 'value'),
               State('dropdown_7', 'value')])

def update_indicator(n_clicks, dropdown_1, dropdown_2, dropdown_3, dropdown_4, dropdown_5, dropdown_6, dropdown_7):

    if dropdown_1 != [] and dropdown_2 != [] and dropdown_3 != [] and dropdown_4 != [] and dropdown_5 != [] \
            and dropdown_6 != [] and dropdown_7 != []:

        input_z = inputs[(inputs['gender'] == dropdown_1)
                         & (inputs['SeniorCitizen'] == dropdown_2)
                         & (inputs['Partner'] == dropdown_3)
                         & (inputs['Dependents'] == dropdown_4)
                         & (inputs['Contract'] == dropdown_5)
                         & (inputs['PaperlessBilling'] == dropdown_6)
                         & (inputs['PaymentMethod'] == dropdown_7)]

        inputs_zz = input_z.drop(['gender','SeniorCitizen','Partner','Dependents','Contract','PaperlessBilling','PaymentMethod'],axis='columns')
        try:
            theme_1 = inputs_zz['gender_n'].iloc[0]
            theme_2 = inputs_zz['SeniorCitizen_n'].iloc[0]
            theme_3 = inputs_zz['Partner_n'].iloc[0]
            theme_4 = inputs_zz['Dependents_n'].iloc[0]
            theme_5 = inputs_zz['Contract_n'].iloc[0]
            theme_6 = inputs_zz['PaperlessBilling_n'].iloc[0]
            theme_7 = inputs_zz['PaymentMethod_n'].iloc[0]
            X_train = [theme_1, theme_2, theme_3, theme_4, theme_5, theme_6, theme_7]
            z = clf_entropy.predict([X_train])
            if z == 'Yes':
                return html.Div([html.Span(f'👌 Yessssssssss 👌'),de.Lottie(options=options, width="30%", height="30%",
                                      url="https://assets3.lottiefiles.com/packages/lf20_xv1gn5by.json")])
            else:
                return html.Div([html.Span(f' 🥺 Noooooooooooooo 🥺'),de.Lottie(options=options, width="30%", height="30%",
                                      url="https://assets3.lottiefiles.com/packages/lf20_ub6q89nd.json")])
        except IndexError:
            return html.Span('Please choose all inputs to check Churn probability')
    else:
        return html.Span('Please choose all inputs to check Churn probability')