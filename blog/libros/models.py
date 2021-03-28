from django.db import models

# Create your models here.
class Registro(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(max_length=40)
    contra= models.CharField(max_length=60)
    
    
    def __str__(self):
        return self.nombre

class login(models.Model):

    id = models.AutoField(primary_key=True)
    
    correo = models.EmailField(max_length=40)
    contra= models.CharField(max_length=60)
    
    
    def __str__(self):
        return self.correo
