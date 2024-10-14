import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Cargar el DataFrame df_merged
df_merged = pd.read_csv('data/df_merged.csv')

# Crear una "descripción" combinando título, autor y etiquetas
df_merged['description'] = df_merged['title'] + ' ' + df_merged['authors'] + ' ' + df_merged['tags'].astype(str)

# Vectorizar la "descripción"
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df_merged['description'])

# Calcular la similitud del coseno
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Función para obtener recomendaciones
def get_recommendations(input_text, cosine_sim=cosine_sim):
    # Vectorizar el texto de entrada
    input_vec = tfidf.transform([input_text])
    sim_scores = cosine_similarity(input_vec, tfidf_matrix).flatten()
    
    # Obtener los índices de los libros recomendados
    indices = pd.Series(df_merged.index, index=df_merged['title']).drop_duplicates()
    
    # Obtener los índices de los libros más similares
    top_indices = sim_scores.argsort()[-6:-1][::-1]  # Top 5 recomendaciones
    recommended_books = df_merged.iloc[top_indices]
    
    return recommended_books

# Interfaz de Streamlit
st.title('Recomendador de Libros')
st.write("Introduce un título o una descripción para recibir recomendaciones.")

# Selección de tipo de entrada
input_type = st.selectbox("¿Qué deseas ingresar?", ("Título", "Descripción"))

# Campo de entrada según la selección
if input_type == "Título":
    user_input = st.text_input("Introduce el título del libro:")
else:
    user_input = st.text_area("Introduce la descripción del libro:")

# Botón para obtener recomendaciones
if st.button("Obtener recomendaciones"):
    if user_input:
        # Llamar a la función de recomendaciones
        recommendations = get_recommendations(user_input)
        
        # Mostrar las recomendaciones
        st.write("**Libros recomendados:**")
        for idx, row in recommendations.iterrows():
            st.write(f"**Título:** {row['title']}, **Autor:** {row['authors']}, **Promedio de Calificación:** {row['average_rating']}")
    else:
        st.write("Por favor, ingresa un título o descripción.")


