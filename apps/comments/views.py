from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Comment
from .serializers import CommentSerializer
from ..cards.serializers import CardSerializer
from ..users.serializers import UserSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (AllowAny,)

    @action(methods=['GET'], detail=True, url_path='comentariodeusuario')
    def user(self, request, pk=None):
        comment = self.get_object()
        if request.method == 'GET':
            serializer = UserSerializer(comment.members)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(methods=['GET'], detail=True)
    def card(self, request, pk=None):
        comment = self.get_object()
        serializer = CardSerializer(comment.card)
        return Response(status=status.HTTP_200_OK, data=serializer.data)