from django.urls import path
from . import views

urlpatterns=[
    path('cursos', views.cursos_view,name="cursos"),
    path('', views.cursos_view),
    path('alunos', views.alunos_view,name="alunos"),
    path('curso/<int:id>', views.curso_view, name="curso"),
    path('profs', views.profs_view,name="profs"),
] 
