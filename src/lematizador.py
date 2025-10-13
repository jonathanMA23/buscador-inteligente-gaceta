import spacy

# Cargamos el modelo de español de spaCy.
# Lo cargamos una sola vez aquí para que sea eficiente.
nlp = spacy.load('es_core_news_sm')

def lematize_text(text):
    """
    Toma un texto, lo procesa con spaCy y devuelve una lista de lemas.
    """
    # Procesamos el texto con el modelo de spaCy
    doc = nlp(text)
    
    # Extraemos el lema de cada token (palabra)
    lemmas = [token.lemma_ for token in doc]
    
    return lemmas