from django.utils import timezone
from django.db import models

class Board(models.Model):
   name = models.CharField(max_length=60, blank=False, null=False)
   description = models.CharField(max_length=150, blank=False, null=False)
   timestamp = models.DateTimeField(default=timezone.now)


#  ● Tableros
#   ○ Nombre (Texto)
#   ○ Descripción (Texto)
#   ○ Fecha de creación (Fecha y hora)
#   ○ Dueño (Llave foránea)
#   ○ Favorito (Muchos a muchos)
#   ○ Visibilidad (Texto, selección)
#   ○ Miembros (Muchos a muchos)
