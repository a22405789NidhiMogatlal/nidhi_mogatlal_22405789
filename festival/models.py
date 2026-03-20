from django.db import models

# Create your models here.


class GeneroMusical(models.Model):
    nome=models.CharField(max_length=255)
    def __str__(self):
        return f"{self.nome}"

class Banda(models.Model):
    nome=models.CharField(max_length=255)
    genero=models.ForeignKey(GeneroMusical,on_delete=models.CASCADE,related_name="bandas")
    def __str__(self):
        return f"{self.nome}"


class Festival(models.Model):
    nome=models.CharField(max_length=255)
    bandas=models.ManyToManyField(Banda,related_name="festivais")
    def __str__(self):
        return f"{self.nome}"