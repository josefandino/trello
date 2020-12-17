from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import List
from .serializers import ListSerializer
from ..cards.serializers import CardSerializer
from ..cards.models import Card


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer

    @action(methods=(['GET', 'POST', 'DELETE']), detail=True)
    def card(self,request, pk=None):
        list = self.get_object()

        if request.method == 'GET':
            cards = Card.objects.filter(list=list)
            serialized = CardSerializer(cards, many=True)
            return Response(
                status=status.HTTP_200_OK,
                data=serialized.data
            )
        if request.method == 'DELETE':
            card_id = request.data['card_id']
            for card in card_id:
                card = Card.objects.get(id=int(card))
                card.delete()

            return Response(status=status.HTTP_200_OK)





