from django.urls import path

from . import apis

app_name = 'restaurants'

urlpatterns = [
    path('list/', apis.ResList.as_view()),
    path('list/<int:pk>/', apis.ResDetail.as_view()),
    path('list/wannago/', apis.WannagoCreate.as_view()),
    path('list/wannago/<int:pk>/', apis.WannagoDestroy.as_view()),
    path('list/checkin/', apis.CheckInCreate.as_view()),
    path('list/checkin/<int:pk>/', apis.CheckInDestroy.as_view()),
]
