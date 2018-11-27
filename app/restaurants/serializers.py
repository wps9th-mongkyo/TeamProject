from rest_framework import serializers

from .models import Restaurant


class ResSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = (
            'pk',
            'name',
            'address',
            'address_detail',
            'phone_num',
            'food_type',
            'price_level',
            'parking',
            'Business_hour',
            'break_time',
            'last_order',
            'holiday',
            'website',
            'view_num',
            'review_num',
            'want_num',
            'created_at',
            'modified_at',
        )