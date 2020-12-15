from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import action

from .models import User
from .serializers import UserSerializer
from ..boards.serializers import BoardSerializer
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def boards(self, request, pk=None):
        user = self.get_object()
        if request.method == 'GET':
            serializer = BoardSerializer(user.board, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
