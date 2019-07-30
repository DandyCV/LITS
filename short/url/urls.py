from django.urls import path

from .views import UrlListCreateAPIView, redirect

urlpatterns = [
    path('url', UrlListCreateAPIView.as_view()),
    path('<short_url>', redirect)
]