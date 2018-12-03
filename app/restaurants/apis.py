from rest_framework import generics

from .serializers import ResSerializer
from .models import Restaurant

class ResList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = ResSerializer

    # queryset = Restaurant.objects \
    #     .select_related('menu') \
    #     .prefetch_related('menu__manuimage')


class ResDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = ResSerializer
