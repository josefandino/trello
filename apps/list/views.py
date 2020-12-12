from django.shortcuts import render

from rest_framework import viewsets

from .models import List
from .serializers import ListSerializers

class ListViewSet(viewsets.ModelViewSet):
   queryset = List.objects.all()
   serializer_class = ListSerializers
