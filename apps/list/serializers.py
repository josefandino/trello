from rest_framework import serializers
from .models import List
from apps.cards.serializers import CardSerializer


class ListSerializer(serializers.ModelSerializer):
    card = CardSerializer(read_only=True, many=True)

    class Meta:
        model = List
        fields = '__all__'
