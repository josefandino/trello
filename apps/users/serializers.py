from rest_framework import serializers
from .models import User

from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100, min_length=4, write_only=True)

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError(
                'The username should only contain alphanumeric characters')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=255, min_length=1, write_only=True)
    username = serializers.CharField(max_length=255, min_length=1, read_only=True)
    tokens = serializers.CharField(max_length=255, min_length=1, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = auth.authenticate(email=email, password=password)
        """ import pdb
        pdb.set_trace() """
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')

        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens
        }
        return super().validate(attrs)
