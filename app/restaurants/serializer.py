from rest_framework import serializers

from posts.serializer import PostImgSerializer
from .models import Restaurant, MenuImage


class MenuImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuImage
        fields = (
            'pk',
            'image',
        )


class ResSerializer(serializers.ModelSerializer):
    menuimage_res = MenuImageSerializer(many=True, read_only=True)
    postimage_posts = PostImgSerializer(many=True, read_only=True)
    class Meta:
        model = Restaurant
        fields = (
            'pk',
            'name',
            'address',
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
            'menu_text',
            'menuimage_res',
            'rate_average'
            'postimage_posts',

        )
        read_only_fields = (
            'menuimage_res',
            'postimage_posts',
        )


