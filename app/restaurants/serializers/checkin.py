from rest_framework import serializers

from ..models import CheckIn


class CheckInSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = CheckIn
        fields = (
            'pk',
            'restaurant',
            'user',
            'created_at'
        )
        read_only_field = (
            'user',
        )
