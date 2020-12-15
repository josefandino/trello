from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Comment
from .serializers import CommentSerializer
from ..users.serializers import UserSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @action(methods=['GET'], detail=True, url_path='comentariodeusuario')
    def user(self, request, pk=None):
        comment = self.get_object()
        if request.method == 'GET':
            serializer = UserSerializer(comment.user)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
