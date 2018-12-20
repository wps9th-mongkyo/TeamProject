from django.urls import path

from . import apis

app_name = 'eatdeal'

urlpatterns = [
    path('list/', apis.EatdealList.as_view()),
    path('list/<int:pk>/', apis.EatdealDetail.as_view()),
    path('list/image/', apis.EatdealImageList.as_view()),
    path('list/image/<int:pk>', apis.EatdealImageDetail.as_view()),
]
