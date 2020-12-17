from django.db import models

from django.utils import timezone
# from ..users.models import User
# from rest_framework_simplejwt.state import User
from django.contrib.auth.models import User
from ..list.models import List


class Card(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    timestamp = models.DateTimeField(default=timezone.now)
    expiration_date = models.DateTimeField(default=timezone.now)
    position = models.IntegerField(default=None)

    members = models.ManyToManyField(User, related_name='card')
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='card')

    def __str__(self):
        return self.name
