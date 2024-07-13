import pandas as pd
import json
import plotly.graph_objs as go
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

def init_dashboard(server):
    dash_app = Dash(__name__, server=server, url_base_pathname='/dashboard/')

    empresas = ['IBM', 'AAPL', 'MSFT', 'AMZN', 'GOOGL', 'TSLA', 'NFLX', 'NVDA', 'PYPL']
    datos_a_comparar = ['MarketCapitalization', 'PERatio', 'RevenueTTM', 'ProfitMargin']

    # Función para cargar datos desde archivos JSON
    def cargar_datos_empresa(empresa):
        json_file_path = f'/Users/laragarciacarnes/Documents/Proyecto_Final/Proyecto_finanzas/mi_proyecto_flask/dashboard/datos_dashboard/dashboard{empresa}.json'

        try:
            with open(json_file_path, 'r') as f:
                data_dict = json.load(f)
                data = pd.DataFrame([data_dict])
        except FileNotFoundError:
            return None
        except json.JSONDecodeError as e:
            return None
        return data

    def cargar_resultados_empresa(empresa, resultado):
        json_file_path = f'/Users/laragarciacarnes/Documents/Proyecto_Final/Proyecto_finanzas/mi_proyecto_flask/dashboard/datos_dashboard/resultado{empresa}.json'

        try:
            with open(json_file_path, 'r') as f:
                data_dict = json.load(f)
                if resultado in data_dict['annualReports'][0]:  # Verificar si el resultado solicitado existe en el primer reporte
                    data = pd.DataFrame([
                        {'fiscalDateEnding': report['fiscalDateEnding'], resultado: float(report[resultado])}  # Convertir a float
                        for report in data_dict['annualReports']
                    ])
                else:
                    return None
        except FileNotFoundError:
            return None
        except json.JSONDecodeError as e:
            return None
        return data

    dash_app.layout = html.Div([
        html.H1('Dashboard de Empresas', style={'color': '#ffffff', 'text-align': 'center'}),
        html.Div(id='info-container', className='row', children=[
            html.Div(id='info-box', className='four columns'),
            html.Div(className='eight columns', children=[
                dcc.Dropdown(
                    id='empresa-dropdown',
                    options=[{'label': empresa, 'value': empresa} for empresa in empresas],
                    value='AAPL',
                    style={'width': '100%', 'color': '#000000'}  # Color del texto negro
                )
            ])
        ]),
        html.Div(id='graphs-container', className='row', children=[
            html.Div([
                dcc.Dropdown(
                    id='comparacion-dropdown',
                    options=[{'label': empresa, 'value': empresa} for empresa in empresas],
                    multi=True,
                    placeholder='Seleccione empresas para comparar',
                    style={'width': '100%', 'color': '#000000'}  # Color del texto negro
                ),
                dcc.Dropdown(
                    id='dato-dropdown',
                    options=[{'label': dato, 'value': dato} for dato in datos_a_comparar],
                    placeholder='Seleccione un dato para comparar',
                    value='MarketCapitalization',
                    style={'width': '100%', 'color': '#000000'}  # Color del texto negro
                )
            ], className='twelve columns'),
            dcc.Graph(id='comparacion-graph', className='twelve columns'),
            dcc.Graph(id='utilidad-neta-graph', className='six columns'),
            dcc.Graph(id='ebitda-ebit-graph', className='six columns'),
            dcc.Graph(id='margen-utilidad-graph', className='six columns'),
            dcc.Graph(id='ingresos-gastos-graph', className='six columns'),
        ])
    ], style={'background-color': '#121212', 'font-family': 'Arial, sans-serif', 'padding': '20px', 'color': '#ffffff'})

    @dash_app.callback(
        Output('info-box', 'children'),
        [Input('empresa-dropdown', 'value')]
    )
    def update_info_box(selected_empresa):
        data = cargar_datos_empresa(selected_empresa)
        if data is None:
            return []

        info_box = html.Div([
            html.H3(f'Empresa: {selected_empresa}', style={'text-align': 'center', 'color': '#ffffff'}),
            html.Div([
                html.Div([
                    html.H4('Capitalización de Mercado', style={'margin-bottom': '5px', 'color': '#ffffff'}),
                    html.P(f'{data["MarketCapitalization"].values[0]}', style={'font-size': '32px', 'color': '#00bfff', 'text-align': 'center'}),
                ], className='info-card'),
                html.Div([
                    html.H4('P/E Ratio', style={'margin-bottom': '5px', 'color': '#ffffff'}),
                    html.P(f'{data["PERatio"].values[0]}', style={'font-size': '32px', 'color': '#ffcc00', 'text-align': 'center'}),
                ], className='info-card'),
                html.Div([
                    html.H4('Ingresos TTM', style={'margin-bottom': '5px', 'color': '#ffffff'}),
                    html.P(f'{data["RevenueTTM"].values[0]}', style={'font-size': '32px', 'color': '#ff6699', 'text-align': 'center'}),
                ], className='info-card'),
                html.Div([
                    html.H4('Margen de Beneficio', style={'margin-bottom': '5px', 'color': '#ffffff'}),
                    html.P(f'{data["ProfitMargin"].values[0]} %', style={'font-size': '32px', 'color': '#66ff66', 'text-align': 'center'}),
                ], className='info-card'),
            ], style={'display': 'flex', 'justify-content': 'space-around', 'margin-top': '20px'})
        ], style={'border': '1px solid #00bfff', 'padding': '20px', 'border-radius': '10px', 'box-shadow': '0 4px 8px rgba(0, 0, 0, 0.2)'})

        return info_box

    @dash_app.callback(
        Output('utilidad-neta-graph', 'figure'),
        [Input('empresa-dropdown', 'value')]
    )
    def update_utilidad_neta_graph(selected_empresa):
        data = cargar_resultados_empresa(selected_empresa, 'netIncome')
        if data is None:
            return {}

        fig = go.Figure(data=go.Scatter(x=data['fiscalDateEnding'], y=data['netIncome'], mode='lines+markers', name='Net Income'))
        fig.update_layout(
            title='Gráfico de Utilidad Neta',
            xaxis_title='Fecha Fiscal',
            yaxis_title='Utilidad Neta',
            plot_bgcolor='#121212',
            paper_bgcolor='#121212',
            font=dict(color='#ffffff')
        )
        return fig


    @dash_app.callback(
        Output('ebitda-ebit-graph', 'figure'),
        [Input('empresa-dropdown', 'value')]
    )
    def update_ebitda_ebit_graph(selected_empresa):
        ebitda_data = cargar_resultados_empresa(selected_empresa, 'ebitda')
        ebit_data = cargar_resultados_empresa(selected_empresa, 'ebit')

        if ebitda_data is None or ebit_data is None:
            return {}

        fig = go.Figure()
        fig.add_trace(go.Bar(x=ebitda_data['fiscalDateEnding'], y=ebitda_data['ebitda'], name='EBITDA'))
        fig.add_trace(go.Bar(x=ebit_data['fiscalDateEnding'], y=ebit_data['ebit'], name='EBIT'))
        fig.update_layout(
            title='Gráfico de EBITDA y EBIT',
            xaxis_title='Fecha Fiscal',
            yaxis_title='Valor',
            barmode='group',
            plot_bgcolor='#121212',
            paper_bgcolor='#121212',
            font=dict(color='#ffffff')
        )
        return fig

    @dash_app.callback(
        Output('margen-utilidad-graph', 'figure'),
        [Input('empresa-dropdown', 'value')]
    )
    def update_margen_utilidad_graph(selected_empresa):
        data = cargar_resultados_empresa(selected_empresa, 'netIncome')

        if data is None:
            return {}

        total_revenue = cargar_resultados_empresa(selected_empresa, 'totalRevenue')
        if total_revenue is None:
            return {}

        # Calcular el margen de utilidad como un valor decimal antes de convertir a porcentaje
        margen_utilidad = (data['netIncome'] / total_revenue['totalRevenue']) * 100

        fig = go.Figure(data=go.Bar(x=data['fiscalDateEnding'], y=margen_utilidad, name='Margen de Utilidad'))
        fig.update_layout(
            title='Gráfico de Margen de Utilidad',
            xaxis_title='Fecha Fiscal',
            yaxis_title='Margen de Utilidad (%)',
            plot_bgcolor='#121212',
            paper_bgcolor='#121212',
            font=dict(color='#ffffff')
        )
        return fig

    @dash_app.callback(
        Output('ingresos-gastos-graph', 'figure'),
        [Input('empresa-dropdown', 'value')]
    )
    def update_ingresos_gastos_graph(selected_empresa):
        total_revenue = cargar_resultados_empresa(selected_empresa, 'totalRevenue')
        if total_revenue is None:
            return {}

        cost_of_revenue = cargar_resultados_empresa(selected_empresa, 'costOfRevenue')
        operating_expenses = cargar_resultados_empresa(selected_empresa, 'operatingExpenses')

        if cost_of_revenue is None or operating_expenses is None:
            return {}

        gastos = cost_of_revenue['costOfRevenue'] + operating_expenses['operatingExpenses']
        ingresos = total_revenue['totalRevenue']

        fig = go.Figure()
        fig.add_trace(go.Bar(x=total_revenue['fiscalDateEnding'], y=ingresos, name='Ingresos'))
        fig.add_trace(go.Bar(x=total_revenue['fiscalDateEnding'], y=gastos, name='Gastos'))
        fig.update_layout(
            title='Gráfico de Distribución de Ingresos y Gastos',
            xaxis_title='Fecha Fiscal',
            yaxis_title='Valor',
            barmode='group',
            plot_bgcolor='#121212',
            paper_bgcolor='#121212',
            font=dict(color='#ffffff')
        )
        return fig

    @dash_app.callback(
        Output('comparacion-graph', 'figure'),
        [Input('empresa-dropdown', 'value'),
         Input('comparacion-dropdown', 'value'),
         Input('dato-dropdown', 'value')]
    )
    def update_comparacion_graph(selected_empresa, selected_empresas, selected_dato):
        if not selected_empresas or not selected_dato:
            return {}

        colors = ['#00bfff', '#ffcc00', '#ff6699', '#66ff66']  # Colores para cada empresa
        figures = []
        max_value = 0

        # Gráfico de comparación para la empresa seleccionada
        data = cargar_datos_empresa(selected_empresa)
        if data is not None:
            try:
                value = float(data[selected_dato].values[0])
                figures.append(go.Bar(name=selected_empresa, x=[selected_empresa], y=[value], marker=dict(color='#00bfff')))
                if value > max_value:
                    max_value = value
            except ValueError:
                pass  # Si el valor no es numérico, simplemente lo saltamos

        # Iterar sobre las empresas seleccionadas para la comparación
        for index, empresa in enumerate(selected_empresas):
            data = cargar_datos_empresa(empresa)
            if data is not None:
                try:
                    value = float(data[selected_dato].values[0])
                    color_index = (index + 1) % len(colors)  # Utilizar módulo para ciclar los colores
                    figures.append(go.Bar(name=empresa, x=[empresa], y=[value], marker=dict(color=colors[color_index])))
                    if value > max_value:
                        max_value = value
                except ValueError:
                    continue  # Si el valor no es numérico, simplemente lo saltamos

        fig = go.Figure(data=figures)
        fig.update_layout(
            barmode='group',
            title=f'Comparación de {selected_dato} entre Empresas',
            yaxis=dict(range=[0, max_value * 1.1]),  # Ajusta el rango del eje y para que comience en 0
            plot_bgcolor='#121212',  # Color de fondo del gráfico
            paper_bgcolor='#121212',  # Color de fondo del papel (para el área alrededor del gráfico)
            font=dict(color='#ffffff')  # Color del texto
        )
        return fig

    return dash_app
