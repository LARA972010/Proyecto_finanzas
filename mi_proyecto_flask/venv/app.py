from flask import Flask, render_template, request
import requests
import pandas as pd

app = Flask(__name__)

# Clave API de Alpha Vantage
api_key = 'tu_api_key'  # Reemplaza 'tu_api_key' con tu propia clave API

@app.route('/', methods=['GET', 'POST'])
def index():
    utilidad_texto = '''
    ¿Busca algunos símbolos o empresas específicas? ¿Está intentando crear un cuadro de búsqueda de autocompletar similar al siguiente?
    La API de búsqueda de símbolos bursátiles impulsa una experiencia de búsqueda de teletipo de autocompletar.
    ¡Te tenemos cubierto! El punto final de búsqueda devuelve los símbolos e información de mercado que mejor coinciden según las palabras clave de su elección. Los resultados de la búsqueda también contienen puntuaciones de coincidencias que le brindan total flexibilidad para desarrollar su propia lógica de búsqueda y filtrado.
    '''
    
    if request.method == 'POST':
        keywords = request.form['keywords']

        # Definir la URL para la solicitud a Alpha Vantage
        url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={keywords}&apikey={api_key}'

        # Realizar la solicitud GET
        r = requests.get(url)

        # Verificar el estado de la solicitud
        if r.status_code == 200:
            # Convertir la respuesta JSON a un diccionario
            data = r.json()

            # Verificar si hay resultados en la respuesta
            if 'bestMatches' in data:
                # Crear un DataFrame de Pandas con los resultados
                df = pd.DataFrame(data['bestMatches'])
                
                # Renderizar el template con los resultados
                return render_template('index.html', df=df, keywords=keywords, utilidad_texto=utilidad_texto)
            else:
                # Si no hay resultados, pasar un DataFrame vacío
                df = pd.DataFrame()  # DataFrame vacío
                error_message = 'No se encontraron resultados para la búsqueda.'
                return render_template('index.html', df=df, error_message=error_message, utilidad_texto=utilidad_texto)
        else:
            error_message = f'Error al realizar la solicitud: {r.status_code}'
            return render_template('index.html', error_message=error_message, utilidad_texto=utilidad_texto)

    # Renderizar el formulario inicial si es un GET request
    # Aquí pasamos un DataFrame vacío también
    df = pd.DataFrame()  # DataFrame vacío
    return render_template('index.html', df=df, utilidad_texto=utilidad_texto)

if __name__ == '__main__':
    app.run(debug=True)
