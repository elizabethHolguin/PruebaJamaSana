from django.db import models
from models import Suscripcion

# Create your models here.
class FormaDePago(models.Model):
    forma_pago = models.CharField(max_length=250)

    def __str__(self):
        return self.forma_pago
    
class Iva(models.Model):
    porcentaje = models.FloatField()
    nombre_impuesto = models.CharField(max_length=300)

    def __str__(self):
        return self.nombre_impuesto

class Tarjeta(models.Model):
    nombre_propietario = models.CharField(max_length=200)
    tipo_tarjeta = models.CharField(max_length=200)
    fecha_caducidad = models.DateField()
    direccion_facturacion = models.CharField(max_length=350)
    cvv = models.IntegerField(default=0)
    numero_tarjeta = models.CharField(max_length=16)

    def __str__(self):
        return self.nombre_propietario + ' . ' + self.numero_tarjeta

class Factura(models.Model):
    id_suscripcion = models.ForeignKey(Suscripcion, on_delete=models.CASCADE)
    id_forma_pago = models.ForeignKey(FormaDePago, on_delete=models.CASCADE)
    id_iva = models.ForeignKey(Iva, on_delete=models.CASCADE)
    monto = models.FloatField()

    def __str__(self):
        return self.id_iva