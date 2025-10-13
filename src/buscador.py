# Importamos la función de preprocesamiento que acabamos de crear
from .preprocesamiento import preprocess_text

# --- Mock Data ---
# La misma base de datos de antes.
mock_articles = [
    { 
        "title": 'La UNAM en el ranking de las mejores universidades del mundo', 
        "url": 'https://www.gaceta.unam.mx/unam-ranking-mundial-2025/', 
        "snippet": 'La Universidad Nacional Autónoma de México se posiciona nuevamente entre las 100 mejores universidades a nivel global, destacando en áreas como artes y humanidades.' 
    },
    { 
        "title": 'Descubren nueva especie de orquídea en la Reserva del Pedregal', 
        "url": 'https://www.gaceta.unam.mx/descubren-orquidea-pedregal/', 
        "snippet": 'Científicos del Instituto de Biología anuncian el hallazgo de una nueva especie de orquídea endémica de la Reserva Ecológica del Pedregal de San Ángel.' 
    },
    { 
        "title": 'Convocatoria para becas de movilidad estudiantil 2025-2', 
        "url": 'https://www.gaceta.unam.mx/convocatoria-becas-movilidad-2025/', 
        "snippet": 'Se abre la convocatoria para que estudiantes de licenciatura puedan realizar una estancia académica en universidades extranjeras durante el segundo semestre de 2025.' 
    },
    { 
        "title": 'El muralismo de Siqueiros: una visión revolucionaria en el MUAC', 
        "url": 'https://www.gaceta.unam.mx/exposicion-siqueiros-muac/', 
        "snippet": 'El Museo Universitario Arte Contemporáneo (MUAC) inaugura una magna exposición que recorre la trayectoria y el impacto del muralista David Alfaro Siqueiros.' 
    },
    { 
        "title": 'Salud mental: UNAM ofrece apoyo psicológico a la comunidad', 
        "url": 'https://www.gaceta.unam.mx/apoyo-psicologico-unam/', 
        "snippet": 'A través de la Facultad de Psicología, la UNAM brinda atención y acompañamiento en salud mental para estudiantes, académicos y trabajadores.' 
    }
]

def search_articles(query, articles):
    """
    Filtra artículos basándose en una búsqueda preprocesada.
    Ahora, en lugar de buscar texto exacto, busca si alguna de las palabras clave
    de la consulta aparece en el texto clave del artículo.
    """
    # Preprocesamos la consulta del usuario para obtener las palabras clave.
    query_tokens = preprocess_text(query)
    
    if not query_tokens:
        return []
    
    results = []
    
    for article in articles:
        # Combinamos título y snippet para tener todo el texto del artículo.
        article_text = article['title'] + " " + article['snippet']
        
        # Preprocesamos el texto del artículo.
        article_tokens = preprocess_text(article_text)
        
        # Verificamos si CUALQUIERA de las palabras de la consulta está en las palabras del artículo.
        # Esto es mucho más flexible que la búsqueda anterior.
        if any(token in article_tokens for token in query_tokens):
            results.append(article)
            
    return results

def main():
    """
    Función principal que ejecuta el programa de búsqueda en la consola.
    """
    print("--- Buscador de Gaceta UNAM (v1.2 - con Lematizador) ---")
    print("Escribe tu búsqueda o 'salir' para terminar el programa.")
    
    while True:
        user_input = input("\n> Buscar: ")
        
        if user_input.lower() == 'salir':
            print("¡Hasta luego!")
            break
        
        search_results = search_articles(user_input, mock_articles)
        
        if search_results:
            print(f"\n--- Se encontraron {len(search_results)} resultados para '{user_input}' ---")
            for i, result in enumerate(search_results, 1):
                print(f"\n{i}. {result['title']}")
                print(f"   URL: {result['url']}")
                print(f"   Fragmento: {result['snippet']}")
        else:
            print(f"\n--- No se encontraron resultados para '{user_input}' ---")

if __name__ == "__main__":
    # Actualizamos el script principal para que llame a la función `main` del buscador
    main()