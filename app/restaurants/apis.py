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
    queryset = Restaurant.objects.all().prefetch_related('menuimage_res', 'post_set')
    serializer_class = ResSerializer
    pagination_class = ResSetPagination
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'


class ResDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all().prefetch_related('menuimage_res', 'post_set')
    serializer_class = ResSerializer


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

