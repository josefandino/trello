from rest_framework import serializers
from .models import Board
<<<<<<< HEAD
=======


class BoardSerializer(serializers.ModelSerializer):
>>>>>>> 6fb12cba104aac300e8faf4695f9f1b204599f04


class BoardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'
