from rest_framework import generics, permissions

from .models import Eatdeal
from .serializer import EatdealSerializer, EatdealImageSerializer


class EatdealList(generics.ListCreateAPIView):
    queryset = Eatdeal.objects.all().prefetch_related('eatdealimages')
    serializer_class = EatdealSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )


class EatdealDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Eatdeal.objects.all().prefetch_related('eatdealimages')
    serializer_class = EatdealSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )


class EatdealImageList(generics.ListCreateAPIView):
    queryset = Eatdeal.objects.all().prefetch_related('eatdealimages')
    serializer_class = EatdealImageSerializer


class EatdealImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Eatdeal.objects.all().prefetch_related('eatdealimages')
    serializer_class = EatdealImageSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
