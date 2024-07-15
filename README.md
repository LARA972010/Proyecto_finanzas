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

    
- PYPL (PayPal Holdings, Inc.): 
    Sector: Servicios Financieros.
    Descripción: PayPal es una plataforma de pagos en línea que permite a los usuarios enviar y recibir dinero a través de internet, y es también propietario de Venmo.

Estas empresas representan una amplia gama de sectores y son algunas de las más influyentes en sus respectivos campos.


- ** Lara García Carnés ** - 
