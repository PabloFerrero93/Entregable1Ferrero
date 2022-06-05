from django.db import models

class Familia(models.Model):
    apellido = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.apellido

class Papa(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    nacimiento = models.DateField()

    def __str__(self) -> str:
        return self.nombre
   

class Mama(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    nacimiento = models.DateField()

    def __str__(self) -> str:
        return self.nombre
    

class Hermano(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    nacimiento = models.DateField()

    def __str__(self) -> str:
        return self.nombre
