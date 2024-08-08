from abc import ABC, abstractmethod

class stack(ABC):
    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def push(self, item):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def __str__(self):
        pass 

class Node:
    def __init__(self, value):
         self.value = value
         self.next = None
    
class stack_using_linkedlist(stack):
    def __init__(self):
        self.top = None
        self._size = 0

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_node = self.top
        self.top = self.top.next
        self._size -= 1
        return popped_node.value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.value

    def size(self):
        return self._size

    def __str__(self):
        current = self.top
        items = []
        while current:
            items.append(current.value)
            current = current.next
        return str(items)
    
class stack_using_array(stack):
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return len(self.items)==0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    