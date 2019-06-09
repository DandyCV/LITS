class My_dict(dict):
    def __init__(self, my_dict):
        self.my_dict = my_dict

    def __iadd__(self, new_dict):
        if isinstance(new_dict, dict):
            self.my_dict.update(new_dict)
        return self


dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3}
dict3 = {4 : 5}

m = My_dict(dict1)

print(m.my_dict)
m += dict2
print(m.my_dict)
m += dict3
print(m.my_dict)