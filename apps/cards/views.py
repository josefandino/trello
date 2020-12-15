from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.serializers import ListSerializer


from .models import Card
from .serializers import CardSerializer
from ..list.models import List


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = ListSerializer


