# Este archivo define un "context processor" personalizado.
# Un context processor en Django es una función que retorna un diccionario de variables
# que estarán disponibles automáticamente en todas las plantillas del proyecto.

def navbar_context(request):
    # Definimos los ítems del navbar y el título del sitio.
    # Esto evita tener que repetir este contexto en cada vista manualmente.
    return {
        'navbar_items': [
            {'name': 'Inicio', 'url_name': 'home'},
            {'name': 'Estudios', 'url_name': 'studies'},
            {'name': 'Portafolio', 'url_name': 'portfolio'},
        ],
        'title': 'Mi Portafolio',
    }
