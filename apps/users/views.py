from django.shortcuts import render

from rest_framework import viewsets, status, generics
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import UserSerializer
# from .serializers import UserSerializer, RegisterSerializer, EmailVerificationSerializer, LoginSerializer
from ..boards.serializers import BoardSerializer
# from rest_framework.response import Response
from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import RefreshToken


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)



    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def boards(self, request, pk=None):
        user = self.get_object()
        if request.method == 'GET':
            serializer = BoardSerializer(user.board, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)

# class RegisterView(generics.GenericAPIView):
#
#      serializer_class = RegisterSerializer
#
#      def post(self,request):
#
#          user = request.data
#          serializer = self.serializer_class(data = user)
#          serializer.is_valid(raise_exception=True)
#          serializer.save()
#          user_data = serializer.data
#
#          return Response({"message": "checked email",**user_data},status=status.HTTP_201_CREATED)

# class LoginAPIView(generics.GenericAPIView):
#      serializer_class = LoginSerializer
#
#      def post(self, request):
#          serializer = self.serializer_class(data=request.data)
#          serializer.is_valid(raise_exception=True)
#          return Response(serializer.data, status=status.HTTP_200_OK)