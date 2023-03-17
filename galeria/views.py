from django.shortcuts import render
from galeria.models import Fotografia



def index(request):
    fotografias = Fotografia.objects.all()  #traz todos os itens do nosso banco 
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request):
    return render(request, 'galeria/imagem.html')
# Create your views here.
