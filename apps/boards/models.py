from django.utils import timezone
from django.db import models

from ..users.models import User


class Board(models.Model):
    name = models.CharField(max_length=60, blank=False, null=False)
    description = models.CharField(max_length=150, blank=False, null=False)
    timestamp = models.DateTimeField(default=timezone.now)
    visibility = models.BooleanField(default=False)

    # favorite = models.ManyToManyField(User, through="FavoriteBoard", related_name='board')

    members = models.ManyToManyField(User, related_name='board')

    def __str__(self):
        return self.name

# class FavoriteBorad(models.models):
#  favorite = models.IntegerField(default=None)
