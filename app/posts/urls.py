from django.urls import path

from . import apis

app_name = 'posts'

urlpatterns = [
    path('list/', apis.PostList.as_view()),
    path('list/<int:pk>/', apis.PostDetail.as_view()),
]
