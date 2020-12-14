from rest_framework import serializers

from .models import List

class ListSerializers(serializers.ModelSerializer):

   class Meta:
      model = List
      fields = '__all__'
      