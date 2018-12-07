from rest_framework import serializers

from members.serializer import UserSerializer
from restaurants.serializers import ResSerializer
from .models import Post, PostImage


class PostImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = (
            'pk',
            'image',
        )


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    restaurant = ResSerializer()
    postimage_posts = PostImgSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = (
            'pk',
            'author',
            'restaurant',
            'rate',
            'content',
            'postimage_posts',
        )
        read_only_fields = (
            'author',
            'restaurant',
            'postimage_posts',
        )
