from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import List
from .serializers import ListSerializers
from ..boards.serializers import BoardSerializer


class ListViewSet(viewsets.ModelViewSet):
<<<<<<< HEAD
    queryset = List.objects.all()
    serializer_class = ListSerializers
=======
   queryset = List.objects.all()
   serializer_class = ListSerializers

   @action(methods=['GET', '´POST', 'DELETE'], detail=True, url_path='list_board')
   def board(self,request, pk=None):
      list = self.get_object()

      if request.method == 'GET':
         serializer = BoardSerializer(list.board)
         return Response(status=status.HTTP_200_OK, data=serializer.data)
>>>>>>> 6fb12cba104aac300e8faf4695f9f1b204599f04
