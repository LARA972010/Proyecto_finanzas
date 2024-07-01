from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

# Lista de empresas
empresas = [
    'IBM', 'AAPL', 'MSFT', 'AMZN', 'GOOGL', 
    'TSLA', 'NFLX', 'NVDA', 'FB', 'PYPL'
]

# Función para cargar los datos desde el CSV correspondiente a la empresa
def cargar_datos_desde_csv(empresa):
    csv_file = f'/Users/laragarciacarnes/Documents/Proyecto_Final/Proyecto_finanzas/datos/{empresa}_monthly_data.csv'
    
    try:
        data = pd.read_csv(csv_file)
    except FileNotFoundError:
        return None
    
    return data

# Función para generar un resumen de los datos
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

    return resumen

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

if __name__ == '__main__':
    app.run(debug=True)
