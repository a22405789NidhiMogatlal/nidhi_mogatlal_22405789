from django.shortcuts import render
from .models import Curso

# Create your views here.

def cursos_view(request):
    curso=Curso.object.select_related('professor').prefetch_related('alunos').all()
    return render(request,'esolaOnline/cursos.html',{'cursos':cursos})
