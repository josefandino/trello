from django.utils import timezone
from django.db import models

from ..boards.models import Board

class List(models.Model):
   name = models.CharField(max_length=60, blank=False, null=False)
   timestamp = models.DateTimeField('Fecha registro', default=timezone.now)
   position = models.IntegerField(default=None)

   board = models.ForeignKey(Board, on_delete=models.PROTECT, related_name='list')


   def __str__(self):
      return self.name

# ○ Nombre (Texto)
#   ○ Tablero (Llave foránea) 
#   ○ Fecha de creación (Fecha y hora)
#   ○ Posición (Entero)
