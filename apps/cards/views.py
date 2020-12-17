from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from ..cards.serializers import CardSerializer


from .models import Card
from .serializers import CardSerializer
from ..comments.models import Comment
from ..comments.serializers import CommentSerializer
from ..list.models import List
from ..users.models import User
from ..users.serializers import UserSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    @action(methods=['GET', 'POST', 'DELETE'], detail=True, url_path='userincard')
    def user(self, request, pk=None):
        card = self.get_object()

        if request.method == 'GET':
            serializer = UserSerializer(card.members, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        if request.method == 'POST':
            user_id = request.data['users_id']
            for user in user_id:
                user = User.objects.get(id=int(user))
                card.members.add(user)
            return Response(status=status.HTTP_200_OK)

        if request.method == 'DELETE':
            user_id = request.data['users_id']
            for user in user_id:
                user = User.objects.get(id=int(user))
                card.members.remove(user)
            return Response(status=status.HTTP_200_OK)

    @action(methods=['GET', 'POST', 'DELETE'], detail=True, url_path='commentincard')
    def comment(self, request, pk=None):
        card = self.get_object()

        if request.method == 'GET':
            serializer = CommentSerializer(card.comments, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        if request.method == 'POST':
            comment_id = request.data['comments_id']
            for comm in comment_id:
                comment = Comment.objects.get(id=int(comm))
                card.comments.add(comment)
            return Response(status=status.HTTP_200_OK)

        if request.method == 'DELETE':
            comment_id = request.data['comments_id']
            for comm in comment_id:
                comment = Comment.objects.get(id=int(comm))
                card.comments.remove(comment)
            return Response(status=status.HTTP_200_OK)

