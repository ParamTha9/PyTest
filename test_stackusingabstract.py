import pytest
from abc import ABC, abstractmethod

class TestsAbstractStack(ABC):

    @abstractmethod
    @pytest.fixture
    def stack(self):
        pass

    def test_is_empty(self, stack):
        assert stack.is_empty()
        stack.push(1)
        assert not stack.is_empty()

    def test_push(self, stack):
        stack.push(1)
        stack.push(2)
        assert stack.size() == 2
        assert str(stack) == self.expected_str([2, 1])

    def test_pop(self, stack):
        stack.push(1)
        stack.push(2)
        assert stack.pop() == 2
        assert stack.pop() == 1
        assert stack.is_empty()

    def test_peek(self, stack):
        stack.push(1)
        stack.push(2)
        assert stack.peek() == 2
        stack.pop()
        assert stack.peek() == 1

    def test_size(self, stack):
        assert stack.size() == 0
        stack.push(1)
        assert stack.size() == 1
        stack.push(2)
        assert stack.size() == 2

    def test_pop_empty(self, stack):
        with pytest.raises(IndexError, match="pop from empty stack"):
            stack.pop()

    def test_peek_empty(self, stack):
        with pytest.raises(IndexError, match="peek from empty stack"):
            stack.peek()

    @abstractmethod
    def expected_str(self, items):
        pass




# import pytest
# from abc import ABC, abstractmethod

# class TestAbstractStack(ABC):

#     @abstractmethod
#     @pytest.fixture
#     def stack(self):
#         pass

#     def test_is_empty(self, stack):
#         assert stack.is_empty()
#         stack.push(1)
#         assert not stack.is_empty()

#     def test_push(self, stack):
#         stack.push(1)
#         stack.push(2)
#         assert stack.size() == 2
#         assert str(stack) == self.expected_str([2, 1])

#     def test_pop(self, stack):
#         stack.push(1)
#         stack.push(2)
#         assert stack.pop() == 2
#         assert stack.pop() == 1
#         assert stack.is_empty()

#     def test_peek(self, stack):
#         stack.push(1)
#         stack.push(2)
#         assert stack.peek() == 2
#         stack.pop()
#         assert stack.peek() == 1

#     def test_size(self, stack):
#         assert stack.size() == 0
#         stack.push(1)
#         assert stack.size() == 1
#         stack.push(2)
#         assert stack.size() == 2

#     def test_pop_empty(self, stack):
#         with pytest.raises(IndexError, match="pop from empty stack"):
#             stack.pop()

#     def test_peek_empty(self, stack):
#         with pytest.raises(IndexError, match="peek from empty stack"):
#             stack.peek()

#     @abstractmethod
#     def expected_str(self, items):
#         pass




# import pytest
# from abc import ABC, abstractmethod
# from stackusingAbstract import stack, stack_using_array, stack_using_linkedlist

# @pytest.fixture
# @abstractmethod
# def stack():
#     return stack_using_array()

# @pytest.fixture
# def Stack_using_linkedlist():
#     return stack_using_linkedlist()

# def test_push(Stack_using_array):
#     Stack_using_array.push(1)
#     Stack_using_array.push(2)
#     assert Stack_using_array.size() == 2

# def test_pop(Stack_using_array):
#     Stack_using_array.push(1)
#     Stack_using_array.push(2)
#     item = Stack_using_array.pop()
#     assert item == 2
#     assert Stack_using_array.size() == 1

# def test_peek(Stack_using_array):
#     Stack_using_array.push(1)
#     Stack_using_array.push(2)
#     item = Stack_using_array.peek()
#     assert item == 2
#     assert Stack_using_array.size() == 2

# def test_is_empty(Stack_using_array):
#     assert Stack_using_array.is_empty()
#     Stack_using_array.push(1)
#     assert not Stack_using_array.is_empty()

# def test_size(Stack_using_array):
#     assert Stack_using_array.size() == 0
#     Stack_using_array.push(1)
#     assert Stack_using_array.size() == 1
#     Stack_using_array.push(2)
#     assert stack_using_array.size() == 2

# def test_pop_empty(Stack_using_array):
#     with pytest.raises(IndexError, match="pop from empty stack"):
#         Stack_using_array.pop()

# def test_peek_empty(Stack_using_array):
#     with pytest.raises(IndexError, match="peek from empty stack"):
#         Stack_using_array.peek()
        
# def test_push(Stack_using_linkedlist):
#     Stack_using_linkedlist.push(1)
#     Stack_using_linkedlist.push(2)
#     assert Stack_using_linkedlist.size() == 2

# def test_pop(Stack_using_linkedlist):
#     Stack_using_linkedlist.push(1)
#     Stack_using_linkedlist.push(2)
#     item=Stack_using_linkedlist.pop()
#     assert item == 2
#     assert Stack_using_linkedlist.size() == 1

# def test_peek(Stack_using_linkedlist):
#     Stack_using_linkedlist.push(1)
#     Stack_using_linkedlist.push(2)
#     item = Stack_using_linkedlist.peek()
#     assert item == 2
#     assert Stack_using_linkedlist.size() == 2

# def test_is_empty(Stack_using_linkedlist):
#     assert Stack_using_linkedlist.is_empty()
#     Stack_using_linkedlist.push(1)
#     assert not Stack_using_linkedlist.is_empty()

# def test_size(Stack_using_linkedlist):
#     assert Stack_using_linkedlist.size() == 0
#     Stack_using_linkedlist.push(1)
#     assert Stack_using_linkedlist.size() == 1
#     Stack_using_linkedlist.push(2)
#     assert Stack_using_linkedlist.size() == 2

# def test_pop_empty(Stack_using_linkedlist):
#     with pytest.raises(IndexError, match="pop from empty stack"):
#         Stack_using_linkedlist.pop()

# def test_peek_empty(Stack_using_linkedlist):
#     with pytest.raises(IndexError, match="peek from empty stack"):
#         Stack_using_linkedlist.peek()


# if __name__=="__main__":
#     pytest.main()