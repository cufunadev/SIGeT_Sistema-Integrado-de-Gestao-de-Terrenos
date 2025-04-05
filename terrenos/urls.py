from django.urls import path
from . import views
from django.contrib import admin




urlpatterns = [
    path('cadastrar/', views.cadastrar_terreno, name='cadastrar_terreno'),
    path('editar/<int:pk>/', views.editar_terreno, name='editar_terreno'),
    path('excluir/<int:pk>/', views.excluir_terreno, name='excluir_terreno'),
]
