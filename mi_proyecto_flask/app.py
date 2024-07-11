from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go
from dash import Dash
import dash_html_components as html 
import dash_core_components as dcc
from dash.dependencies import Input, Output


app = Flask(__name__, template_folder='templates', static_folder='static')
# confighuracion de dash:
dash_app = Dash(__name__, server=app, url_base_pathname='/dashboard/')


def cargar_datos_empresa(empresa):
    json_file = f'dashboard{empresa}.json'
    try:
        data = pd.read_json(json_file)
    except FileNotFoundError:
        return None
    return data

# Configuración del layout de Dash
dash_app.layout = html.Div([
    html.H1('Dashboard de Empresas'),
    dcc.Dropdown(
        id='empresa-dropdown',
        options=[{'label': empresa, 'value': empresa} for empresa in empresas],
        value='AAPL'
    ),
    dcc.Graph(id='market-cap-graph'),
    dcc.Graph(id='pe-ratio-graph')
])

@dash_app.callback(
    Output('market-cap-graph', 'figure'),
    Output('pe-ratio-graph', 'figure'),
    [Input('empresa-dropdown', 'value')]
)
def update_graphs(selected_empresa):
    data = cargar_datos_empresa(selected_empresa)
    if data is None:
        return {}, {}

    # Gráfico de capitalización de mercado
    fig1 = go.Figure(data=[
        go.Bar(name='MarketCap', x=[selected_empresa], y=[data['MarketCapitalization'].values[0]])
    ])
    fig1.update_layout(title='Capitalización de Mercado')

    # Gráfico de P/E Ratio
    fig2 = go.Figure(data=[
        go.Bar(name='P/E Ratio', x=[selected_empresa], y=[data['PERatio'].values[0]])
    ])
    fig2.update_layout(title='P/E Ratio')

    return fig1, fig2



# -----------------------------------------------------------------------

# Configuración inicial de Matplotlib y Seaborn
def setup():
    import matplotlib
    matplotlib.use('Agg')  # Establece el backend a 'Agg' (renderizado no interactivo)
    import matplotlib.pyplot as plt
    import seaborn as sns

    app = Flask(__name__)

    @app.before_first_request
    def before_first_request():
        setup()

    return app


# Lista de empresas
empresas = [
    'IBM', 'AAPL', 'MSFT', 'AMZN', 'GOOGL', 
    'TSLA', 'NFLX', 'NVDA', 'PYPL'
]

# Función para cargar los datos desde el CSV correspondiente a la empresa
def cargar_datos_desde_csv(empresa):
    csv_file = f'/Users/laragarciacarnes/Documents/Proyecto_Final/Proyecto_finanzas/datos/{empresa}_monthly_data.csv'
    
    try:
        data = pd.read_csv(csv_file)
    except FileNotFoundError:
        return None
    
    return data


def cargar_datos_opciones(empresa):
    csv_file = f'/Users/laragarciacarnes/Documents/Proyecto_Final/Proyecto_finanzas/datos/{empresa}_options_data.csv'
    
    try:
        data = pd.read_csv(csv_file)
    except FileNotFoundError:
        return None
    
    return data


# Función para generar un resumen de los datos e incluir predicciones
def generar_resumen(data):
    resumen = {}

    # Convertir la columna 'fecha' a tipo fecha
    data['fecha'] = pd.to_datetime(data['fecha'])
    
    # Calcular la tendencia general
    resumen['tendencia'] = "ascendente" if data['4. close'].iloc[-1] > data['4. close'].iloc[0] else "descendente"

    # Encontrar los máximos y mínimos
    resumen['max_precio'] = data['4. close'].max()
    resumen['min_precio'] = data['4. close'].min()

    # Calcular la volatilidad (desviación estándar de los precios de cierre)
    resumen['volatilidad'] = data['4. close'].std()

    # Preparar los datos para la predicción (solo usaremos el precio de cierre como feature)
    X = data.index.values.reshape(-1, 1)  # Usaremos los índices de los datos como feature
    y = data['4. close'].values.reshape(-1, 1)

    # Dividir los datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Inicializar y entrenar el modelo de regresión lineal
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Hacer predicciones sobre los datos de prueba
    y_pred = model.predict(X_test)

    # Calcular el error cuadrático medio (MSE)
    mse = mean_squared_error(y_test, y_pred)
    resumen['mse'] = mse

    #  Hacer una predicción para el próximo período (añadir un nuevo punto al final)
    nuevo_indice = np.array([X[-1][0] + 1]).reshape(-1, 1)
    nueva_prediccion = model.predict(nuevo_indice)[0][0]
    resumen['prediccion_proximo'] = nueva_prediccion

    return resumen

def generar_graficos_opciones(data):
    # Análisis de volatilidad implícita vs. precio de ejercicio
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='strike', y='implied_volatility', data=data)
    plt.title('Volatilidad Implícita vs. Precio de Ejercicio')
    plt.xlabel('Precio de Ejercicio')
    plt.ylabel('Volatilidad Implícita')
    plt.grid(True)
    plt.savefig('static/volatilidad_vs_strike.png')
    plt.close()

    # Análisis de las griegas con Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['strike'], y=data['delta'], mode='markers', name='Delta'))
    fig.add_trace(go.Scatter(x=data['strike'], y=data['gamma'], mode='markers', name='Gamma'))
    fig.add_trace(go.Scatter(x=data['strike'], y=data['theta'], mode='markers', name='Theta'))
    fig.add_trace(go.Scatter(x=data['strike'], y=data['vega'], mode='markers', name='Vega'))
    fig.add_trace(go.Scatter(x=data['strike'], y=data['rho'], mode='markers', name='Rho'))

    fig.update_layout(title='Griegas vs. Precio de Ejercicio',
                    xaxis_title='Precio de Ejercicio',
                    yaxis_title='Valor de la Griega',
                    legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01))
    
    # Guardar el gráfico interactivo en un archivo HTML
    fig.write_html('static/griegas_vs_strike_interactivo.html')

    # ** Nuevo código para análisis de Spread Bid-Ask, Volumen y Open Interest **
    
    # Histograma del spread bid-ask
    plt.figure(figsize=(10, 6))
    sns.histplot(data['ask'] - data['bid'], bins=30, kde=True)
    plt.title('Histograma del Spread Bid-Ask')
    plt.xlabel('Spread Bid-Ask')
    plt.ylabel('Frecuencia')
    plt.grid(True)
    plt.savefig('static/spread_bid_ask_histogram.png')
    plt.close()

    # Gráfico de volumen vs. precio de ejercicio
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='strike', y='volume', data=data)
    plt.title('Volumen vs. Precio de Ejercicio')
    plt.xlabel('Precio de Ejercicio')
    plt.ylabel('Volumen')
    plt.grid(True)
    plt.savefig('static/volumen_vs_strike.png')
    plt.close()

    # Gráfico de open interest vs. precio de ejercicio
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='strike', y='open_interest', data=data)
    plt.title('Open Interest vs. Precio de Ejercicio')
    plt.xlabel('Precio de Ejercicio')
    plt.ylabel('Open Interest')
    plt.grid(True)
    plt.savefig('static/open_interest_vs_strike.png')
    plt.close()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    if request.method == 'POST':
        keywords = request.form['keywords']
        return render_template('buscar.html', keywords=keywords)
    return render_template('buscar.html')

@app.route('/grafico', methods=['GET', 'POST'])
def grafico():
    if request.method == 'POST':
        empresa = request.form['empresa']
        return redirect(url_for('mostrar_grafico', empresa=empresa))
    return render_template('grafico.html', empresas=empresas)

@app.route('/grafico/<empresa>')
def mostrar_grafico(empresa):
    data = cargar_datos_desde_csv(empresa)
    if data is None:
        return f'No se encontraron datos para la empresa {empresa}'
    
    data_json = data.to_json(orient='records')
    resumen = generar_resumen(data)

    return render_template('mostrar_grafico.html', empresa=empresa, data=data_json, resumen=resumen)

@app.route('/opciones', methods=['GET', 'POST'])
def opciones():
    if request.method == 'POST':
        empresa = request.form['empresa']
        return redirect(url_for('mostrar_opciones', empresa=empresa))
    return render_template('opciones.html', empresas=empresas)

@app.route('/opciones/<empresa>')
def mostrar_opciones(empresa):
    data = cargar_datos_opciones(empresa)
    if data is None:
        return f'No se encontraron datos de opciones para la empresa {empresa}'
    
    generar_graficos_opciones(data)

    return render_template('mostrar_opciones.html', empresa=empresa)


if __name__ == '__main__':
    app.run(debug=True)
    # hola que tal 
