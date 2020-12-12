from django.db import models

class List(models.Model):
   name = models.CharField(max_length=60, blank=False, null=False)

# ○ Nombre (Texto)
#   ○ Tablero (Llave foránea) 
#   ○ Fecha de creación (Fecha y hora)
#   ○ Posición (Entero)
