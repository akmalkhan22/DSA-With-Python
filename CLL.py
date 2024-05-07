#------------- Circular linklist---------->
class Node:
    def __init__(self, item=None, next=None) -> None:
        self.item = item
        self.next = next

class CLL:
    def __init__(self, last=None) -> None:
        self.last = last
    
    def is_empty(self):
        return self.last == None
    
    def insert_at_start(self, item):
        n= Node(item)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
    
    def insert_at_last(self, item):
        n = Node(item)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
            self.last = n

    def search(self, item):
        if not self.is_empty():
            temp = self.last.next
            while temp != self.last:
                if temp.item == item:
                    return temp
                temp = temp.next
            if temp.item == item:
                return temp
        else:
            return None


    def insert_after(self, temp, item):
        n= Node(item, temp.next)
        if temp != None:
            if temp == self.last:
                temp.next = n
                self.last = n
            else:
                temp.next = n
        else:
            return None
        
    
    def print_list(self):
        if not self.is_empty():
            temp = self.last.next
            while temp != self.last:
                print(temp.item, end=" ")
                temp = temp.next

            print(temp.item)

    def delete_first(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                self.last.next = self.last.next.next

    def delete_last(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                temp = self.last.next
                while temp.next != self.last:
                    temp = temp.next
                temp.next = self.last.next
                self.last = temp

    def delete_item(self, data):
        if not self.is_empty():
            temp = self.last.next
            if temp == self.last:
                if temp.item == data:
                    self.last =  None
            else:
                while temp != self.last:
                    if temp.next == self.last:
                        if self.last.item == data:
                            self.delete_last()
                            break

                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break

                    temp = temp.next

    def __iter__(self):
        if self.last == None:
          return CLLIterator(None)
        else:
            return CLLIterator(self.last.next)


class CLLIterator:
    def __init__(self, start) -> None:
        self.current = start
        self.start = start
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current == None:
            raise StopIteration
        if self.current == self.start and self.count == 1:
            raise StopIteration
        else:
            self.count = 1
        data = self.current.item
        self.current = self.current.next
        return data



        

list = CLL()
list.insert_at_start(34)
list.insert_at_last(2)
list.insert_after(list.search(34), 4)
list.insert_after(list.search(2), 14)
# list.delete_first()
# list.delete_last()
list.delete_item(2)
print("--"*30)
list.print_list()
print()
print("--"*30)
for item in list:
    print(item, end=" ")