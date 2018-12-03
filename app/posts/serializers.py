from rest_framework import serializers

from members.serializer import UserSerializer
from restaurants.serializers import ResSerializer
from .models import Post, PostImage


class PostImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = (
            'pk',
            'post',
            'image',
        )


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    restaurant = ResSerializer()
    postimage = PostImgSerializer(many=True)

    class Meta:
        model = Post
        fields = (
            'pk',
            'author',
            'restaurant',
            'rate',
            'postimage',
            'context',
        )
        read_only_fields = (
            'author',
            'restaurant',
        )
