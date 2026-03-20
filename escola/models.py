from django.db import models

# Create your models here.


class Escola(models.Model):
    nome=models.CharField(max_length=255)
    def __str__(self):
        return f"{self.nome}"
    


class Turma(models.Model):
    nome=models.CharField(max_length=100)
    escola=models.ForeignKey(Escola,on_delete=models.CASCADE,related_name="turmas")

    def __str__(self):
        return f"{self.nome}"


class Aluno(models.Model):
    nome=models.CharField(max_length=255)
    numero=models.IntegerField()
    turma=models.ForeignKey(Turma, on_delete=models.CASCADE, related_name="alunos")

    def __str__(self):
        return f"{self.nome}"


class Professor(models.Model):
    nome=models.CharField(max_length=255)
    turma=models.OneToOneField(Turma,on_delete=models.CASCADE,related_name="turma")

    def __str__(self):
        return f"{self.nome}"

