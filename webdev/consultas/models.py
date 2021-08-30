from django.db import models

# Create your models here.

class Consulta(models.Model):
    nome = models.CharField(max_length=127)
    id = models.AutoField
    cpf = models.TextField(max_length=11)
    adress = models.TextField(max_length=127)
    age = models.PositiveIntegerField(max_length=3)
    requested_amount = models.DecimalField
    ticket_id = models.CharField(max_length=5)
    aproved = models.BooleanField