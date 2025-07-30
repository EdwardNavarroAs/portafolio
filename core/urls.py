"""
URL configuration for the core project.

Este archivo es el punto central de enrutamiento de Django.
Su propósito es redirigir las URLs principales del sitio hacia las apps correspondientes.

Más información:
https://docs.djangoproject.com/en/5.2/topics/http/urls/

Ejemplos:
- Para una vista basada en funciones:
      1. Importa la vista: from my_app import views
      2. Añade un path: path('', views.home, name='home')
- Para vistas basadas en clases:
      1. Importa la clase: from other_app.views import Home
      2. Añade un path: path('', Home.as_view(), name='home')
- Para incluir otras configuraciones de URLs:
      1. Importa include: from django.urls import include, path
      2. Añade un path: path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Ruta para acceder al panel de administración de Django en /admin/
    path('admin/', admin.site.urls),
    
    # Incluye todas las rutas definidas en la aplicación 'miweb'
    # Esto permite mantener separadas las rutas de cada app.
    path('', include('miweb.urls')),
]
