class Node:
    def __init__(self, prev=None, item =None, next=None) -> None:
        self.prev= prev
        self.item= item
        self.next = next

class DLL:
    def __init__(self, start=None) -> None:
        self.start = start

    def is_empty(self):
        return self.start == None

    def insert_at_start(self, data):
        n = Node(None, data, self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n

    def insert_at_last(self, data):
        temp = self.start
        if temp is not None:
            while temp.next is not None:
                temp = temp.next

        n= Node(temp, data, temp.next)
        if temp == None:
            self.start = n
        else:
            temp.next = n

    def search(self, data):
        temp = self.start
        if temp != None:
            while temp is not None:
                if temp.item == data:
                    return temp
                temp = temp.next
        return None
    
    def insert_after(self, temp, data):
        if temp != None:
            n = Node(temp, data, temp.next)
            if temp.next != None:
                temp.next.prev = n
            temp.next = n
            
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end = " ")
            temp = temp.next
    
    def delete_first(self):
        if not self.is_empty():
            self.start = self.start.next
            if self.start is not None:   
               self.start.prev = None
    
    def delete_last(self):
        temp = self.start
        if temp is None:
            pass
        if temp.next is None:
            self.start = None
        else:
            while temp.next != None:
                temp = temp.next
            temp.prev.next = None
    
    def delete_item(self, data):
        temp = self.start
        if temp is None:
            pass
        else:
            while temp is not None:
                if temp.item == data:
                    if temp.next is not None:
                        temp.next.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.next
                    else:
                        self.start = temp.next
                    break
                    
                temp = temp.next
    
    def __iter__(self):
        return DLLIterator(self.start)



class DLLIterator:
    def __init__(self, start) -> None:
        self.current= start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data



DLLlist =DLL();

DLLlist.insert_at_start(11)
DLLlist.insert_at_start(12)
DLLlist.insert_at_start(120)
DLLlist.insert_at_last(20)
# DLLlist.delete_first()
DLLlist.insert_after(DLLlist.search(12), 10)
DLLlist.delete_item(12)

print("--"*30)
print("Doubly link list items:")
DLLlist.print_list()
print()
print("--"*30)
for item in DLLlist:
    print(item, end=" ")
print()
print("--"*30)