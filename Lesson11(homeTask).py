class My_dict(dict):
    def __init__(self, my_dict):
        self.my_dict = my_dict

    # my_dict += {a : a}  += повинно додавати пару ключ : значення у словник
    def __add__(self, new_dict):
        if type(new_dict) is dict:
            My_dict(self.my_dict.update(new_dict))
        return self


dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3}
dict3 = [1,2]
m = My_dict(dict1)

print(m.my_dict)
m += dict2
print(m.my_dict)