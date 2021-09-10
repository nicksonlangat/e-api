from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.models import BaseUserManager
from rest_framework.authtoken.models import Token
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','first_name','last_name')

class UserRegisterSerializer(serializers.ModelSerializer):
    """
    A user serializer for registering the user
    """
    class Meta:
        model = User
        fields = ('email','email','first_name','last_name','password')

    def validate_email(self, email):
        user = User.objects.filter(email=email)
        if user:
            raise serializers.ValidationError("Email is already taken")
        return BaseUserManager.normalize_email(email)

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)

class AuthUserSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()
    class Meta:
         model = User
         fields = ('id','email','first_name','last_name', 'auth_token')
         read_only_fields = ('id',)
    
    def get_auth_token(self, obj):
        token = Token.objects.filter(user=obj)
        token.delete()
        token = Token.objects.create(user=obj)
        return token.key

class EmptySerializer(serializers.Serializer):
    pass