from rest_framework import serializers
from .models import Board


class BoardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'
