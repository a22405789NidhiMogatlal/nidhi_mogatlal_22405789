from django.urls import path
from . import views

urlpatterns=[
    path('cursos', views.cursos_view,name="cursos"),
    path(' ', views.cursos_view),
    path('alunos', views.cursos_view,name="alunos")
]