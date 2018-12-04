from rest_framework import generics

from .serializers import PostSerializer
from .models import Post


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects \
        .select_related('author', 'restaurant') \
        .prefetch_related('postimage_posts')
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects \
        .select_related('author', 'restaurant') \
        .prefetch_related('postimage_posts')
    serializer_class = PostSerializer
