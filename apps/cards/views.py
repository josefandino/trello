from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from ..cards.serializers import CardSerializer


from .models import Card
from .serializers import CardSerializer
from ..list.models import List


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def card(self, request, pk=None):
        list = self.get_object()

        if request.method == 'GET':
            serializer = CardSerializer(list.card)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        #if request.method == 'POST':

