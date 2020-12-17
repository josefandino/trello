from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from ..list.models import List
from ..list.serializers import ListSerializer
from ..users.models import User
from .models import Board
from .serializers import BoardSerializer
from ..users.models import User

from ..users.serializers import UserSerializer


class BoardViewSet(viewsets.ModelViewSet):
    """ Cómo usuario quiero crear un tablero desde la página principal para gestionar un
    proyecto """ 
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    @action(methods=['GET','POST','DELETE'], detail=True)
    def invite(self, req, pk=None):   
        """ Como usuario quiero invitar a otros usuarios (registrados y no registrados) como
        miembros del tablero para que puedan acceder a ese proyecto.        
        queda pendiente :
        Pero no pueden editar los detalles del mismo, únicamente agregar elementos."""
        board = self.get_object()
        
        if req.method == 'GET':
            serializer = UserSerializer(board.members, many=True)
            return Response(status = status.HTTP_200_OK, data = serializer.data)
        
        if req.method in ['POST','DELETE']:
            users_id = req.data['users']
            for id in users_id:
                user = User.objects.get(id=id)
                if req.method == 'POST':
                    board.members.add(user)                    
                    serializer = UserSerializer(board.members, many=True)
                    return Response(status = status.HTTP_201_CREATED, data = serializer.data)
                elif req.method == 'DELETE':
                    board.members.remove(user)
                    serializer = UserSerializer(board.members, many=True)
                    return Response(status = status.HTTP_204_NO_CONTENT, data = serializer.data)

    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def lis(self, request, pk=None):
        boar = self.get_object()

        # if request.method == 'GET':
        #     serializer = ListSerializer(board.list)
        #     return Response(status=status.HTTP_200_OK, data=serializer.data)
        if request.method == 'GET':
            board = Board.objects.filter(id=boar.id)
            serialized = BoardSerializer(board, many=True)
            return Response(
                status=status.HTTP_200_OK,
                data=serialized.data
            )

        if request.method == 'POST':
            list_id = request.data['list_id']
            for list in list_id:
                list = List.objects.get(id=int(list))
                list.create()
            return Response(status=status.HTTP_200_OK)

        if request.method == 'DELETE':
            list_id = request.data['list_id']
            for list in list_id:
                list= List.objects.get(id=int(list))
                list.delete()

            return Response(status=status.HTTP_200_OK)

    @action(methods=['GET','POST','DELETE'], detail=True)
    def favorite(self, req, pk=None):   
        """ Cómo usuario quiero ver la lista de mis tableros y distinguir aquellos seleccionados
        como favoritos. """
        board = self.get_object()
        
        if req.method == 'GET':
            serializer = UserSerializer(board.favorite, many=True)
            return Response(status = status.HTTP_200_OK, data = serializer.data)
        
        if req.method in ['POST','DELETE']:
            users_id = req.data['users']
            for id in users_id:
                user = User.objects.get(id=id)
                if req.method == 'POST':
                    board.favorite.add(user)                    
                    serializer = UserSerializer(board.favorite, many=True)
                    return Response(status = status.HTTP_201_CREATED, data = serializer.data)
                elif req.method == 'DELETE':
                    board.favorite.remove(user)
                    serializer = UserSerializer(board.favorite, many=True)
                    return Response(status = status.HTTP_204_NO_CONTENT, data = serializer.data)

class BoardListUser(ListAPIView):
    """ Cómo usuario quiero ver la lista de mis tableros y distinguir aquellos seleccionados
    como favoritos. """ 

    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    #permission_classes = (IsAuthenticated,)    
    
    def get_queryset(self):       
        # query = {}
        # query['subscribers__id'] = self.request.user.id        
        # self.queryset = self.queryset.filter(**query)
        # return super().get_queryset()
        
        my_subscritions = Newsletter.objects.filter(subscribers=self.request.user.id)
        return my_subscritions