from django.db import models

class Carro(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año = models.IntegerField()
    color = models.CharField(max_length=50)
    placa = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.placa}"
    
    class Meta:
        verbose_name = "Carro"
        verbose_name_plural = "Carros"
        ordering = ['-año', 'marca']
