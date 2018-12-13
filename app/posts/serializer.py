from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

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
    author = UserSerializer(read_only=True)
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