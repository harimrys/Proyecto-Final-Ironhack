import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
import time

# Cargar el DataFrame
df = pd.read_csv("data/df_images.csv")  # Reemplaza con la ruta a tu archivo CSV

# Inicializa el modelo de embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')  # O el modelo que hayas elegido

# Conecta a Pinecone
pc = Pinecone(api_key="c87f754c-84b9-420e-aa7d-9bc6929fe641")  # Reemplaza con tu clave de API
index = pc.Index('books')

# Función de búsqueda
def search_books(query, search_type):
    if search_type == 'Description':
        # Genera un vector para la consulta
        vector = model.encode(query).tolist()
        
        # Realiza la búsqueda en Pinecone usando argumentos nombrados
        results = index.query(vector=vector, top_k=10, include_values=True)

        # Obtiene los IDs y valores de los resultados
        recommended_books = []
        for match in results['matches']:
            book_id = match['id']
            score = match['score']
            # Busca en el DataFrame original para obtener más información sobre el libro
            book_info = df.iloc[int(book_id)]
            
            # Filtrar libros con al menos 20000 valoraciones
            if book_info['Num_Ratings'] >= 20000:
                recommended_books.append({
                    'Title': book_info['Book'],
                    'Author': book_info['Author'],
                    'Description': book_info['Description'],
                    'Image_URL': book_info['Image_URL'],
                    'URL': book_info['URL'],
                    'Avg_Rating': book_info['Avg_Rating'],
                    'Score': score
                })
        return recommended_books


    # Lógica para buscar por título o autor
    elif search_type == 'Title':
        return df[df['Book'].str.contains(query, case=False)].to_dict('records')
    elif search_type == 'Author':
        return df[df['Author'].str.contains(query, case=False)].to_dict('records')


# Función para obtener los 100 peores libros con al menos 20000 valoraciones
def get_bottom_books(n=100, min_ratings=20000):
    filtered_books = df[df['Num_Ratings'] >= min_ratings].drop_duplicates()  # Filtra y elimina duplicados
    bottom_books = filtered_books.nsmallest(n, 'Avg_Rating')  # Obtiene los n libros con peor rating
    return bottom_books.to_dict('records')


# Interfaz de usuario en Streamlit

# Configurar la página
st.set_page_config(
    page_title = "Bookémon",  # Cambia esto por el título deseado
    page_icon = "📚",  # Puedes añadir un icono si lo deseas
)

st.title("📚✨ Bookémon: Catch them all! 🔍🐉")

# Espacio entre el título y el contenido
st.markdown("<br><br>", unsafe_allow_html=True)  # Añadir 2 líneas de espacio

# Agregar una imagen en la barra lateral
st.sidebar.image("Designer (10).jpeg", caption="Catch them all!!🔍🐉", use_column_width=True) 

page = st.sidebar.selectbox("Try your luck", ["Book recommender", "100 Worst books", "Surprise me!"])

if page == "Book recommender":
    search_type = st.selectbox("Select search type", ["Title", "Author", "Description"])
    query = st.text_input("Please enter your search:")
    
    if st.button("Search"):
        if query:
            if search_type == "Description":
                results = search_books(query, search_type)
                # Muestra los resultados con imagen al lado
                for book in results:
                    col1, col2 = st.columns([1, 3])
                    with col1:
                        st.image(book['Image_URL'], width=100)
                    with col2:
                        st.write(f"**{book['Title']}**")
                        st.write(f"Author: {book['Author']}")
                        st.write(f"Rating: {book['Avg_Rating']}⭐")
                        st.write(f"[More information]({book['URL']})")
            else:
                results = search_books(query, search_type)
                # Muestra los resultados con imagen al lado
                for book in results:
                    col1, col2 = st.columns([1, 3])
                    with col1:
                        st.image(book['Image_URL'], width=100)  # Muestra la imagen del libro
                    with col2:
                        st.write(f"**{book['Book']}**")  # Título del libro
                        st.write(f"Author: {book['Author']}")  # Autor del libro
                        st.write(f"Rating: {book['Avg_Rating']}⭐")
                        st.write(f"[More information]({book['URL']})")  # Enlace al libro
        else:
            st.warning("Please enter a search term.")

elif page == "100 Worst books":
    # Mostrar los 100 peores libros
    bottom_books = get_bottom_books()
    for book in bottom_books:
        col1, col2 = st.columns([1, 3])
        with col1:
            if isinstance(book['Image_URL'], str) and book['Image_URL']:
                st.image(book['Image_URL'], width=100)
            else:
                st.write("**Image Not Available**")  # Mensaje cuando no hay imagen
        with col2:
            st.write(f"**{book['Book']}**")
            st.write(f"Author: {book['Author']}")
            st.write(f"Rating: {book['Avg_Rating']}⭐")
            st.write(f"[More information]({book['URL']})")

elif page == "Surprise me!":
        # Espacio para la animación
        placeholder = st.empty()
            
        # Mostrar la animación de sombrero mágico
        placeholder.image("giphy.gif")  # Reemplaza con la ruta de tu animación
        time.sleep(3)  # Espera unos segundos para mostrar el GIF
            
        # Elegir un libro al azar
        libro_aleatorio = df.sample()
            
        # Limpiar el espacio y mostrar el libro
        placeholder.empty()  # Limpia la animación
        st.markdown(f"### We recommend: **{libro_aleatorio['Book'].values[0]}**")
        st.markdown(f"**Author:** {libro_aleatorio['Author'].values[0]}")
        st.markdown(f"**Description:** {libro_aleatorio['Description'].values[0]}")
        st.image(libro_aleatorio['Image_URL'].values[0], width=200)