from django.urls import path
from .views import index, named_index

#якшо приходить запит на пустий URL запускається index
urlpatterns = [
    path('', index),
    path('<name>', named_index)
]