from django.utils import timezone
from django.db import models

from ..boards.models import Board
from ..users.models import User


class List(models.Model):
   name = models.CharField(max_length=60, blank=False, null=False)
   timestamp = models.DateTimeField('Fecha registro', default=timezone.now)
   position = models.IntegerField(default=None)

   board = models.ManyToManyField(Board, related_name='list')
   members = models.ManyToManyField(User, related_name='list')

   def __str__(self):
      return self.name

# ○ Nombre (Texto)
#   ○ Tablero (Llave foránea) 
#   ○ Fecha de creación (Fecha y hora)
#   ○ Posición (Entero)
