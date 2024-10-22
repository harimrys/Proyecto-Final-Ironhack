import os
from pinecone import Pinecone, ServerlessSpec

# Crea una instancia de Pinecone
pc = Pinecone(api_key = "c87f754c-84b9-420e-aa7d-9bc6929fe641")

# Crear un índice llamado 'books'
if 'books' not in pc.list_indexes().names():
    pc.create_index(
        name='books',
        dimension=384,  # Usar 768 como dimensión de ejemplo para embeddings
        metric='euclidean',  # Puedes cambiar esto si lo necesitas
        spec=ServerlessSpec(
            cloud='aws',  # Cambia según tus necesidades
            region='us-east-1'  # Cambia según tus necesidades
        )
    )

# Conectar al índice
index = pc.Index('books')
