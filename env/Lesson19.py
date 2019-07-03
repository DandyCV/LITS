try:
    import ujson
except ImportError:
    import json as ujson

import bottle
from bottle import request, response
from bottle import get, post, route

@get('/')
def index():
    return 'Hello'

@post('/')
def post_index():
    data = request.data
    return data

@route('/')
def route_index():
    return 'index page'

@route('/', method='post')
def return_data():
    return request.json()

@route('/<name:>')
def get_name(name):
    return 'Hello ' + name

@route('/')
def get_name():
    response.headers['Content-Type'] = 'applicatiob/json'
    # response.json({'text1':'json'})
    return ujson.dumps({'from_server':'hello'})

bottle.run(port=8080)


dict = {}

# GET ('/')            повертає весь словник (масив{}) {'key1':'value1'}, {'key2':'value2'}
# GET ('/<key>')       повертає значення по ключу(в формат json) {'key':'value'}
# POST ('/')           {'key':'value'} - для апдейту словника
# PUT ('/<key>')      стрінгою передає значення ключа для апдейту 'new_value'
# DELETE ('/<key>')   {'key':'value'} - до видалення з словнику
