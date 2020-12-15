from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action

from ..list.models import List
from .models import Card
from .serializers import CardSerializer
from ..list.serializers import ListSerializer
from ..list.models import List


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = ListSerializer

    # @action(methods=['GET'], detail=True)
    # def list(self, request, pk=None):
    #     card = self.get_object()

        # if request.method == 'GET':
        #     serialized = ListSerializers(List.card, many=True)
        #     return Response(status=status.HTTP_200_OK, data=serialized.data)
    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def list_add(self, request, pk='None'):
        card = self.get_object()

        if request.method == 'GET':
            serializer = ListSerializer(card.list)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        if request.method == 'POST':
            list_id = request.data['list_id']
            for lists in list_id:
                list = List.objects.get(id=int(lists))
                card.list.add(list)
            return Response(status=status.HTTP_200_OK)

        if request.method == 'DELETE':
            list_id = request.data['list_id']
            for lists in list_id:
                list = List.objects.get(id=int(lists))
                card.list.remove(list)
            return Response(status=status.HTTP_200_OK)
