from django.shortcuts import render
from .models import *


# Create your views here.

def cursos_view(request):
    cursos=(Curso.objects.select_related().prefetch_related().all())
    return render(request,'escolaOnline/cursos.html',{'cursos':cursos})

def profs_view(request):
    profs=Professor.objects.all()
    return render(request,'escolaOnline/profs.html',{'profs':profs})

def alunos_view(request):
    alunos=Aluno.objects.all()
    return render(request,'escolaOnline/alunos.html',{'alunos':alunos})


def curso_view(request, id):
    curso=Curso.objects.get(id=id)       
    return render(request, 'escolaOnline/curso.html', {'curso': curso})