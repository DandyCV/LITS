from django.contrib import admin
from django.urls import path

from .api.v0.view import ArticleListCreateAPIView, ArticleRetriveAPIView, ArticleRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('articles/', ArticleListCreateAPIView.as_view()),
    path('articles/<int:pk>', ArticleRetrieveUpdateDestroyAPIView.as_view())
    ]