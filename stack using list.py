class Stack(list):
    def is_empty(self):
        return len(self) == 0
    
    def push(self, data):
        self.append(data)
    
    def pop(self):
        if not self.is_empty():
            super().pop()
        else:
            raise IndexError("Stack is empty")
    
    def peek(self):
        if not self.is_empty():
           return self[-1]
        else:
            raise IndexError('Stack is empty')
    
    def size(self):
        return len(self)
    
    def insert(self, index, data):
        raise AttributeError("No attribut 'insert' in stack.")
    
stk =Stack()
stk.push(10)
stk.push(20)
stk.push(30)
stk.push(40)
print("top value ", stk.peek())
    