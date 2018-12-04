from rest_framework import serializers

from .models import Restaurant, Menu, MenuImage


class MenuImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuImage
        fields = (
            'post'
            'image'
        )


class MenuSerializer(serializers.ModelSerializer):
    menuimage = MenuImageSerializer
    class Meta:
        model = Menu
        fields = (
            'name'
            'menu_text'
            'menuimage'
        )
        read_only_fields = (
            'menuimage'
        )


class ResSerializer(serializers.ModelSerializer):
    menu = MenuSerializer
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
            'youtube',
            'view_num',
            'review_num',
            'want_num',
            'created_at',
            'modified_at',
            'latitude',
            'longitude',
        )

