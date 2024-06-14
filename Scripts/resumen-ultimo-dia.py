import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener la clave API desde las variables de entorno
api_key = os.getenv('ALPHA_VANTAGE_API_KEY')

# Comprobar si la clave API se ha cargado correctamente
if api_key is None:
    raise ValueError('No se encontró la clave API en el archivo .env. Asegúrate de que ALPHA_VANTAGE_API_KEY esté definida.')

# URL para obtener datos diarios
url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey={api_key}'

# Realizar la solicitud GET
r = requests.get(url)

# Verificar el estado de la solicitud
if r.status_code != 200:
    raise ValueError(f'Error al obtener datos: {r.status_code}')

# Convertir la respuesta a JSON
data = r.json()

# Extraer el precio de cierre y el volumen del DataFrame
symbol = data['Global Quote']['01. symbol']
open_price = float(data['Global Quote']['02. open'])
high_price = float(data['Global Quote']['03. high'])
low_price = float(data['Global Quote']['04. low'])
price = float(data['Global Quote']['05. price'])
volume = int(data['Global Quote']['06. volume'])
latest_trading_day = data['Global Quote']['07. latest trading day']
previous_close = float(data['Global Quote']['08. previous close'])
change = float(data['Global Quote']['09. change'])
change_percent = data['Global Quote']['10. change percent']

# Crear un DataFrame con los datos
df = pd.DataFrame({
    'Symbol': [symbol],
    'Open': [open_price],
    'High': [high_price],
    'Low': [low_price],
    'Price': [price],
    'Volume': [volume],
    'Latest Trading Day': [latest_trading_day],
    'Previous Close': [previous_close],
    'Change': [change],
    'Change Percent': [change_percent]
})

# Imprimir el DataFrame
print(df)

# Guardar el DataFrame en un archivo CSV
df.to_csv('ibm_stock_data.csv', index=False)
print('Datos guardados en ibm_stock_data.csv')
