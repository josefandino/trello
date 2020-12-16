from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import List
from .serializers import ListSerializer
from ..boards.serializers import BoardSerializer


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer

    @action(methods=['GET', '´POST', 'DELETE'], detail=True, url_path='list_board')
    def card(self, request, pk=None):
        list = self.get_object()

        if request.method == 'GET':
            serializer = ListSerializer(list.card)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        # if request.method == ''