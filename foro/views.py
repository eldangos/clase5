from django.shortcuts import render
from .models import Noticia

# Create your views here.
def foro(request):
    noticia=Noticia.objects.all()
    return render(request,"foro/noticia.html",
                  {'noticia':noticia})