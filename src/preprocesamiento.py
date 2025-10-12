# Importamos las herramientas necesarias de la biblioteca NLTK
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string # Para quitar la puntuación

def preprocess_text(text):
    """
    Función principal que toma un texto y le aplica una serie de pasos de limpieza.
    1. Convierte a minúsculas.
    2. Tokeniza (divide el texto en palabras).
    3. Elimina puntuación y palabras no alfabéticas.
    4. Elimina "stop words" (palabras comunes sin significado).
    """
    
    # Paso 1: Convertir a minúsculas
    text = text.lower()
    
    # Paso 2: Tokenizar el texto
    tokens = word_tokenize(text, language='spanish')
    
    # Paso 3: Eliminar puntuación y palabras no alfabéticas
    # Creamos una lista de tokens limpios
    words = [word for word in tokens if word.isalpha()]
    
    # Paso 4: Eliminar "stop words"
    # Obtenemos la lista de stop words en español de NLTK
    stop_words = set(stopwords.words('spanish'))
    
    # Filtramos la lista de palabras, quitando las stop words
    filtered_words = [word for word in words if not word in stop_words]
    
    # Devolvemos la lista de palabras procesadas
    return filtered_words

# --- Ejemplo de uso (para probar que funciona) ---
if __name__ == '__main__':
    ejemplo = "La UNAM inauguró una magna exposición sobre el muralista Siqueiros en el MUAC."
    print(f"Texto original: '{ejemplo}'")
    
    palabras_procesadas = preprocess_text(ejemplo)
    print(f"Texto procesado (tokens): {palabras_procesadas}")
    # Salida esperada: ['unam', 'inauguró', 'magna', 'exposición', 'muralista', 'siqueiros', 'muac']
