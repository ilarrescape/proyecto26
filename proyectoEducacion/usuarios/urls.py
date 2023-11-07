from django.urls import path
from . import views

urlpatterns = [
    path('lista_personas/', views.lista_personas, name='lista_personas'),
    path('agregar/', views.agregar_persona, name='agregar_persona'),
]