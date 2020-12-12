from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.serializers import ListSerializer

from .models import Card
from .serializers import CardSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    @action(methods=['GET'], detail=True)
    def list_add(self, request, pk='None'):
        card = self.get_object()
        if request.mehotd == 'GET':
            serializer = ListSerializer(card.list)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
