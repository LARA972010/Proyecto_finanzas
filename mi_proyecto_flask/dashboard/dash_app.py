import pandas as pd
import json
import plotly.graph_objs as go
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

def init_dashboard(server):
    dash_app = Dash(__name__, server=server, url_base_pathname='/dashboard/')

    empresas = ['IBM', 'AAPL', 'MSFT', 'AMZN', 'GOOGL', 'TSLA', 'NFLX', 'NVDA', 'PYPL']

    # Función para cargar datos desde archivos JSON
    def cargar_datos_empresa(empresa):
        json_file_path = f'/Users/laragarciacarnes/Documents/Proyecto_Final/Proyecto_finanzas/mi_proyecto_flask/dashboard/datos_dashboard/dashboard{empresa}.json'
        
        try:
            with open(json_file_path, 'r') as f:
                data_dict = json.load(f)
                data = pd.DataFrame([data_dict])
                print(f'Datos cargados para {empresa}:', data)  # Debugging
        except FileNotFoundError:
            print(f'Archivo no encontrado para {empresa}')  # Debugging
            return None
        except json.JSONDecodeError as e:
            print(f'Error decoding JSON para {empresa}: {e}')  # Debugging
            return None
        return data

    dash_app.layout = html.Div([
        html.H1('Dashboard de Empresas'),
        html.Div(id='info-container', className='row', children=[
            html.Div(id='info-box', className='four columns'),
            html.Div(className='eight columns', children=[
                dcc.Dropdown(
                    id='empresa-dropdown',
                    options=[{'label': empresa, 'value': empresa} for empresa in empresas],
                    value='AAPL'
                )
            ])
        ]),
        html.Div(className='row', children=[
            html.Div(className='six columns', children=[
                dcc.Graph(id='market-cap-graph'),
            ]),
            html.Div(className='six columns', children=[
                dcc.Graph(id='pe-ratio-graph'),
            ])
        ]),
        html.Div(className='row', children=[
            html.Div(className='six columns', children=[
                dcc.Graph(id='revenue-graph'),
            ]),
            html.Div(className='six columns', children=[
                dcc.Graph(id='profit-margin-graph'),
            ])
        ]),
        dcc.Dropdown(
            id='comparacion-dropdown',
            options=[{'label': empresa, 'value': empresa} for empresa in empresas],
            multi=True,
            placeholder='Seleccione empresas para comparar'
        ),
        dcc.Graph(id='comparacion-graph')
    ])

    @dash_app.callback(
        [Output('market-cap-graph', 'figure'),
         Output('pe-ratio-graph', 'figure'),
         Output('revenue-graph', 'figure'),
         Output('profit-margin-graph', 'figure'),
         Output('info-box', 'children')],
        [Input('empresa-dropdown', 'value')]
    )
    def update_graphs(selected_empresa):
        data = cargar_datos_empresa(selected_empresa)
        if data is None:
            return {}, {}, {}, {}, {}

        print(f'Datos para gráfico: {data}')  # Debugging

        fig1 = go.Figure(data=[
            go.Bar(name='MarketCap', x=[selected_empresa], y=[data['MarketCapitalization'].values[0]])
        ])
        fig1.update_layout(title='Capitalización de Mercado')

        fig2 = go.Figure(data=[
            go.Bar(name='P/E Ratio', x=[selected_empresa], y=[data['PERatio'].values[0]])
        ])
        fig2.update_layout(title='P/E Ratio')

        fig3 = go.Figure(data=[
            go.Bar(name='Revenue', x=[selected_empresa], y=[data['RevenueTTM'].values[0]])
        ])
        fig3.update_layout(title='Ingresos TTM')

        fig4 = go.Figure(data=[
            go.Bar(name='Profit Margin', x=[selected_empresa], y=[data['ProfitMargin'].values[0]])
        ])
        fig4.update_layout(title='Margen de Beneficio')

        info_box = [
            html.H3(f'Empresa: {selected_empresa}'),
            html.P(f'Capitalización de Mercado: {data["MarketCapitalization"].values[0]}'),
            html.P(f'P/E Ratio: {data["PERatio"].values[0]}'),
            html.P(f'Ingresos TTM: {data["RevenueTTM"].values[0]}'),
            html.P(f'Margen de Beneficio: {data["ProfitMargin"].values[0]} %'),
        ]

        return fig1, fig2, fig3, fig4, info_box

    @dash_app.callback(
        Output('comparacion-graph', 'figure'),
        [Input('comparacion-dropdown', 'value')]
    )
    def update_comparacion_graph(selected_empresas):
        if not selected_empresas:
            return {}

        figures = []
        for empresa in selected_empresas:
            data = cargar_datos_empresa(empresa)
            if data is not None:
                figures.append(go.Bar(name='MarketCap', x=[empresa], y=[data['MarketCapitalization'].values[0]]))
                figures.append(go.Bar(name='P/E Ratio', x=[empresa], y=[data['PERatio'].values[0]]))
                figures.append(go.Bar(name='Revenue', x=[empresa], y=[data['RevenueTTM'].values[0]]))
                figures.append(go.Bar(name='Profit Margin', x=[empresa], y=[data['ProfitMargin'].values[0]]))

        fig = go.Figure(data=figures)
        fig.update_layout(barmode='group', title='Comparación entre Empresas')
        return fig

    return dash_app
