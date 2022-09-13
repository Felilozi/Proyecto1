from django.db import models

class Familia(models.Model):
    nombre = models.CharField(max_length=60)
    year = models.IntegerField()
    fecha = models.DateField()
    vinculo =models.CharField(max_length=60)

