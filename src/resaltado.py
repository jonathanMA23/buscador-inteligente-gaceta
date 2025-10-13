
from .preprocesamiento import preprocess_text

# ¡NUEVO! Definimos los tags para el resaltado en HTML
HIGHLIGHT_START_HTML = '<span class="bg-yellow-200 rounded-md px-1">'
HIGHLIGHT_END_HTML = '</span>'

# Códigos de escape ANSI para la terminal
HIGHLIGHT_START_TERMINAL = '\033[1;93m'
HIGHLIGHT_END_TERMINAL = '\033[0m'

def highlight(fragment, query, format='terminal'):
    """
    Resalta los términos de la consulta en un fragmento de texto.
    Soporta formato 'terminal' o 'html'.
    """
    if format == 'html':
        start_tag, end_tag = HIGHLIGHT_START_HTML, HIGHLIGHT_END_HTML
    else: # Por defecto, usa el formato de terminal
        start_tag, end_tag = HIGHLIGHT_START_TERMINAL, HIGHLIGHT_END_TERMINAL
        
    query_stems = set(preprocess_text(query))
    
    if not query_stems:
        return fragment

    highlighted_words = []
    original_words = fragment.split()

    for word in original_words:
        clean_word = ''.join(filter(str.isalnum, word))
        processed_stems = preprocess_text(clean_word)
        
        if processed_stems and processed_stems[0] in query_stems:
            highlighted_words.append(f"{start_tag}{word}{end_tag}")
        else:
            highlighted_words.append(word)
    
    # Usamos .join() para reconstruir el fragmento
    return " ".join(highlighted_words)