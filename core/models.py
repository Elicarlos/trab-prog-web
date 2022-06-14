

from django.db import models

# Create your models here.

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to="produtos/%d/%m/%Y/")
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    
