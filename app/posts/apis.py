from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination

from posts.permissions import IsOwnerOrReadOnly
from .models import Post, PostImage
from .serializer import PostSerializer, PostImgSerializer


class PostSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects \
        .select_related('author') \
        .prefetch_related('postimage_posts', 'author__wannago_set')
    serializer_class = PostSerializer
    pagination_class = PostSetPagination
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects \
        .select_related('author', 'restaurant') \
        .prefetch_related('postimage_posts')
    serializer_class = PostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )


class PostImageListCreate(generics.ListCreateAPIView):
    queryset = PostImage.objects.all()
    serializer_class = PostImgSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )


class PostImageRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostImage.objects.all()
    serializer_class = PostImgSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )
