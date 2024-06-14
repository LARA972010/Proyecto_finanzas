import requests
import pandas as pd

# Tu clave API
api_key = 'tu_clave_api'

# URL para obtener datos diarios
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={api_key}'
# Solicitar los datos
r = requests.get(url)
data = r.json()

# Procesar los datos
# El JSON tiene los datos en 'Time Series (Daily)'
daily_data = data['Time Series (Daily)']

# Convertir a DataFrame
df = pd.DataFrame.from_dict(daily_data, orient='index')

# Renombrar las columnas
df.columns = ['open', 'high', 'low', 'close', 'volume']

# Convertir los datos a tipos apropiados
df = df.astype({
    'open': 'float',
    'high': 'float',
    'low': 'float',
    'close': 'float',
    'volume': 'int'
})

# Convertir el índice a fechas
df.index = pd.to_datetime(df.index)

# Ordenar el DataFrame por la fecha
df = df.sort_index()

# Guardar el DataFrame en un archivo CSV
df.to_csv('IBM_daily_data.csv')

# Mostrar un mensaje de confirmación
print("Datos guardados en 'IBM_daily_data.csv'")
