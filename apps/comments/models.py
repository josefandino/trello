from django.db import models
from django.utils import timezone


from ..users.models import User
from ..cards.models import Card
from ..list.models import List


class Comment(models.Model):
    message = models.CharField(max_length=150)
    timestamp = models.DateTimeField('Fecha registro', default=timezone.now)

    members = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.message


