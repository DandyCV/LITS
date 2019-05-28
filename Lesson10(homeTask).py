class Stack:
    """Стек глибино 5 елементів"""
    def __init__(self, stack = []):
        self.stack = stack

    def push(self, new_element):
        if len(self.stack) < 5:
            print('Додаю в стек елемент ', new_element)
            self.stack.append(new_element)
            return self.stack
        else:
            print('Стек переповнений, елемент ', new_element, ' не додано.')
            return self.stack

    @property
    def pop(self):
        if self.stack:
            print('Видаляю зі стеку елемент ', self.stack.pop())
            return self.stack
        else:
            return 'В стеку не залишилось елементів.'

    @property
    def length(self):
        return 'Глибина стеку = ' + str(len(self.stack))

    @property
    def is_empty(self):
        if self.stack:
            return 'В стеку є елементи'
        else:
            return 'Стек порожній'

s = Stack([8, 'b'])
print(s.push(2))
print(s.push('a'))
print(s.push(7))
print(s.push('j'))
print(s.push('11'))
print(s.push('k'))
print(s.pop)
print(s.length)
print(s.is_empty)
print(s.pop)
print(s.pop)
print(s.pop)
print(s.pop)
print(s.pop)
print(s.is_empty)
print(s.pop)