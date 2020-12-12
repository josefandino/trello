from django.db import models
from django.utils import timezone

class Comments(Models.Model):
   timestamp = models.DateTimeField('Fecha registro', default=timezone.now)

# ● Comentarios
#     ○ Tarjeta (Llave foránea)
#     ○ Mensaje (Texto)
#     ○ Dueño (Llave foránea)
#     ○ Fecha de creación (Fecha y hora)