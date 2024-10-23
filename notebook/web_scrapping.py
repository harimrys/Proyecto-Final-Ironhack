import requests
from bs4 import BeautifulSoup

def get_cover_image_url(book_url):
    try:
        print(f"Procesando URL: {book_url}") 
        response = requests.get(book_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            img_tag = soup.find('img', {'class': 'ResponsiveImage'})  
            if img_tag:
                print(f"Imagen encontrada para: {book_url}")  
                return img_tag['src']
            else:
                print(f"No se encontró la imagen para: {book_url}")  
        else:
            print(f"Código de estado {response.status_code} para: {book_url}")  
    except Exception as e:
        print(f"Error al procesar la URL: {book_url}, Error: {e}") 
    return None