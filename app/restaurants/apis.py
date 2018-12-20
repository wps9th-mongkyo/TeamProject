from rest_framework import generics, permissions, filters
from rest_framework.pagination import PageNumberPagination

from restaurants.permissions import IsUser
from .serializers.checkin import CheckInSerializer
from .models import Restaurant, Wannago, CheckIn
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
    def get_queryset(self):
        re_pk=self.kwargs['pk']
        return Wannago.objects.filter(Restaurant__pk=re_pk)
    serializer_class = WannagoSerializer


class CheckInCreate(generics.CreateAPIView):
    queryset = CheckIn.objects.all()
    serializer_class = CheckInSerializer


class CheckInDestroy(generics.DestroyAPIView):
    queryset = CheckIn.objects.all()
    serializer_class = CheckInSerializer


class IosWannagoDestroy(generics.DestroyAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
        IsUser,
    )

    def get_queryset(self):
        self.lookup_field = 'restaurant_pk'
        return super().get_queryset()

    def get_object(self):
        re_pk = self.kwargs['restaurant_pk']
        query = Wannago.objects.get(restaurant__pk=re_pk)
        return query

    serializer_class = WannagoSerializer


class IosCheckInDestroy(generics.DestroyAPIView):
    permission_classes = (
        permissions.IsAuthenticated,
        IsUser,
    )

    def get_queryset(self):
        self.lookup_field = 'checkin_pk'
        return super().get_queryset()

    def get_object(self):
        re_pk = self.kwargs['checkin_pk']
        query = CheckIn.objects.get(restaurant__pk=re_pk)
        return query

    serializer_class = CheckInSerializer
