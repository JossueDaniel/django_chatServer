from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Asigna el usuario autenticado como propietario de la sala
        if not self.pk:  # Si es una nueva instancia
            self.owner = kwargs.pop('owner', None)
        super(Room, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
