from django.http import JsonResponse
from .models import dict_
import json


# Create your views here.

def index(request):
    if request.method == 'GET':
        return JsonResponse(dict_, status = 200)
    if request.method == 'POST':
        data = json.loads(str(request.body, 'utf-8'))
        dict_.update(data)
        return JsonResponse(data, status=201)


def named_index(request, name):
    if request.method == 'GET':
        return JsonResponse({name: dict_[name]}, status = 200)
    if request.method == 'PUT':
        data = json.loads(str(request.body, 'utf-8'))
        dict_[name] = data[name]
        return JsonResponse({name: dict_[name]}, status = 201)
    if request.method == 'DELETE':
        value = dict_.pop(name)
        return JsonResponse({name: value}, status = 204)