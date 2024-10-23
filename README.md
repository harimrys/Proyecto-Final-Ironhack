# 📚✨ Bookémon: ¡Atrápalos Todos! 🔍🐉

¡Bienvenido al Recomendador de Libros! Este es mi proyecto final del bootcamp de Ironhack de Data Analytics, donde se ha desarrollado una aplicación de recomendación de libros utilizando tecnologías de análisis de datos y herramientas modernas.


## 🌟 Descripción

La aplicación permite a los usuarios buscar libros por **título**, **autor** o **descripción**. Además, ofrece recomendaciones personalizadas basadas en las descripciones proporcionadas. Los usuarios pueden explorar visualmente los géneros de los libros y descubrir nuevas lecturas a través de una interfaz interactiva.


## 🎥 GIF de Demostración

![Demo Streamlit](gif/Animation.gif)


## 🗂 Estructura del Proyecto

- **📁 .streamlit/**: 
  - `config.toml`: Archivo de configuración específico de Streamlit.
  
- **📁 data/**:
  - `df_books.csv`: Datos de libros.
  - `df_images.csv`: Dataset final con las imagenes de los libros y columnas seleccionadas.
  - `goodreads_data_with_images.csv`: Dataset de libros con imágenes.
  - `goodreads_data.csv`: Dataset principal de libros sin imágenes.

- **🖼 gif**:
  - `Animation.gif`: Demostración de la aplicación en formato GIF.
  - `Designer (10).jpeg`: Imagen de diseño utilizada en el proyecto.
  - `giphy.gif`: GIF de demostración.
 
- **📁 notebook/**:
  - `functions.py`: Funciones auxiliares utilizadas en los notebooks.
  - `generate_vectors.ipynb`: Generación de vectores para búsqueda semántica con Pinecone.
  - `graphics.ipynb`: Análisis y generación de gráficos interactivos.
  - `main.ipynb`: Notebook principal para la limpieza y análisis de los datos.
  - `pinecone_setup.py`: Configuración inicial y carga de vectores en Pinecone.
  - `web_scrapping.ipynb`: Proceso de scraping para obtener información de los libros.
  - `web_scrapping.py`: Script de scraping en Python.

- **📜 Archivos de configuración**:
  - `.gitattributes`: Configuración de atributos de Git.
  - `.gitignore`: Archivos y carpetas que Git debe ignorar.
  - `app.py`: Archivo principal de la aplicación Streamlit.
  - `config.yaml`: Archivo de configuración general del proyecto.
  
- **📄 Otros archivos**:
  - `README.md`: Documentación del proyecto.
  - `requirements.txt`: Lista de dependencias necesarias para ejecutar el proyecto.


## 💻 Tecnologías Utilizadas

- **Python**: Para la lógica del backend y procesamiento de datos.
- **Streamlit**: Para la creación de la interfaz de usuario interactiva.
- **Pandas**: Para la manipulación de datos y análisis.
- **Pinecone**: Para la implementación de búsqueda semántica y almacenamiento de descripciones de libros.
- **BeautifulSoup y Requests**: Para realizar web scraping y obtener imágenes de las portadas de los libros.


## 🌈 Características

- **🔍 Búsqueda por Título, Autor o Descripción**: Encuentra libros específicos rápidamente.
- **🎲 Recomendaciones Aleatorias**: Recibe sugerencias de libros al azar.
- **👎 100 Peores Libros**: Una sección dedicada a los libros menos recomendados, para que sepas cuáles evitar.
- **📈 Gráfico de Libros con Más Valoraciones**: Muestra los libros más valorados por los usuarios.
- **🌌 Visualización de Nubes de Palabras**: Representa palabras clave de los géneros más populares.

## 🚀 Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/nombre_del_repositorio.git
   
2. Navega a la carpeta del proyecto:
   ```bash
   cd nombre_del_repositorio
   
3. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt

## 🏁 Uso

1. Inicia la aplicación:
   ```bash
   streamlit run app.py

## 📉 100 Peores Libros
Hemos recopilado una lista de los 100 peores libros según las valoraciones de los usuarios. Esta sección te ayudará a evitar lecturas decepcionantes y a hacer elecciones más informadas.

## 🤝 Contribuciones
Si deseas contribuir a este proyecto, por favor envía un pull request o abre un issue para discutir posibles mejoras.

