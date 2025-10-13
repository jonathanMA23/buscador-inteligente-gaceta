
import colorama
# Importamos los datos de ejemplo desde su nuevo archivo
from .data import mock_articles
# Importamos a nuestros nuevos especialistas en indexación y ranking
from .indexer import build_index, search_with_ranking

# ¡Importamos a nuestro nuevo especialista en resaltado!
from .resaltado import highlight_fragment

# ¡NUEVO! Inicializamos colorama. Esto "activa" la compatibilidad de colores.
# autoreset=True hace que cada print vuelva al estilo por defecto automáticamente.
colorama.init(autoreset=True)


def main():
    """
    Función principal que ejecuta el buscador.
    """
    print("--- Buscador de Gaceta UNAM (v2.0 - con Ranking de Relevancia) ---")
    
    # 1. Fase de Indexación (se hace una sola vez al principio)
    # Llama al especialista para construir el índice TF-IDF
    vectorizer, tfidf_matrix = build_index(mock_articles)
    
    # 2. Bucle de Búsqueda
    while True:
        user_input = input("Escribe tu búsqueda o 'salir' para terminar el programa.\n> Buscar: ")
        
        if user_input.lower() == 'salir':
            print("¡Hasta luego!")

            break
            
        # Realizamos la búsqueda usando el nuevo sistema de ranking
        search_results = search_with_ranking(user_input, vectorizer, tfidf_matrix, mock_articles)
        
        if not search_results:
            print(f"\n--- No se encontraron resultados para '{user_input}' ---")
        else:
            print(f"\n--- Se encontraron {len(search_results)} resultados para '{user_input}' (ordenados por relevancia) ---")
            # Iteramos sobre los resultados, que ahora incluyen un puntaje
            for i, result in enumerate(search_results):
                article = result['article']
                score = result['score']
                print(f"{i+1}. {article['title']} (Relevancia: {score:.2f})")
                print(f"   URL: {article['url']}")
                # Mostramos un pequeño fragmento del contenido para dar contexto
                fragment = " ".join(article['content'].split()[:20]) + "..."
                print(f"   Fragmento: {fragment}\n")

if __name__ == '__main__':
    main()

