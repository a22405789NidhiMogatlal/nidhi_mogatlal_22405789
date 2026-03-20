from django.db import models

# Create your models here.
class Ingrediente(models.Model):
    nome=models.CharField(max_length=255)
    def __str__(self):
        return f"{self.nome}"

class Receita(models.Model):
    nome=models.CharField(max_length=255)
    ingredientes=models.ManyToManyField(Ingrediente,related_name="receita")
    def __str__(self):
        return f"{self.nome}"

class Utilizador(models.Model):
    nome=models.CharField(max_length=255)
    recFav=models.ManyToManyField(Receita,related_name="favoritos")
    def __str__(self):
        return f"{self.nome}"
