from django.contrib.auth import get_user_model, authenticate
from rest_framework import permissions, generics
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import NotAuthenticated, AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import UserSerializer

User = get_user_model()


class AuthTokenView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, __ = Token.objects.get_or_create(user=user)
            data = {
                'token': token.key,
                'user': UserSerializer(user).data,
            }
            return Response(data)
        raise AuthenticationFailed()


class FacebookAuthTokenView(APIView):

    def post(self, request):
        facebook_user_id = request.data.get('facebook_user_id')
        access_token = request.data.get('access_token')
        user = authenticate(access_token)
        token = Token.objects.get_or_create(user=user)[0]
        data = {
            'token': token.key,
            'user': UserSerializer(user).data,
        }
        return Response(data)


class ProfileView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        return Response(UserSerializer(request.user).data)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        if lookup_url_kwarg not in self.kwargs:
            if not self.request.user.is_authenticated:
                raise NotAuthenticated()
            return self.request.user

        user = super().get_object()
        return user
