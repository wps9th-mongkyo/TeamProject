from rest_framework import serializers

from ..models import Wannago


class WannagoSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    class Meta:
        model = Wannago
        fields = (
            'pk',
            'restaurant',
            'user',
            'created_at'
        )
        read_only_field = (
            'user',
        )
