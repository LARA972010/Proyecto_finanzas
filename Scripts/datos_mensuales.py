import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener la clave API desde las variables de entorno
api_key = os.getenv('ALPHA_VANTAGE_API_KEY')

# URL para obtener los datos mensuales ajustados de IBM
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol=IBM&apikey={api_key}'

# Realizar la solicitud GET
r = requests.get(url)

# Verificar el estado de la solicitud
if r.status_code == 200:
    # Convertir la respuesta JSON a un diccionario
    data = r.json()

    # Verificar si los datos contienen la serie mensual ajustada
    if 'Monthly Adjusted Time Series' in data:
        # Obtener los datos relevantes de la serie mensual ajustada
        monthly_data = data['Monthly Adjusted Time Series']
        
        # Crear una lista de diccionarios para construir el DataFrame
        rows = []
        for date, values in monthly_data.items():
            row = {
                'Date': date,
                'Open': values['1. open'],
                'High': values['2. high'],
                'Low': values['3. low'],
                'Close': values['4. close'],
                'Adjusted Close': values['5. adjusted close'],
                'Volume': values['6. volume'],
                'Dividend Amount': values['7. dividend amount']
            }
            rows.append(row)

        # Crear el DataFrame a partir de la lista de diccionarios
        df = pd.DataFrame(rows)

        # Ordenar el DataFrame por fecha (opcional)
        df['Date'] = pd.to_datetime(df['Date'])
        df.sort_values(by='Date', inplace=True)
        df.reset_index(drop=True, inplace=True)

        # Guardar el DataFrame en un archivo CSV
        df.to_csv('ibm_monthly_adjusted.csv', index=False)

        print(f'Datos guardados correctamente en ibm_monthly_adjusted.csv')
    else:
        print('No se encontraron datos de la serie mensual ajustada en la respuesta JSON.')
else:
    print(f'Error al realizar la solicitud: {r.status_code}')
