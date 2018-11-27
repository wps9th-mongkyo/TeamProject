from django.urls import path

from . import apis

urlpatterns = [
    path('list/', apis.UserList.as_view()),
    path('list/<int:pk>', apis.UserDetail.as_view()),
]
