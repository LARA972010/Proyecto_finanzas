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

## Autores

- **Tu Nombre** - [tu_usuario](https://github.com/tu_usuario)
