from django.db import models

# Create your models here.
class Ginasio(models.Model):
    nome=models.CharField(max_length=255)
    def __str__(self):
        return f"{self.nome}"


class PersonalTrainer(models.Model):
    nome=models.CharField(max_length=255)
    ginasio=models.ForeignKey(Ginasio,on_delete=models.CASCADE,related_name="personal_trainers")

    def __str__(self):
        return f"{self.nome}"

class Cliente(models.Model):
    nome=models.CharField(max_length=255)
    ginasio=models.ForeignKey(Ginasio,on_delete=models.CASCADE,related_name="clientes")

    def __str__(self):
        return f"{self.nome}"


class Sessao(models.Model):

    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE,related_name="membro")
    pt=models.ForeignKey(PersonalTrainer,on_delete=models.CASCADE,related_name="PT")
    data=models.DateField()
    hora=models.TimeField()

    class Meta:
        unique_together=("pt","data","hora")
    def __str__(self):
        return f"{self.cliente} - {self.pt} - {self.data}"
