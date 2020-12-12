from django.db import models

class User(models.Model):
   name = models.CharField(max_lenght=120)
   lastname = models.CharField(max_lenght=120)
   email = models.EmailField()
   password = models.CharField(max_lenght=40)
   created_at = models.DateField()
   updated_at = models.DateField()

   class Meta:
      ordering = ['name']
      verbose_name = 'User'
      verbose_name_plural = 'Users'
   
   def __str__(self):
      return self.name
