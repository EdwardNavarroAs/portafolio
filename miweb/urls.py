from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('estudios/', views.studies, name='estudios'),
    path('portafolio/', views.portfolio, name='portafolio'),
]
