# 📚✨ Bookémon: ¡Atrápalos Todos! 🔍🐉

¡Bienvenido al Recomendador de Libros! Este es mi proyecto final del bootcamp de Ironhack de Data Analytics, donde se ha desarrollado una aplicación de recomendación de libros utilizando tecnologías de análisis de datos y herramientas modernas.

## 🌟 Descripción

La aplicación permite a los usuarios buscar libros por **título**, **autor** o **descripción**. Además, ofrece recomendaciones personalizadas basadas en las descripciones proporcionadas. Los usuarios pueden explorar visualmente los géneros de los libros y descubrir nuevas lecturas a través de una interfaz interactiva.

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

## 🎥 GIF de Demostración

Aquí hay una animación que muestra cómo funciona la aplicación:

![Demo Streamlit](gif/Animation.gif)




## 🚀 Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/nombre_del_repositorio.git

## Estructura del Proyecto

/proyecto_final │                                                       
├── .streamlit/                                                                                              
│   └── config.toml                                                                                   
├── data/                                                                                            
│   └── df_books.csv                                                                                                          
│   └── df_images.csv                                                                                           
│   └── goodreads_data_with_images.csv                                                                                       
│   └── goodreads_data.csv                                                   
├── notebook/                                                                                                                            
│   └── functions.py                                                                            
│   └── generate_vectors.ipynb                                                                                                                                               
│   └── main.ipynb                                                                                   
│   └── pinecone_setup.py                                                                                                                               
│   └── web_scrapping.ipynb                                                                                                    
│   └── web_scrapping.py                                                                                                 
├── .gitattributes                                                                                                                                                                      
├── .gitignore                                                                                                                                                                           
├── app.py                                                                                                         
├── requirements.txt                                                                                                      
└── README.md                                                                                            

