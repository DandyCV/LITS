from django.urls import path
from .views import *

#якшо приходить запит на пустий URL запускається index
urlpatterns = [
    path('', index),
    path('<name>', named_index)
]