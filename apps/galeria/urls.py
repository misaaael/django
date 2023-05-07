from django.urls import path
from apps.galeria.views import index, imagem, index_teste, buscar

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('index_teste', index_teste, name='index_teste'),
    path('buscar', buscar, name='buscar'),
]