from rest_framework import serializers
from ..models import MenuImage, Restaurant
from posts.serializer import PostSerializer


class MenuImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuImage
        fields = (
            'pk',
            'image',
        )


class ResSerializer(serializers.ModelSerializer):
    menuimage_res = MenuImageSerializer(many=True, read_only=True)
    post_set = PostSerializer(many=True, read_only=True)
    rate_good = serializers.SerializerMethodField()
    rate_normal = serializers.SerializerMethodField()
    rate_bad = serializers.SerializerMethodField()


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
            'rate_average',
            'rate_good',
            'rate_normal',
            'rate_bad',
            'menu_text',
            'menuimage_res',
            'post_set',
        )
        read_only_fields = (
            'menuimage_res',
            'post_set',
        )
    # def get_is_like(self, obj):
    #     user = self.content['request'].user
    #     return obj.wannago_set.filter(user=user)

    def get_rate_good(self, obj):
        return obj.post_set.filter(rate=5).count()

    def get_rate_normal(self, obj):
        return obj.post_set.filter(rate=3).count()

    def get_rate_bad(self, obj):
        return obj.post_set.filter(rate=1).count()

