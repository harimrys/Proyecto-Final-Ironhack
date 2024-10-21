import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone

# Cargar el DataFrame
df = pd.read_csv("data/df_images.csv")  # Reemplaza con la ruta a tu archivo CSV

# Inicializa el modelo de embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')  # O el modelo que hayas elegido

# Conecta a Pinecone
pc = Pinecone(api_key="c87f754c-84b9-420e-aa7d-9bc6929fe641")  # Reemplaza con tu clave de API
index = pc.Index('books')

# Función de búsqueda
def search_books(query, search_type):
    if search_type == 'Descripción':
        # Genera un vector para la consulta
        vector = model.encode(query).tolist()
        
        # Realiza la búsqueda en Pinecone usando argumentos nombrados
        results = index.query(vector=vector, top_k=5, include_values=True)

        # Obtiene los IDs y valores de los resultados
        recommended_books = []
        for match in results['matches']:
            book_id = match['id']
            score = match['score']
            # Busca en el DataFrame original para obtener más información sobre el libro
            book_info = df.iloc[int(book_id)]
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
    elif search_type == 'Título':
        return df[df['Book'].str.contains(query, case=False)].to_dict('records')
    elif search_type == 'Autor':
        return df[df['Author'].str.contains(query, case=False)].to_dict('records')


# Función para obtener los 100 peores libros con al menos 20000 valoraciones
def get_bottom_books(n=100, min_ratings=20000):
    filtered_books = df[df['Num_Ratings'] >= min_ratings].drop_duplicates()  # Filtra y elimina duplicados
    bottom_books = filtered_books.nsmallest(n, 'Avg_Rating')  # Obtiene los n libros con peor rating
    return bottom_books.to_dict('records')


# Interfaz de usuario en Streamlit
st.title("📚 Recomendador de Libros")

search_type = st.selectbox("Selecciona el tipo de búsqueda", ["Título", "Autor", "Descripción"])
query = st.text_input("Ingresa tu búsqueda:")

if st.button("Buscar"):
    if query:
        if search_type == 'Descripción':
            results = search_books(query, search_type)
            # Muestra los resultados con imagen al lado
            for book in results:
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.image(book['Image_URL'], width=100)
                with col2:
                    st.write(f"**{book['Title']}**")
                    st.write(f"Autor: {book['Author']}")
                    st.write(f"Rating: {book['Avg_Rating']} ⭐")
                    st.write(f"[Ver más]({book['URL']})")
        else:
            results = search_books(query, search_type)
            # Muestra los resultados con imagen al lado
            for book in results:
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.image(book['Image_URL'], width=100)  # Muestra la imagen del libro
                with col2:
                    st.write(f"**{book['Book']}**")  # Título del libro
                    st.write(f"Autor: {book['Author']}")  # Autor del libro
                    st.write(f"Rating: {book['Avg_Rating']} ⭐")
                    st.write(f"[Ver más]({book['URL']})")  # Enlace al libro
    else:
        st.warning("Por favor ingresa un término de búsqueda.")

# Botones para mostrar peores libros
if st.button("Mostrar 100 Peores Libros"):
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
            st.write(f"Autor: {book['Author']}")
            st.write(f"Rating: {book['Avg_Rating']} ⭐")
            st.write(f"[Ver más]({book['URL']})")
