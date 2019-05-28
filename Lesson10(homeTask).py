class Stack:
    '''Стек глибино 5 елементів'''
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


print(Stack().push(2))
print(Stack().push('a'))
print(Stack().push(7))
print(Stack().push('j'))
print(Stack().push('11'))
print(Stack().push('k'))
print(Stack().pop)
print(Stack().length)
print(Stack().is_empty)
print(Stack().pop)
print(Stack().pop)
print(Stack().pop)
print(Stack().pop)
print(Stack().pop)
print(Stack().is_empty)
print(Stack().pop)