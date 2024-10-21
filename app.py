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
                'Score': score
            })
        return recommended_books

    # Lógica para buscar por título o autor
    elif search_type == 'Título':
        return df[df['Book'].str.contains(query, case=False)].to_dict('records')
    elif search_type == 'Autor':
        return df[df['Author'].str.contains(query, case=False)].to_dict('records')

# Interfaz de usuario en Streamlit
st.title("📚 Recomendador de Libros")

search_type = st.selectbox("Selecciona el tipo de búsqueda", ["Título", "Autor", "Descripción"])
query = st.text_input("Ingresa tu búsqueda:")

if st.button("Buscar"):
    if query:
        if search_type == 'Descripción':
            results = search_books(query, search_type)
            # Muestra los resultados
            for book in results:
                st.image(book['Image_URL'], width=100)
                st.write(f"**{book['Title']}**")
                st.write(f"Autor: {book['Author']}")
                st.write(f"[Ver más]({book['URL']})")
        else:
            results = search_books(query, search_type)
            for book in results:
                st.image(book['Image_URL'], width=100)  # Muestra la imagen del libro
                st.write(f"**{book['Book']}**")  # Título del libro
                st.write(f"Autor: {book['Author']}")  # Autor del libro
                st.write(f"[Ver más]({book['URL']})")  # Enlace al libro
    else:
        st.warning("Por favor ingresa un término de búsqueda.")
