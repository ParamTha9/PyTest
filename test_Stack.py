# import pytest
# from stack_using_linkedlist import Stack

# @pytest.fixture
# def stack():
#     return Stack()

# def test_push(stack):
#     stack.push(1)
#     stack.push(2)
#     assert stack.size() == 2

# def test_pop(stack):
#     stack.push(1)
#     stack.push(2)
#     item=stack.pop()
#     assert item == 2
#     assert stack.size() == 1

# def test_peek(stack):
#     stack.push(1)
#     stack.push(2)
#     item = stack.peek()
#     assert item == 2
#     assert stack.size() == 2

# def test_is_empty(stack):
#     assert stack.is_empty()
#     stack.push(1)
#     assert not stack.is_empty()

# def test_size(stack):
#     assert stack.size()==0
#     stack.push(1)
#     assert stack.size()==1
#     stack.push(2)
#     assert stack.size()==2

# def test_pop_empty(stack):
#     with pytest.raises(IndexError, match="pop from empty stack"):
#         stack.pop()

# def test_peek_empty(stack):
#     with pytest.raises(IndexError, match="peek from empty stack"):
# #         stack.peek()

# # if __name__=="__main__":
#     pytest.main()
