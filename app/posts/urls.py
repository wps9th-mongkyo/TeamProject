from django.urls import path

from . import apis

app_name = 'posts'

urlpatterns = [
    path('', apis.PostList.as_view()),
    path('<int:pk>/', apis.PostDetail.as_view()),
]
