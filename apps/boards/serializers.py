from rest_framework import serializers
from .models import Board
from apps.list.serializers import ListSerializer

class BoardSerializer(serializers.ModelSerializer):
    list = ListSerializer(read_only=True, many=True)
    class Meta:
        model = Board   
        fields = '__all__'
