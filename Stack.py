# class Node:
#     def __init__(self, item = None, next = None) -> None:
#         self.item = item
#         self.next = next

class Stack:
    def __init__(self) -> None:
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
           
            raise IndexError('Stack is empty')
    
    def peek(self):
       if not self.is_empty():
           return self.items[-1]
       else:
           raise IndexError('Stack is empty')
       
    def size(self):
        return len(self.items)
    
st = Stack()
st.push(3)
st.push(23)
st.push(20)
st.push(10)
st.push(14)

print(st.pop())
print(st.peek())
 

    