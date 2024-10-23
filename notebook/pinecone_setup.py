import os
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv, find_dotenv
load_dotenv()


my_key = os.getenv("my_key")

# Crea una instancia de Pinecone
pc = Pinecone(api_key = my_key)

# Se crea un índice llamado 'books'
if 'books' not in pc.list_indexes().names():
    pc.create_index(
        name='books',
        dimension=384,  
        metric='euclidean', 
        spec=ServerlessSpec(
            cloud='aws',  
            region='us-east-1' 
        )
    )

# Conecta con el índice
index = pc.Index('books')
