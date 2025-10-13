

# Importamos las herramientas de NLTK
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import string

# Importamos a nuestro especialista en lematización
from .lematizador import lematize_text

def preprocess_text(text):
    """
    Función principal que toma un texto y le aplica una serie de pasos de limpieza.
    1. Convierte a minúsculas.
    2. Lematiza el texto.
    3. Elimina puntuación y palabras no alfabéticas.
    4. Elimina "stop words".
    5. Aplica "stemming" para obtener la raíz de las palabras.
    """
    
    # Paso 1: Convertir a minúsculas
    text = text.lower()
    
    # Paso 2: Lematizar el texto
    lemmas = lematize_text(text)
    
    # Paso 3: Eliminar puntuación y palabras no alfabéticas
    words = [word for word in lemmas if word.isalpha()]
    
    # Paso 4: Eliminar "stop words"
    stop_words = set(stopwords.words('spanish'))
    filtered_words = [word for word in words if word not in stop_words and word != '-PRON-']
    
    # Paso 5: Aplicar Stemming
    # Creamos un stemmer para español
    stemmer = SnowballStemmer('spanish')
    # Aplicamos el stemmer a cada palabra de nuestra lista ya filtrada
    stems = [stemmer.stem(word) for word in filtered_words]
    
    # Devolvemos la lista de raíces de palabras (stems)
    return stems

