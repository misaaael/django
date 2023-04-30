from django.shortcuts import render, get_object_or_404

from galeria.models import *



def index(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})


def index_teste(request):
    fotografia = Fotografia.objects.order_by('nome').filter(publicada=True)
    return render(request, 'galeria/index_teste.html', {"cards": fotografia})

def buscar (request):
    return render(request, "buscar.html")
