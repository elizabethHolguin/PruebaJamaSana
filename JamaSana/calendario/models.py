from django.db import models
from models import Cliente
from models import Comidas

# Create your models here.

class Calendario(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_cliente
        
class Dias(models.Model):
    id_calendario = models.ForeignKey(Calendario, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_calendario

class Detalle_dias(models.Model):
    id_dias = models.ForeignKey(Dias, on_delete=models.CASCADE)
    hora_entrega = models.DateTimeField('Hora de entrega')
    id_comida = models.ForeignKey(Comidas, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_dias