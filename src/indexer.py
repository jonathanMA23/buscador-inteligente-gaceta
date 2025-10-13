# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .preprocesamiento import preprocess_text

# Definimos una función 'dummy' para que TfidfVectorizer no intente
# preprocesar el texto por su cuenta, ya que nosotros ya lo hicimos.
def dummy_fun(doc):
    return doc

def build_index(articles):
    """
    Construye un índice TF-IDF a partir de una lista de artículos.
    Devuelve el vectorizador y la matriz TF-IDF.
    """
    print("Construyendo el índice de relevancia (TF-IDF)...")
    
    # Usamos nuestro preprocesador para convertir cada artículo en una lista de 'stems'
    processed_articles = [" ".join(preprocess_text(article['content'])) for article in articles]
    
    # Creamos el vectorizador TF-IDF
    vectorizer = TfidfVectorizer(
        analyzer='word',
        tokenizer=dummy_fun,
        preprocessor=dummy_fun,
        token_pattern=None
    )
    
    # Ajustamos el modelo y transformamos los datos
    tfidf_matrix = vectorizer.fit_transform(processed_articles)
    
    print("Índice construido exitosamente.")
    return vectorizer, tfidf_matrix

def search_with_ranking(query, vectorizer, tfidf_matrix, articles):
    """
    Realiza una búsqueda y devuelve los resultados ordenados por relevancia.
    """
    # Preprocesamos la consulta del usuario
    processed_query = " ".join(preprocess_text(query))
    
    # Convertimos la consulta a un vector TF-IDF
    query_vector = vectorizer.transform([processed_query])
    
    # Calculamos la similitud del coseno entre la consulta y todos los documentos
    cosine_similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
    
    # Obtenemos los índices de los resultados ordenados por similitud (de mayor a menor)
    related_docs_indices = cosine_similarities.argsort()[::-1]
    
    # Creamos la lista de resultados con su puntaje de relevancia
    results = []
    for i in related_docs_indices:
        # Solo añadimos resultados que tengan una relevancia mayor a 0
        if cosine_similarities[i] > 0:
            results.append({
                "article": articles[i],
                "score": cosine_similarities[i]
            })
            
    return results
