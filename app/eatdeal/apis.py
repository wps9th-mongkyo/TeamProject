from rest_framework import generics

from .models import Eatdeal
from .serializer import EatdealSerializer


class EatdealList(generics.ListCreateAPIView):
    queryset = Eatdeal.objects.all().prefetch_related('eatdealimages')
    serializer_class = EatdealSerializer


class EatdealDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Eatdeal.objects.all().prefetch_related('eatdealimages')
    serializer_class = EatdealSerializer
