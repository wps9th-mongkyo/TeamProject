from rest_framework import generics, permissions, filters
from rest_framework.pagination import PageNumberPagination

from restaurants.permissions import IsUser
from .models import Restaurant, Wannago
from .serializers import ResSerializer, WannagoSerializer


class ResSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ResList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.prefetch_related('menuimage_res',
                                                    'post_set',
                                                    'post_set__postimage_posts',
                                                    'post_set__author',
                                                   'post_set__author__wannago_set')
    serializer_class = ResSerializer
    pagination_class = ResSetPagination
    filter_backends = (filters.OrderingFilter, filters.SearchFilter,)
    ordering_fields = '__all__'
    search_fields = (
        'name', 'address', 'food_type', 'phone_num', 'price_level', 'parking', 'Business_hour', 'break_time', 'last_order', 'holiday',
    )
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )


class ResDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all().prefetch_related('menuimage_res', 'post_set')
    serializer_class = ResSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )


class WannagoCreate(generics.CreateAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )
    queryset = Wannago.objects.all()
    serializer_class = WannagoSerializer


class WannagoDestroy(generics.DestroyAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
        IsUser,
    )
    queryset = Wannago.objects.all()
    serializer_class = WannagoSerializer

