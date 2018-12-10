from rest_framework import serializers

from members.serializer import UserSerializer
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
    postimage_posts = PostImgSerializer(many=True)

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
