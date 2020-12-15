from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from ..users.models import User
from .models import Board
from .serializers import BoardSerializer
from ..users.models import User

from ..users.serializers import UserSerializer


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    @action(methods=['GET', 'POST', 'DELETE'], detail=True, url_path='user_table')
    def user(self, request, pk=None):
        board = self.get_object()

        if request.method == 'GET':
            serializer = UserSerializer(board.members, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        if request.method == 'POST':
            user_id = request.data['users_id']
            for user in user_id:
<<<<<<< HEAD
                User.objects.get(id=int(user))
                board.suer.add(board)
=======
                user = User.objects.get(id=int(user))
                board.members.add(user)
>>>>>>> 6fb12cba104aac300e8faf4695f9f1b204599f04
            return Response(status=status.HTTP_200_OK)

        if request.method == 'DELETE':
            user_id = request.data['users_id']
            for user in user_id:
<<<<<<< HEAD
                User.objects.get(id=int(user))
                board.user.remove(board)
=======
                user = User.objects.get(id=int(user))
                board.members.remove(user)
>>>>>>> 6fb12cba104aac300e8faf4695f9f1b204599f04
            return Response(status=status.HTTP_200_OK)


