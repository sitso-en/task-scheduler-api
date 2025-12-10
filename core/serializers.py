from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = [
            'id','username', 'email', 'first_name', 'last_name', 'password'
        ]

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer):
        model = User
        fields = [
            'id', 'username','email', 'first_name', 'last_name'
        ]