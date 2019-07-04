import bottle
from bottle import request, response
from bottle import get, post, route, put, delete

dict_ = {
    "Monday": "Kyiv",
    "Tuesday": "Lviv",
    "Wednesday": "Odessa",
    "Thursday": "Kharkiv",
    "Friday": "Chernivtsi"
        }


@get('/')
def get_dict():
    return dict_


@route('/<key:>')
def get_dict_name(key):
    return {key: dict_[key]}


@post('/')
def update_dict():
    #new_dict = {'Saturday': request.json.get('Saturday'), 'Sunday': request.json.get('Sunday')}
    dict.update(request.json)
    response.status = 201
    return request.json


@put('/<key>')
def update_key(key):
    value = request.json.get(key)
    dict[key] = value
    response.status = 201
    return {key: dict_[key]}


@delete('/<key>')
def remove_key(key):
    value = dict_.pop(key)
    response.status = 204
    return value


bottle.run(port=8080)

dict_2 = {"Saturday": "Kharkiv", "Sunday": "Ternopil"}

dict_3 = {"Monday": "Kherson"}


#
# GET ('/')            повертає весь словник (масив{}) {'key1':'value1'}, {'key2':'value2'}
# GET ('/<key>')       повертає значення по ключу(в формат json) {'key':'value'}
# POST ('/')           {'key':'value'} - для апдейту словника
# PUT ('/<key>')      стрінгою передає значення ключа для апдейту 'new_value'
# DELETE ('/<key>')   {'key':'value'} - до видалення з словнику
