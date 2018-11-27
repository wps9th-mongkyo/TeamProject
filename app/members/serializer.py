from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'first_name',
            'last_name',
            'img_profile',
            'phone',
            'email',
            'introduce',
            'following',
            'review_num',
            'checkin_num',
            'followers_num',
            'created_at',
            'modified_at',
        )

