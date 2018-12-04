from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .models import Restaurant
from .serializers import ResSerializer


class ResList(generics.ListCreateAPIView):
    queryset = Restaurant.objects \
        .prefetch_related('manuimage')
    serializer_class = ResSerializer


class ResSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ResList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all().prefetch_related('menuimage_res')
    serializer_class = ResSerializer
    pagination_class = ResSetPagination


class ResDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = ResSerializer
