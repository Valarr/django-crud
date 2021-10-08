from django.db import models

# Create your models here.

class Consulta(models.Model):
    ticket_id = models.CharField(max_length=128)
    approved = models.BooleanField(default=False)
#   nome = models.CharField(max_length=127)
#    id = models.AutoField
#    cpf = models.TextField(max_length=11,null=True)
#    adress = models.TextField(max_length=127,null=True)
#    age = models.PositiveIntegerField(null=True)
#    requested_amount = models.DecimalField(max_digits=7, decimal_places=2,null=True)
#    ticket_id = models.CharField(max_length=5)
#    aproved = models.BooleanField(default=False,null=True)