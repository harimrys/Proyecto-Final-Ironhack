import pandas as pd
import numpy as np
import torch
from transformers import DistilBertTokenizer, DistilBertModel

def numerico(df_books, columns, columns2):
    # Convertir Num_Ratings a numérico eliminando las comas
    df_books[columns] = df_books[columns].str.replace(',', '').astype(int)
    df_books[columns2] = df_books[columns2].fillna('No description available')
