from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_carros, name='lista_carros'),
    path('crear/', views.crear_carro, name='crear_carro'),
    path('editar/<int:pk>/', views.editar_carro, name='editar_carro'),
    path('eliminar/<int:pk>/', views.eliminar_carro, name='eliminar_carro'),
]
