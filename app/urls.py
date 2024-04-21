from django.urls import path
from .views import *
urlpatterns = [
    path("",tillu, name="tillu"),
    path("post",post, name="post"),
    path("update/<int:id>",update, name="update"),
]
