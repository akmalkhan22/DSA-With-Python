# Circular Doubly linklist
class Node:
    def __init__(self, item = None, prev = None, next= None):
        self.prev = prev
        self.item = item
        self.next = next

class CDL:
    def __init__(self, start = None):
        self.start = start
    
    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            n.prev = n
        else:
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n
        self.start = n
        
    def insert_at_last(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            n.prev = n
            self.start = n
        else:
            n.next = self.start
            n.prev = self.start.prev
            n.prev.next = n
            self.start.prev = n

    def search(self, data):
        temp = self.start
        if temp == None:
            return None
        if temp.item == data:
            return temp
        else:
            temp = temp.next
            while temp != self.start:
                if temp.item == data:
                    return temp
                temp = temp.next
            return None
        
    def insert_after(self, temp, data):
        n = Node(data)
        if temp != None:
            n.next = temp.next
            n.prev = temp
            temp.next.prev = n
            temp.next = n
        
    def print_list(self):
        temp = self.start
        if temp is not None:
            print(temp.item, end=" ")
            temp = temp.next
            while temp != self.start:
                print(temp.item, end=" ")
                temp = temp.next


    def delete_first(self):
        if self.start is not None:
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.prev.next = self.start.next
                self.start.next.prev = self.start.prev
                self.start = self.start.next

    def delete_last(self):
        if self.start is not None:
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.prev.prev.next = self.start
                self.start.prev = self.start.prev.prev


    def delete_item(self, data):
        if self.start is not None:
            if self.start.next == self.start:
                if self.start.item == data:
                    self.start = None
            else:
                temp = self.start.next
                while temp != self.start:
                    if temp.item == data:
                        temp.prev.next = temp.next
                        temp.next.prev =temp.prev
                    temp = temp.next

    
    def __iter__(self):
        return CDLIterator(self.start)




class CDLIterator:
    def __init__(self, start) -> None:
        self.current = start
        self.start = start
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current == None:
            raise StopIteration
        
        if self.current == self.start and self.count==1:
            raise StopIteration
        else:
            self.count =1
        
        data = self.current.item
        self.current = self.current.next
        return data



list = CDL()
list.insert_at_start(2)
list.insert_at_start(4)
list.insert_at_start(7)
list.insert_at_last(12)
list.insert_at_last(23)
list.insert_at_last(30)
list.insert_at_last(37)
list.delete_last()
list.delete_item(2)
# list.delete_first()
print("--"*30)
list.print_list()
print()
print("--"*30)
for i in list:
    print(i, end=" ")
print()
print("--"*30)

          
        
           