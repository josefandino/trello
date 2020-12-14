from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action

from ..list.models import List
from .models import Card
from .serializers import CardSerializer
from ..list.serializers import ListSerializers

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = ListSerializers

    # @action(methods=['GET'], detail=True)
    # def list(self, request, pk=None):
    #     card = self.get_object()

        # if request.method == 'GET':
        #     serialized = ListSerializers(List.card, many=True)
        #     return Response(status=status.HTTP_200_OK, data=serialized.data)
