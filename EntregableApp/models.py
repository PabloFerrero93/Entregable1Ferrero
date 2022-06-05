from django.db import models

class Familia(models.Model):
    apellido = models.CharField(max_length=40)

class Papa(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    nacimiento = models.DateField()
   

class Mama(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    nacimiento = models.DateField()
    

class Hermano(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    nacimiento = models.DateField()
