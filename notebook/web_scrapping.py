import requests
from bs4 import BeautifulSoup

def get_cover_image_url(book_url):
    try:
        print(f"Procesando URL: {book_url}")  # Mensaje de progreso
        response = requests.get(book_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Encontrar la imagen de portada usando la clase 'ResponsiveImage'
            img_tag = soup.find('img', {'class': 'ResponsiveImage'})  
            if img_tag:
                print(f"Imagen encontrada para: {book_url}")  # Mensaje si se encuentra la imagen
                return img_tag['src']
            else:
                print(f"No se encontró la imagen para: {book_url}")  # Mensaje si no se encuentra la imagen
        else:
            print(f"Código de estado {response.status_code} para: {book_url}")  # Mensaje con el código de estado
    except Exception as e:
        print(f"Error al procesar la URL: {book_url}, Error: {e}")  # Mensaje de error
    return None