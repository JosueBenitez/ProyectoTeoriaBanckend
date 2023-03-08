from django.db import models

# Create your models here.
class Temperatura:
    temperatura = models.DecimalField(max_digits = 18, decimal_places = 2)
    humedad = models.DecimalField(max_digits = 18, decimal_places = 2)
    fecha = models.DateTimeField()