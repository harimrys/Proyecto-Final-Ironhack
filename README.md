# 📚✨ Bookémon: ¡Atrápalos Todos! 🔍🐉

![Demo Streamlit](gif/Animation.gif)


Este proyecto se ha desarrollado como el proyecto final del bootcamp de **Ironhack Data Analytics**.

He desarrollado una aplicación web construida con Streamlit que permite a los usuarios buscar libros por título, autor o descripción. Utiliza Pinecone para mejorar la búsqueda semántica de libros y ofrecer recomendaciones personalizadas. 

## Características

- **Búsqueda por Título:** Encuentra libros utilizando el título del libro.
- **Búsqueda por Autor:** Busca libros basados en el nombre del autor.
- **Búsqueda por Descripción:** Recomienda libros según una descripción o género literario proporcionado.
- **Imágenes de Libros:** Muestra la portada del libro junto a la información.
- **Interfaz Intuitiva:** Una interfaz de usuario sencilla y fácil de navegar.

## Tecnologías Utilizadas

- [Streamlit](https://streamlit.io/) - Framework para crear aplicaciones web interactivas.
- [Pinecone](https://www.pinecone.io/) - Servicio para implementar búsqueda semántica de alta calidad.
- Python - Lenguaje de programación utilizado para el desarrollo.
- Pandas - Biblioteca para la manipulación de datos.

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

