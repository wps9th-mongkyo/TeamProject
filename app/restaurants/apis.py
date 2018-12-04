from rest_framework import generics

from .serializers import ResSerializer
from .models import Restaurant


class ResList(generics.ListCreateAPIView):
    queryset = Restaurant.objects \
        .prefetch_related('manuimage')
    serializer_class = ResSerializer


class ResDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects \
        .prefetch_related('menu__manuimage')
    serializer_class = ResSerializer
