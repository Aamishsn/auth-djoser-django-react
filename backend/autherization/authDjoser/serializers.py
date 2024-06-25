from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

UserAccount = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model=UserAccount
        fields=('id', 'email', 'firstName', 'lastName', 'password')