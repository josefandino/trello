from django.shortcuts import render

from rest_framework import viewsets

from .models import Board
from .serializers import BoardSerializers

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializers
