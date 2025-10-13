Proyecto: Buscador Inteligente para Gaceta UNAM
Este proyecto es un motor de búsqueda inteligente construido en Python desde cero, aplicando conceptos de Procesamiento del Lenguaje Natural (PLN) y Recuperación de Información (RI). El objetivo es ofrecer una experiencia de búsqueda moderna y relevante para los artículos de Gaceta UNAM.

Cómo ejecutar este proyecto
Para poner en marcha el buscador en cualquier computadora con Python 3 instalado, sigue estos pasos:

1. Clonar el Repositorio
Primero, descarga el código fuente desde GitHub a tu máquina local.

git clone [https://github.com/jonathanMA23/buscador-inteligente-gaceta]
cd buscador-inteligente-gaceta

2. Crear y Activar un Entorno Virtual (Recomendado)
Crear un entorno virtual aísla las dependencias de este proyecto de otros que tengas en tu sistema.

# Crear el entorno
python3 -m venv venv

# Activar el entorno (en macOS/Linux)
source venv/bin/activate

En Windows, el comando de activación es .\venv\Scripts\activate

3. Instalar las Dependencias
Con el entorno activado, instala todas las bibliotecas necesarias usando el archivo requirements.txt con un solo comando.

pip install -r requirements.txt

4. Descargar Modelos de Lenguaje
Nuestro motor de búsqueda necesita los "cerebros" pre-entrenados de NLTK y spaCy para funcionar.

# Descargar modelos de NLTK (punkt y stopwords)
python3 -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"

# Descargar modelo de spaCy para español
python3 -m spacy download es_core_news_sm

5. ¡Lanzar la Aplicación Web!
Finalmente, inicia el servidor web de Flask.

python3 app.py

Abre tu navegador y ve a la dirección que aparece en la terminal (usualmente https://www.google.com/search?q=http://127.0.0.1:5000) para usar el buscador.

Fases del Proyecto
Fase 1: Prototipo Inicial y Planificación
Objetivo: Crear un buscador básico y estructurar el proyecto.

Técnicas: Búsqueda simple por subcadenas.

Resultado: Scripts iniciales y README.md con el plan de desarrollo.

Fase 2: Preprocesamiento de Textos
Objetivo: "Limpiar" y "estandarizar" el texto para una búsqueda más inteligente.

Técnicas: Tokenización, Normalización (minúsculas), Stop Words (NLTK), Lematización (spaCy) y Stemming (NLTK).

Resultado: Búsquedas flexibles que entienden diferentes formas de una palabra (ej. "universidad" vs "universidades").

Fase 3: Indexación y Modelo de Recuperación
Objetivo: Ordenar los resultados por relevancia.

Técnicas: Modelo de espacio vectorial con TF-IDF (scikit-learn).

Resultado: Los resultados más importantes aparecen primero, cada uno con un puntaje de relevancia.

Fase 4: Expansión y Mejora de la Experiencia
Objetivo: Mejorar la visualización de los resultados para el usuario.

Técnicas: Resaltado de Términos (Highlighting) de las palabras clave en los resultados.

Resultado: El usuario puede ver visualmente por qué un resultado es relevante.

Fase 5: Creación de la Interfaz Web
Objetivo: Sacar el proyecto de la terminal y hacerlo accesible desde un navegador.

Técnicas: Creación de un servidor web con Flask y una interfaz de usuario con HTML.

Resultado: Una aplicación web completamente funcional.

[def]: https://github.com/jonathanMA23/buscador-inteligente-gaceta