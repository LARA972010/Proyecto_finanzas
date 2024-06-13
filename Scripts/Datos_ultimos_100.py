from alpha_vantage.timeseries import TimeSeries
import pandas as pd

# Reemplaza 'YOUR_API_KEY' con tu propia API Key de Alpha Vantage
api_key = 'YOUR_API_KEY'

# Inicializa la instancia de TimeSeries con tu API Key
ts = TimeSeries(key=api_key, output_format='pandas')

# Obtén datos diarios de IBM para los últimos 100 días
data, meta_data = ts.get_daily(symbol='IBM', outputsize='compact')

# Muestra los primeros registros de los datos
print(data.head())
