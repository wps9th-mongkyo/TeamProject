from django.urls import path

from . import apis

urlpatterns = [
    path('list/', apis.ResList.as_view()),
    path('list/<int:pk>', apis.ResDetail.as_view()),
]