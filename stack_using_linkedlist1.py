# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class Stack:
#     def __init__(self):
#         self.top = None
#         self._size = 0

#     def is_empty(self):
#         return self.top is None

#     def push(self, item):
#         new_node = Node(item)
#         new_node.next = self.top
#         self.top = new_node
#         self._size += 1

#     def pop(self):
#         if self.is_empty():
#             raise IndexError("pop from empty stack")
#         popped_node = self.top
#         self.top = self.top.next
#         self._size -= 1
#         return popped_node.value

#     def peek(self):
#         if self.is_empty():
#             raise IndexError("peek from empty stack")
#         return self.top.value

#     def size(self):
#         return self._size

#     def __str__(self):
#         current = self.top
#         items = []
#         while current:
#             items.append(current.value)
#             current = current.next
#         return str(items)

# Example usage
# if __name__ == "__main__":
#     stack = Stack()
#     stack.push(1)
#     stack.push(2)
#     stack.push(3)
#     print("Stack after pushes:", stack)
#     print("Top item:", stack.peek())
#     print("Popped item:", stack.pop())
#     print("Stack after pop:", stack)
#     print("Is stack empty?", stack.is_empty())
#     print("Stack size:", stack.size())
