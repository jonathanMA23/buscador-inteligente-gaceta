# -*- coding: utf-8 -*-

# --- Mock Data ---
# Simula una base de datos de artículos para la búsqueda.
# Es la misma información que se usó en el archivo HTML.
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
    Filtra una lista de artículos basándose en un término de búsqueda.
    La búsqueda no distingue entre mayúsculas y minúsculas y busca en el título y el snippet.
    """
    # Convierte la consulta a minúsculas para una búsqueda insensible a mayúsculas.
    query = query.lower().strip()
    
    # Si la consulta está vacía, no devuelve resultados.
    if not query:
        return []
    
    # Lista para almacenar los resultados encontrados.
    results = []
    
    # Itera sobre cada artículo en la base de datos.
    for article in articles:
        # Comprueba si la consulta está en el título o en el snippet del artículo.
        if query in article['title'].lower() or query in article['snippet'].lower():
            results.append(article)
            
    return results

def main():
    """
    Función principal que ejecuta el programa de búsqueda en la consola.
    """
    print("--- Buscador de Gaceta UNAM (Versión de Consola en Python) ---")
    print("Escribe tu búsqueda o 'salir' para terminar el programa.")
    
    # Bucle infinito para permitir múltiples búsquedas.
    while True:
        # Solicita al usuario que ingrese su búsqueda.
        user_input = input("\n> Buscar: ")
        
        # Si el usuario escribe 'salir', el programa termina.
        if user_input.lower() == 'salir':
            print("¡Hasta luego!")
            break
        
        # Llama a la función de búsqueda con la entrada del usuario.
        search_results = search_articles(user_input, mock_articles)
        
        # Muestra los resultados encontrados.
        if search_results:
            print(f"\n--- Se encontraron {len(search_results)} resultados para '{user_input}' ---")
            for i, result in enumerate(search_results, 1):
                print(f"\n{i}. {result['title']}")
                print(f"   URL: {result['url']}")
                print(f"   Fragmento: {result['snippet']}")
        else:
            # Informa al usuario si no se encontraron resultados.
            print(f"\n--- No se encontraron resultados para '{user_input}' ---")

# Este bloque asegura que la función main() se ejecute solo cuando el script se corre directamente.
if __name__ == "__main__":
    main()