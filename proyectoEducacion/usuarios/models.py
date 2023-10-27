from django.db import models

# Create your models here.
class Pais(models.Model): 
    idPais_id = models.IntegerField(primary_key = True) 
    nombrePais = models.CharField(max_length=100, unique=True)

class Provincia(models.Model): 
    idProvincia_id = models.IntegerField(primary_key = True) 
    nombreProvincia = models.CharField(max_length=100) 
    fkPais = models.ForeignKey(Pais, on_delete=models.CASCADE)

#Hola Mundo

class Ciudad(models.Model): 
    idCiudad_id = models.IntegerField(primary_key = True) 
    nombreCiudad = models.CharField(max_length=100) 
    fk_Provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE) 
    fk_Pais = models.ForeignKey(Pais, on_delete=models.CASCADE)