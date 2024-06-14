import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener la clave API desde las variables de entorno
api_key = os.getenv('ALPHA_VANTAGE_API_KEY')

# Definir los parámetros de la solicitud
keywords = 'tesco'
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
        
        # Mostrar o procesar el DataFrame según necesites
        print(df)
    else:
        print('No se encontraron resultados para la búsqueda.')
else:
    print(f'Error al realizar la solicitud: {r.status_code}')
