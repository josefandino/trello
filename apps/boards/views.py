from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from ..list.models import List
from ..list.serializers import ListSerializer
from ..users.models import User
from .models import Board
from .serializers import BoardSerializer
from ..users.models import User

from ..users.serializers import UserSerializer


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = (AllowAny,)

    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def user(self, request, pk=None):
        board = self.get_object()

        if request.method == 'GET':
            serializer = UserSerializer(board.members, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        if request.method == 'POST':
            user_id = request.data['users_id']
            for user in user_id:
                user = User.objects.get(id=int(user))
                board.members.add(user)
            return Response(status=status.HTTP_200_OK)

        if request.method == 'DELETE':
            user_id = request.data['users_id']
            for user in user_id:
                user = User.objects.get(id=int(user))
                board.members.remove(user)
            return Response(status=status.HTTP_200_OK)

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