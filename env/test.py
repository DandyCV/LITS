import json as ujson

dict = {
    'Monday': 'Kyiv',
    'Tuesday': 'Lviv',
    'Wednesday': 'Odessa',
    'Thursday': 'Kharkiv',
    'Friday': 'Chernivtsi'
        }

data_dict = {'Saturday': 'Rivne', 'Sunday': 'Ternopil'}
name = 'Monday'

data = ujson.dumps(dict[name])

dict.update(data_dict)
print(ujson.dumps(dict))

print(data)