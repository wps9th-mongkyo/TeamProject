from rest_framework import serializers


from .models import User
from restaurants.serializers.wannago import WannagoSerializer


class UserSerializer(serializers.ModelSerializer):
    wannago_set = WannagoSerializer(many=True, read_only=True)

    class Meta:
        model = User

        fields = (
            'pk',
            'username',
            'img_profile',
            'phone',
            'email',
            'introduce',
            'wannago_set',
        )
