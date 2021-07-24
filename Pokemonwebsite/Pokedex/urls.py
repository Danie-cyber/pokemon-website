from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('<str:pk_name>/', views.pokemon, name='pokemon_lookup'),
]
