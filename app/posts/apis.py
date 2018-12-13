from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .models import Post
from .serializer import PostSerializer


class PostSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects \
        .select_related('author', 'restaurant') \
        .prefetch_related('postimage_posts')
    serializer_class = PostSerializer
    pagination_class = PostSetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects \
        .select_related('author', 'restaurant') \
        .prefetch_related('postimage_posts')
    serializer_class = PostSerializer
