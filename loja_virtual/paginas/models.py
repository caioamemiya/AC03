from django.db import models

# Create your models here.

class Produto(models.Model):
    codigo = models.CharField(max_length=30)
    nome = models.CharField(max_length=60)

class Orcamento(models.Model):
    codigo = models.IntegerField()
    data =  models.DateField(auto_now=True)
    status = models.IntegerField()
    valor_total = models.DecimalField(decimal_places=2, max_digits=15)

class ItemOrcamento(models.Model):
    codigo_item = models.IntegerField()
    codigo_orcamento = models.IntegerField()
    codigo_produto = models.IntegerField()
    quantidade = models.DecimalField(decimal_places=2, max_digits=10)
    valor_unitario = models.DecimalField(decimal_places=2,max_digits=15)
