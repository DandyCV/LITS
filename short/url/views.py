from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from rest_framework.generics import ListCreateAPIView
from short_url import decode_url

from .models import Url
from .serializers import UrlSerializer

from rest_framework import permissions


class UrlListCreateAPIView(ListCreateAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


def redirect(request, short_url):
    url_id = decode_url(short_url)
    url = get_object_or_404(Url, id=url_id)

    return HttpResponseRedirect(url.url)
