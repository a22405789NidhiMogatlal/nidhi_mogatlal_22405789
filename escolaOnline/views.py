from django.shortcuts import render
from .models import Curso


# Create your views here.

def cursos_view(request):
    cursos=(Curso.objects.select_related().prefetch_related().all())
    return render(request,'escolaOnline/cursos.html',{'cursos':cursos})

def profs_view(request):
    profs=Professor.objects.prefetch_related().all()
    return render(request,'escolaOnline/profs.html',{'profs':cursos})

