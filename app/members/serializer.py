from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed

from restaurants.serializers.checkin import CheckInSerializer
from .models import User
from restaurants.serializers.wannago import WannagoSerializer


class UserSerializer(serializers.ModelSerializer):

    wannago_set = WannagoSerializer(many=True, read_only=True)
    checkin_set = CheckInSerializer(many=True, read_only=True)

    class Meta:
        model = User

        fields = (
            'pk',
            'username',
            'full_name',
            'img_profile',
            'phone',
            'email',
            'introduce',
            'wannago_set',
            'checkin_set',
        )


class AuthTokenSerializerr(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None

    def validate(self, data):
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed('아이디 또는 비밀번호가 올바르지 않습니다.')
        self.user = user
        return data

    def to_representation(self, instance):
        token = Token.objects.get_or_create(user=self.user)[0]
        data = {
            'user': UserSerializer(self.user).data,
            'token': token.key,
        }
        return data
