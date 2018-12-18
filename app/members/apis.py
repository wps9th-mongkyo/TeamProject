from django.contrib.auth import get_user_model, authenticate
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import NotAuthenticated, AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from members.models import User
from .backends import FacebookBackend
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
                'user': user
            }
            return Response(data)
        raise AuthenticationFailed()

        # serializer = AuthTokenSerializer(data=request.data)
        # if serializer.is_valid():
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FacebookAuthTokenView(APIView):

    def post(self, request):
        facebook_user_id = request.data.get('facebook_user_id')
        access_token = request.data.get('access_token')
        if User.objects.filter(username=facebook_user_id).exists():
            user = User.objects.get(username=facebook_user_id)
        else:
            user = FacebookBackend.get_user_by_access_token(access_token)
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


# class FacebookAuthTokenView(APIView):
#     def post(self, request):
#         # 전달받은 토큰(페이스북  access token) 값 유저 정보(token, user)를 사용해서
#         # 정상적인 token인지 검사 후
#         # DB에 해당 유저가 존재하는지 검사(authenticate)
#         # 있다면 -> 토큰발급
#         # 없다면 -> 유저 생성 후 토큰 발급과
#
#         pass


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
