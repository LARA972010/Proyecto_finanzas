# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=demo'
r = requests.get(url)
data = r.json()

print(data)


"""""

Tendencia de la MONEDA_EXCHANGE_RATE

Esta API devuelve el tipo de cambio en tiempo real para cualquier par de moneda digital (por ejemplo, Bitcoin) o moneda física (por ejemplo, USD).


Parámetros de la API

❚ Requerido:function

La función de tu elección. En este caso,function=CURRENCY_EXCHANGE_RATE

❚ Requerido:from_currency

The currency you would like to get the exchange rate for. It can either be a physical currency or digital/crypto currency. For example: from_currency=USD or from_currency=BTC.

❚ Requerido:to_currency

The destination currency for the exchange rate. It can either be a physical currency or digital/crypto currency. For example: to_currency=USD or to_currency=BTC.

❚ Requerido:apikey

Tu clave de API. Reclama tu clave API gratuita aquí.


Ejemplos (haga clic para ver la salida JSON)

Bitcoin a Euro:
https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=EUR&apikey=demo

Dólar estadounidense a yen japonés:
https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=demo

import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=EUR&apikey=demo'
r = requests.get(url)
data = r.json()

print(data)




DIGITAL_CURRENCY_DAILY

Esta API devuelve la serie temporal histórica diaria de una moneda digital (por ejemplo, BTC) que se negocia en un mercado específico (por ejemplo, EUR/Euro), que se actualiza diariamente a medianoche (UTC). Los precios y los volúmenes se cotizan tanto en la moneda específica del mercado como en el USD.


Parámetros de la API

❚ Requerido:function

La serie temporal de tu elección. En este caso,function=DIGITAL_CURRENCY_DAILY

❚ Requerido:symbol

La moneda digital/criptográfica de su elección. Puede ser cualquiera de las monedas de la lista de monedas digitales. Por ejemplo: symbol=BTC.

❚ Requerido:market

El mercado de cambio de su elección. Puede ser cualquiera de los mercados de la lista de mercado. Por ejemplo: market=EUR.

❚ Requerido:apikey

Tu clave de API. Reclama tu clave API gratuita aquí.


Ejemplos (haga clic para ver la salida JSON)

https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=EUR&apikey=demo

Archivo CSV descargable:
https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=EUR&apikey=demo&datatype=csv


Guías específicas del idioma

Python  NodeJS  PHP  C#/. NET  otros
import requests 

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=EUR&apikey=demo'
r = requests.get(url)
data = r.json()

print(data) """""