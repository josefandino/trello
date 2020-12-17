from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import List
from .serializers import ListSerializer
from ..cards.serializers import CardSerializer
from ..cards.models import Card


class ListViewSet(viewsets.ModelViewSet):
    """ Cómo usuario quiero agregar listas a mi tablero para agregar tareas a cada una. """
    queryset = List.objects.all()
    serializer_class = ListSerializer






