class Stack:
    """Стек глибино 5 елементів"""
    def __init__(self, stack = [], depth = 0):
        self.stack = stack
        self.depth = depth

    def push(self, new_element):
        if len(self.stack) < self.depth:
            self.stack.append(new_element)
            return self.stack
        else:
            return 'Stack is full'

    @property
    def pop(self):
        if self.stack:
            self.stack.pop()
            return self.stack
        return 'Stack is empty'

    @property
    def length(self):
        return str(len(self.stack))

    @property
    def has_elements(self):
        if self.stack:
            return True
        else:
            return False


s = Stack([8, 'b'], depth = 7,)

print(s.push(2))
print(s.push('a'))
print(s.push(7))
print(s.push('j'))
print(s.push('11'))
print(s.push('k'))
print(s.pop)
print(s.length)
print(s.has_elements)
print(s.pop)
print(s.pop)
print(s.pop)
print(s.push('j'))
print(s.push('11'))
print(s.pop)
print(s.pop)
print(s.has_elements)
print(s.pop)
print(s.has_elements)
print(s.pop)
print(s.pop)
print(s.pop)
print(s.pop)
print(s.has_elements)