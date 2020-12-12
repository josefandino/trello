from rest_framework import serializers

from .models import Comments

class CommentSerializers(serializers.ModelSerializer):

   class Meta:
      model = Comment
      fields = '__all__'
      