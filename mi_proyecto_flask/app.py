from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__, template_folder='/Users/laragarciacarnes/Documents/Proyecto_Final/Proyecto_finanzas/mi_proyecto_flask/templates', static_folder='mi_proyecto_flask/static')


# Función para cargar los datos desde el CSV correspondiente a la empresa
def cargar_datos_desde_csv(empresa):
    # Ruta al directorio donde se encuentran los datos CSV
    csv_dir = os.path.join(os.getcwd(), 'Proyecto_finanzas', 'datos')
    csv_file = os.path.join(csv_dir, f'{empresa}_monthly_data.csv')
    
    # Leer el CSV con pandas
    try:
        data = pd.read_csv(csv_file)
    except FileNotFoundError:
        return None
    
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar')
def buscar():
    return render_template('buscar.html')

@app.route('/grafico/<empresa>')
def grafico(empresa):
    # Cargar los datos del CSV correspondiente a la empresa
    data = cargar_datos_desde_csv(empresa)
    
    if data is None:
        return f'No se encontraron datos para la empresa {empresa}'
    
    # Convertir los datos a formato JSON para pasarlos a la plantilla
    data_json = data.to_json(orient='records')
    
    # Renderizar la plantilla 'grafico.html' con los datos y el nombre de la empresa
    return render_template('grafico.html', empresa=empresa, data=data_json)

if __name__ == '__main__':
    app.run(debug=True)
