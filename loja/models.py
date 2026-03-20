from django.db import models

# Create your models here.
class Loja(models.Model):
    nome=models.CharField(max_length=255)
    def __str__(self):
        return f"{self.nome}"

class Categoria(models.Model):
    nome=models.CharField(max_length=255)
    def __str__(self):
        return f"{self.nome}"

class Produto(models.Model):
    nome=models.CharField(max_length=255)
    loja=models.ForeignKey(Loja,on_delete=models.CASCADE,related_name="produtos")
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE,related_name="produtos")

    def __str__(self):
        return f"{self.nome}"

class Cliente(models.Model):
    nome=models.CharField(max_length=255)
    morada=models.CharField(max_length=255,unique=True)
    def __str__(self):
        return f"{self.nome}"

class Pedido(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE,related_name="pedido")

    def __str__(self):
        return f"{self.cliente}: {self.data_criacao}"

class Item(models.Model):
    pedido=models.ForeignKey(Pedido,on_delete=models.CASCADE,related_name="item")
    produto= models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="itens") 
    quantidade=models.IntegerField()
    def __str__(self):
        return f"{self.produto}: {self.quantidade}"