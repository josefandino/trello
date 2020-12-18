from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

# from ..cards.serializers import CardSerializer
# from .utils import Util
#
from .models import Card
from .serializers import CardSerializer
from ..comments.models import Comment
from ..comments.serializers import CommentSerializer
from ..list.models import List
from ..users.models import User
from ..users.serializers import UserSerializer


class CardViewSet(viewsets.ModelViewSet):
    """ Cómo usuario despues de agregar listas a mi tablero pueda agregar tareas a cada una."""
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    
    @action(methods=['GET', 'POST', 'DELETE'], detail=True, url_path='userincard')
    def user(self, request, pk=None):
        """ Cómo usuario quiero agregar tarjetas a cada lista para poder asignar responsables de
        cada una, para que les lleguen un correo de bienvenida."""
        card = self.get_object()

        if request.method == 'GET':
            serializer = UserSerializer(card.members, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

        if request.method == 'POST':

            user_id = request.data['users_id']
            for user in user_id:
                user = User.objects.get(id=int(user))
                card.members.add(user)
                # send correo
                email_body = 'Hola '+user.name+' as sido invitado a la tarjeta '+card.name
                data = {'email_body': email_body,
                        'to_email': user.email,
                        'email_subject': 'Verify your email'}
                Util.send_email(data)
            return Response(status=status.HTTP_200_OK)

        if request.method == 'DELETE':
            user_id = request.data['users_id']
            for user in user_id:
                user = User.objects.get(id=int(user))
                card.members.remove(user)
            return Response(status=status.HTTP_200_OK)