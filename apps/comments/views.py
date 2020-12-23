from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Comment
from .serializers import CommentSerializer
from ..users.serializers import UserSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """Cómo usuario quiero agregar comentarios en cada tarea para poder comunicarme con
    los miembros o responsables. """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
