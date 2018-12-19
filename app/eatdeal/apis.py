from rest_framework import generics, permissions

from .models import Eatdeal
from .serializer import EatdealSerializer


class EatdealList(generics.ListCreateAPIView):
    queryset = Eatdeal.objects.all().prefetch_related('eatdealimages')
    serializer_class = EatdealSerializer
    # permission_classes = (
    #     permissions.IsAuthenticatedOrReadOnly
    # )


class EatdealDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Eatdeal.objects.all().prefetch_related('eatdealimages')
    serializer_class = EatdealSerializer
    # permission_classes = (
    #     permissions.IsAuthenticatedOrReadOnly
    # )
