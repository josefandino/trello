from django.db import models

class User(models.Model):
   name = models.CharField('Nombres', max_length=120, blank=False, null=False)
    lastname = models.CharField('Apellidos', max_length=120, blank=False, null=False)
   email = models.EmailField('Email', max_length=120, blank=False, null=False, unique=True)
   password = models.CharField(max_lenght=40)
   timestamp = models.DateTimeField('Fecha registro', default=timezone.now)

   class Meta:
      ordering = ['name']
      verbose_name = 'User'
      verbose_name_plural = 'Users'
   
   def __str__(self):
      return '{0},{1}'.format(self.lastname, self.name)
