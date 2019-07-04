from django.http import HttpResponse, JsonResponse
from .models import dict_

def index(request):

    html = '<html><body>TEXT!!!</body></html>'

    return HttpResponse (html, status = 200)


def named_index(request, name):


    html = f'<html><body>HELLO {name}</body></html>'

    return HttpResponse(html, status=200)

    return JsonResponse(html, status=200)
# Create your views here.
