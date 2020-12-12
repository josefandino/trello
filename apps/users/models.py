from django.db import models
from django.utils import timezone

class User(models.Model):
   name = models.CharField(max_length=120, blank=False, null=False)
   lastname = models.CharField(max_length=120, blank=False, null=False)
   email = models.EmailField(max_length=120, blank=False, null=False, unique=True)
   password = models.CharField(max_length=40)
   timestamp = models.DateTimeField(default=timezone.now)

   class Meta:
      ordering = ['name']
      verbose_name = 'User'
      verbose_name_plural = 'Users'
   
   def __str__(self):
      return '{0},{1}'.format(self.lastname, self.name)
