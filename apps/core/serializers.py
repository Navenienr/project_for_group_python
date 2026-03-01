"""
Сериализаторы базового модуля.
"""
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    # Сериализатор регистрации новых пользователей
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, attrs):
        # валидация паролей и email
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': 'Пароли не совпадают'})
        
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({'email': 'Пользователь с таким email уже существует'})

        return attrs
    
    def create(self, validated_data):
        # создание пользователя в базе данных, вызывается при serializer.save()
        validated_data.pop('password2')

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        return user
    

class UserProfileSerializer(serializers.ModelSerializer):
    # Сериализатор профиля пользователя (для фронтенда)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'tg_username', 'date_joined', 'is_moderator')
        read_only_fields = ['id', 'date_joined', 'is_moderator']        