from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    celular = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='carnets/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.celular})"