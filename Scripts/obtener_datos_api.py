import requests

def descargar_datos_csv(url, ruta_guardado):
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(ruta_guardado, 'wb') as f:
            f.write(response.content)
        print(f"Archivo CSV guardado en '{ruta_guardado}'")
    else:
        print(f"Error al descargar el archivo CSV. Código de estado: {response.status_code}")

if __name__ == "__main__":
    url_csv = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo&datatype=csv"
    ruta_destino = "datos_ibm_intradia.csv"
    descargar_datos_csv(url_csv, ruta_destino)
