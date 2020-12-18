from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.permissions import(
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
)

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
                    code = status.HTTP_201_CREATED
                elif req.method == 'DELETE':
                    board.members.remove(user)
                    code = status.HTTP_204_NO_CONTENT
            serializer = UserSerializer(board.members, many=True)
            return Response(status = code , data = serializer.data)

    
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
            code = status.HTTP_404_NOT_FOUND
            for id in users_id:
                try:
                    user = User.objects.get(id=id)
                    if req.method == 'POST':
                        board.favorite.remove(user)
                        code = status.HTTP_201_CREATED
                    elif req.method == 'DELETE':
                        board.favorite.remove(user)
                        code = status.HTTP_204_NO_CONTENT
                except :
                    continue

            serializer = UserSerializer(board.favorite, many=True)
            return Response(status = code, data = serializer.data)

        # if req.method == 'POST':
        #     users_id = req.data['user_ids']
        #     for ids in users_id:
        #         print(ids)
        #         user = User.objects.get(id=ids)
        #         board.favorite.add(user)
        #     serializer = UserSerializer(board.favorite, many=True)
        #     return Response(status=status.HTTP_200_OK, data=serializer.data)

class BoardListUser(ListAPIView):
    """ Cómo usuario quiero ver la lista de mis tableros y distinguir aquellos seleccionados
    como favoritos. """ 

    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = (IsAuthenticated,)    
    
    def get_queryset(self):    
        """ captura el id del user logeado y se pasa como parametro a la consulta de Board"""   
        # query = {}
        # query['subscribers__id'] = self.request.user.id        
        # self.queryset = self.queryset.filter(**query)
        # return super().get_queryset()
        
        my_subscritions = Board.objects.filter(owner=self.request.user.id)
        return my_subscritions