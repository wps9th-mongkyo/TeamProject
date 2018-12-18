from django.urls import path

from . import apis

app_name = 'eatdeal'

urlpatterns = [
    path('list/', apis.EatdealList.as_view()),
    path('list/<int:pk>/', apis.EatdealDetail.as_view()),
]
