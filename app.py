# Importamos Flask y las herramientas para manejar peticiones web y renderizar HTML
from flask import Flask, render_template, request

# Importamos todos nuestros módulos y funciones del motor de búsqueda
from src.data import mock_articles
from src.indexer import build_index, search_with_ranking
from src.resaltado import highlight

# Inicializamos la aplicación de Flask
app = Flask(__name__)

# --- Fase de Indexación (se ejecuta una sola vez al iniciar el servidor) ---
print("Iniciando el servidor y construyendo el índice de búsqueda...")
vectorizer, tfidf_matrix = build_index(mock_articles)
print("¡Servidor listo para recibir búsquedas!")
# -------------------------------------------------------------------------

# Definimos la ruta principal de nuestra aplicación web
@app.route('/', methods=['GET', 'POST'])
def home():
    search_query = ""
    results = []

    # Si el usuario envía el formulario (hace una búsqueda)...
    if request.method == 'POST':
        search_query = request.form.get('query', '')
        if search_query:
            # Usamos nuestro motor de búsqueda para obtener los resultados con ranking
            search_results = search_with_ranking(search_query, vectorizer, tfidf_matrix, mock_articles)
            
            # Procesamos los resultados para el frontend
            for result in search_results:
                article = result['article']
                score = result['score']
                
                # Creamos el fragmento y lo resaltamos en formato HTML
                fragment = " ".join(article['content'].split()[:30]) + "..."
                highlighted_fragment = highlight(fragment, search_query, format='html')
                
                results.append({
                    'title': article['title'],
                    'url': article['url'],
                    'score': f"{score:.2f}",
                    'fragment': highlighted_fragment
                })

    # Renderizamos la plantilla HTML, pasándole los resultados para que los muestre
    return render_template('index.html', query=search_query, results=results)

if __name__ == '__main__':
    # Este modo 'debug' es útil para desarrollo
    app.run(debug=True)
