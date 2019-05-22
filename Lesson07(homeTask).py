from collections import Counter
def w_dict(new_string):
    new_string = new_string.lower()
    _list = ''.join(i for i in new_string if i.isalpha() or i == ' ')
    _list = _list.split(' ')
    _list = [value for value in _list if value]
    _dict = dict(Counter(_list))
    return _dict


print(w_dict('Hello! My Name - Joe!!! And his name - joe too. Say "hello" to Joe'))