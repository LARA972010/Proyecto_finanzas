# Proyecto Integrado: Análisis y Visualización de Datos de Finanzas

## Descripción

Este proyecto tiene como objetivo recopilar, analizar y visualizar datos financieros de diversas empresas. Los datos se obtienen utilizando la API de Alpha Vantage y se almacenan en una base de datos PostgreSQL. Los análisis y visualizaciones se realizan en Power BI, y una página web interactiva desarrollada con Flask muestra los resultados y visualizaciones.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Ejecución](#ejecución)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Visualizaciones](#visualizaciones)
- [Extensiones Futuras](#extensiones-futuras)
- [Autores](#autores)

## Tecnologías Utilizadas

- **Python**: Para la recopilación y procesamiento de datos.
- **PostgreSQL**: Base de datos relacional para almacenar los datos financieros.
- **Power BI**: Herramienta de visualización de datos.
- **Flask**: Framework de desarrollo web en Python.
- **Alpha Vantage API**: Fuente de datos financieros.

## Instalación

### Prerrequisitos

- Python 3.7 o superior
- PostgreSQL
- Power BI Desktop
- Una cuenta y clave API de Alpha Vantage

### Clonar el Repositorio

Para empezar, clona el repositorio del proyecto a tu máquina local.

### Instalación de Dependencias

Instala las dependencias del proyecto utilizando el archivo `requirements.txt`.

### Configuración de la Base de Datos

Crea una base de datos en PostgreSQL y ejecuta el script SQL proporcionado para crear las tablas necesarias.

## Configuración

### Configuración de Variables de Entorno

Crea un archivo `.env` en el directorio raíz del proyecto y configura las variables de entorno necesarias, incluyendo la configuración de la base de datos y la clave API de Alpha Vantage.

## Ejecución

### Poblar la Base de Datos

Ejecuta el script para recopilar datos de la API de Alpha Vantage y poblar la base de datos con la información de las acciones de las empresas seleccionadas.

### Iniciar la Aplicación Web

Inicia la aplicación web Flask para visualizar los datos y análisis financieros en tu navegador.

### Análisis y Visualización en Power BI

Abre Power BI Desktop, conéctate a la base de datos PostgreSQL y crea las visualizaciones necesarias utilizando los datos recopilados.

## Estructura del Proyecto

El proyecto está estructurado de la siguiente manera:

- **app.py**: Código principal de la aplicación Flask.
- **data_collector.py**: Script para recopilar datos y poblar la base de datos.
- **schema.sql**: Script SQL para crear las tablas en PostgreSQL.
- **requirements.txt**: Dependencias del proyecto.
- **.env**: Variables de entorno.
- **templates/**: Plantillas HTML para la aplicación Flask.
- **static/**: Archivos estáticos (CSS, JS) para la aplicación Flask.

## Visualizaciones

Las visualizaciones en Power BI incluyen:

- **Gráficos de Líneas**: Muestran los precios históricos de las acciones.
- **Gráficos de Velas**: Detallan las fluctuaciones diarias de precios.
- **Indicadores de Volumen**: Indican el volumen de acciones comercializadas.

Las visualizaciones se integran en la aplicación Flask mediante un iframe que muestra el dashboard de Power BI.

## Extensiones Futuras

1. **Análisis Predictivo**: Implementar modelos de machine learning para predecir el rendimiento futuro de las acciones basado en datos históricos.
2. **Más Fuentes de Datos**: Integrar más fuentes de datos financieros, como noticias de finanzas y análisis de sentimiento en redes sociales.
3. **Interactividad Mejorada**: Utilizar bibliotecas de JavaScript como D3.js o Chart.js para crear gráficos y mapas interactivos.


# Datod de las empresas que voy a incorporar a mi bbdd:
- IBM (International Business Machines Corporation):
    Sector: Tecnología.
    Descripción: IBM es una de las mayores compañías de tecnología del mundo, conocida por sus productos de hardware y software, así como por sus servicios de consultoría y tecnología en la nube.

- AAPL (Apple Inc.):
    Sector: Tecnología.
    Descripción: Apple es famosa por sus productos electrónicos de consumo como el iPhone, iPad, MacBook, y Apple Watch, además de servicios como Apple Music y iCloud.
- MSFT (Microsoft Corporation):
    Sector: Tecnología.
    Descripción: Microsoft es conocido por su software Windows, la suite de productividad Office, y sus servicios de nube Azure. También desarrolla hardware como la Xbox.

- AMZN (Amazon.com, Inc.):
    Sector: Comercio electrónico y tecnología.
    Descripción: Amazon es el gigante del comercio electrónico y ofrece servicios en la nube a través de AWS (Amazon Web Services). También es conocido por su línea de dispositivos electrónicos como Kindle y Echo.

- GOOGL (Alphabet Inc.):
    Sector: Tecnología.
    Descripción: Alphabet es la empresa matriz de Google, conocido por su motor de búsqueda, YouTube, Android, y otros servicios de publicidad y software.

- TSLA (Tesla, Inc.):
    Sector: Automoción y Energía.
    Descripción: Tesla es líder en la fabricación de vehículos eléctricos y soluciones de energía sostenible, como paneles solares y sistemas de almacenamiento de energía.

- NFLX (Netflix, Inc.):
    Sector: Entretenimiento.
    Descripción: Netflix es una plataforma de streaming de vídeo que ofrece una amplia gama de series, películas y documentales, produciendo además contenido original.

- NVDA (NVIDIA Corporation):
    Sector: Tecnología.
    Descripción: NVIDIA es conocida por sus tarjetas gráficas y procesadores de alto rendimiento, utilizados en gaming, IA, y centros de datos.

- FB (Meta Platforms, Inc.) (anteriormente Facebook):
    Sector: Tecnología y Redes Sociales.
    Descripción: Meta Platforms es la empresa matriz de Facebook, Instagram, WhatsApp y Oculus, centrada en redes sociales y realidad virtual.
    
- PYPL (PayPal Holdings, Inc.): 
    Sector: Servicios Financieros.
    Descripción: PayPal es una plataforma de pagos en línea que permite a los usuarios enviar y recibir dinero a través de internet, y es también propietario de Venmo.

Estas empresas representan una amplia gama de sectores y son algunas de las más influyentes en sus respectivos campos.


Gráfico de Volatilidad Implícita vs. Precio de Ejercicio
Este gráfico muestra la relación entre la volatilidad implícita de las opciones y su precio de ejercicio. Aquí está lo que puedes interpretar:

Volatilidad Implícita: Es una medida de la variabilidad esperada del precio de un activo subyacente o índice en el futuro.
Precio de Ejercicio: Es el precio al que el titular de una opción tiene el derecho de comprar o vender el activo subyacente.
Análisis y Utilidad:

Patrón de Volatilidad: Puedes observar cómo varía la volatilidad implícita a medida que cambia el precio de ejercicio. Esto puede revelar patrones o tendencias que los traders pueden usar para determinar estrategias de trading.
Implied Volatility Smile: A veces, este gráfico muestra una sonrisa de volatilidad implícita, donde las opciones fuera del dinero pueden tener volatilidades implícitas más altas que las opciones en el dinero. Esto puede proporcionar insights sobre las expectativas del mercado respecto a la futura volatilidad del precio del activo subyacente.
Gráfico de Griegas vs. Precio de Ejercicio
Las griegas son medidas sensibles al precio, al tiempo y a la volatilidad de las opciones. Este gráfico compara varias griegas (Delta, Gamma, Theta, Vega y Rho) con el precio de ejercicio:

Delta: Muestra la sensibilidad del precio de una opción a cambios en el precio del activo subyacente.
Gamma: Indica la tasa de cambio de Delta respecto al precio del activo subyacente.
Theta: Muestra cómo se espera que el valor de una opción cambie con el paso del tiempo, todo lo demás siendo igual.
Vega: Mide la sensibilidad de una opción al cambio en la volatilidad implícita del activo subyacente.
Rho: Muestra la sensibilidad de una opción al cambio en las tasas de interés.
Análisis y Utilidad:

Sensibilidad a Diferentes Precios de Ejercicio: Puedes observar cómo cada una de las griegas varía con respecto al precio de ejercicio. Esto es crucial para entender cómo se comportará el valor de la opción en función del precio del activo subyacente y otros factores.
Selección de Estrategias: Los traders pueden utilizar esta información para seleccionar estrategias de opciones en función de sus expectativas sobre la dirección del precio del activo subyacente, la volatilidad esperada y el paso del tiempo.
Conclusión:
Ambos gráficos proporcionan información valiosa para los traders y analistas financieros interesados en opciones. Ayudan a visualizar cómo cambian los precios y las expectativas del mercado en relación con diferentes factores clave como la volatilidad y las griegas. Estos gráficos son herramientas poderosas para la toma de decisiones informadas en el mercado de opciones.

- Spread Bid-Ask: Indica la liquidez y los costos de transacción asociados con las opciones. (El spread bid-ask es una medida de la liquidez de las opciones. Un spread más pequeño indica una mayor liquidez, lo que generalmente significa que hay menos costos asociados con la compra y venta de la opción.)

- Volumen y Open Interest: Indican la actividad y el interés en diferentes precios de ejercicio y fechas de vencimiento. (El volumen y el open interest son indicadores importantes de la actividad y el interés en las opciones en diferentes strikes y fechas de vencimiento.
Gráfico de Volumen vs. Precio de Ejercicio:
Este gráfico muestra qué strikes están viendo más actividad en términos de volumen negociado.)

- Predicción de Precios de Opciones: Utiliza machine learning para hacer predicciones sobre los precios futuros de las opciones. (Este gráfico muestra dónde se encuentran las mayores posiciones abiertas (open interest).)

## Autores

- ** Lara García ** - 
