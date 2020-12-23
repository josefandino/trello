from rest_framework import serializers
from .models import Card
from apps.comments.serializers import CommentSerializer


class CardSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Card
        fields = '__all__'
