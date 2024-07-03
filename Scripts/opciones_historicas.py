import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener la clave API desde las variables de entorno
api_key = os.getenv('ALPHA_VANTAGE_API_KEY')

# Función para obtener datos mensuales de una empresa
def obtener_datos_mensuales(symbol):
    url = f'https://www.alphavantage.co/query?function=HISTORICAL_OPTIONS&symbol={symbol}&apikey={api_key}'
    r = requests.get(url)
    data = r.json()
    
    # Comprobar si la respuesta contiene datos válidos
    if 'Monthly Time Series' not in data:
        print(f"No se encontraron datos mensuales para {symbol}")
        return None
    
    # Extraer datos de la sección Monthly Time Series
    monthly_data = data['Monthly Time Series']
    
    # Convertir el diccionario a DataFrame de Pandas
    df = pd.DataFrame(monthly_data).T  # .T para transponer los datos
    
    # Resetear el índice para que las fechas sean una columna
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'fecha'}, inplace=True)
    
    return df

# Lista de símbolos de empresas de interés
empresas = ['IBM', 'AAPL', 'MSFT', 'AMZN', 'GOOGL', 'TSLA', 'NFLX', 'NVDA', 'PYPL']

# Bucle para obtener datos y guardar en archivos CSV
for empresa in empresas:
    df_empresa = obtener_datos_mensuales(empresa)
    
    if df_empresa is not None:
        # Guardar el DataFrame como CSV
        filename = f'{empresa}_monthly_data.csv'
        df_empresa.to_csv(filename, index=False)
        print(f'Datos de {empresa} guardados en {filename}')
