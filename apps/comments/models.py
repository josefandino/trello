from django.db import models
from django.utils import timezone


from ..users.models import User
from ..cards.models import Card
from ..list.models import List


class Comment(models.Model):
   message = models.CharField(max_length=150)
   timestamp = models.DateTimeField('Fecha registro', default=timezone.now)

   members = models.ManyToManyField(User, related_name='comments')
   card = models.ManyToManyField(Card, related_name='comments')
   list = models.ForeignKey(List, on_delete=models.PROTECT)

   def __str__(self):
      return self.message

