Proyecto: Buscador Inteligente para Gaceta UNAM
1. Objetivo del Proyecto
Desarrollar un sistema de Recuperación de Información (RI) eficiente y preciso para el acervo de la Gaceta UNAM. El proyecto aplicará técnicas de Procesamiento del Lenguaje Natural (PLN) para mejorar la relevancia de los resultados de búsqueda, superando las limitaciones de una búsqueda por coincidencia de texto simple.

Este proyecto se basa en los temarios de las asignaturas "Procesamiento del Lenguaje Natural" y "Análisis y Procesamiento Inteligente de Textos".

2. Fases del Proyecto
Fase 1: Prototipo Inicial y Baseline (¡Completada!) ✔️
En esta fase, creamos una primera versión funcional del buscador.

Actividades:

Diseño de la interfaz de usuario (HTML).

Implementación de la lógica de búsqueda básica en Python y JavaScript.

Técnica utilizada: Búsqueda por subcadena (query in text).

Resultado: Un prototipo que encuentra coincidencias exactas del texto buscado, pero no entiende sinónimos, plurales o el contexto.

Fase 2: Preprocesamiento de Textos (Fundamentos de PLN)
El objetivo de esta fase es "limpiar" y "normalizar" tanto los documentos de la Gaceta como las consultas del usuario para que la computadora pueda procesarlos de manera más inteligente.

Actividades:

Tokenización: Separar el texto en unidades mínimas (palabras o "tokens").

Normalización: Convertir todo el texto a minúsculas.

Eliminación de Palabras Funcionales (Stop Words): Quitar palabras muy comunes que no aportan significado (ej. "el", "la", "de", "que").

Lematización o Stemming: Reducir las palabras a su raíz o lema. Por ejemplo, "universidades", "universitaria" y "universitario" se convertirían en "universidad". Esto permite que una búsqueda por "universidad" encuentre todos esos resultados.

Conceptos del temario: PLN (3.2.1, 4.1), Análisis (2.2.1)

Fase 3: Indexación y Modelo de Recuperación
Aquí construiremos el "cerebro" del buscador. En lugar de leer todos los documentos cada vez que hay una búsqueda, crearemos un índice optimizado para hacer consultas ultra rápidas.

Actividades:

Crear un Índice Invertido: Es una estructura de datos que mapea cada palabra (lema) a una lista de los documentos en los que aparece. Es como el índice de un libro, pero para todas las palabras.

Implementar un Modelo de Ponderación (TF-IDF): Calcularemos la importancia de cada palabra en cada documento. TF-IDF (Term Frequency-Inverse Document Frequency) es un método estadístico que da más peso a las palabras que son frecuentes en un documento pero raras en el resto de la colección. Esto nos permitirá ordenar los resultados por relevancia.

Conceptos del temario: Análisis (2.2.2, 2.2.3.2)

Fase 4: Expansión y Mejora de la Experiencia
Con el motor de búsqueda funcionando, podemos añadirle funcionalidades avanzadas para hacerlo aún más potente y amigable.

Actividades:

Expansión de Consultas: Sugerir sinónimos o términos relacionados para mejorar la búsqueda (ej. si buscas "académico", también buscar "profesor" o "investigador").

Resaltado de Términos (Highlighting): Marcar en los resultados las palabras que coincidieron con la búsqueda.

Evaluación del Sistema: Medir la eficacia del buscador utilizando métricas como Precisión y Recall.

Conceptos del temario: Análisis (2.2.3.1.1, 2.2.5), PLN (3.3, 7.1)

3. Tecnologías Propuestas
Lenguaje de Programación: Python 3.

Bibliotecas de PLN:

NLTK (Natural Language Toolkit): Ideal para empezar con tokenización, stop words y stemming.

spaCy: Una biblioteca más moderna y potente para tareas de PLN más avanzadas.

Bibliotecas de Cálculo:

Scikit-learn: Contiene implementaciones eficientes de TF-IDF.

4. Estructura del Repositorio en GitHub
/
├── data/                     # Aquí podríamos guardar los artículos de la Gaceta en formato .txt o .json
├── src/                      # Código fuente del proyecto
│   ├── preprocesamiento.py   # Funciones para limpiar el texto
│   └── buscador.py           # Lógica principal del motor de búsqueda
├── main.py                   # Script principal para ejecutar el buscador en consola
└── README.md                 # La explicación del proyecto (este archivo)
