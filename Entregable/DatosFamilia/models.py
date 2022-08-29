from django.db import models

class familiar(models.Model):
    nombre = models.CharField(max_length=30)
    cumpleaños = models.DateField()
    parentesco = models.CharField(max_length=12)

