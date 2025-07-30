# Importamos las funciones necesarias para definir rutas
from django.urls import path

# Importamos las vistas definidas en views.py de esta misma app ('miweb')
from . import views

# Aquí se definen las rutas específicas para la aplicación 'miweb'.
# Estas rutas se incluyen desde el archivo core/urls.py usando include('miweb.urls')

urlpatterns = [
    # Ruta para la página principal del sitio ("/")
    # Esta vista se llama 'home' y debe estar definida en views.py
    path('', views.home, name='home'),

    # Ruta para la página de "Estudios" ("/studies/")
    # Accede a la vista 'studies' en views.py
    path('studies/', views.studies, name='studies'),

    # Ruta para la página de "Portafolio" ("/portfolio/")
    # Accede a la vista 'portfolio' en views.py
    path('portfolio/', views.portfolio, name='portfolio'),
]

# Nota:
# El parámetro 'name' en cada path permite usar {% url 'nombre' %} en las plantillas HTML,
# lo cual hace que las URLs sean más fáciles de manejar y mantener.
