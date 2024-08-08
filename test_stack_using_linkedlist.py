import pytest
from stackusingabstract import stack_using_linkedlist
from test_stackusingabstract import TestsAbstractStack

class TestsStackUsingLinkedList(TestsAbstractStack):
    
    @pytest.fixture
    def stack(self):
        return stack_using_linkedlist()

    def expected_str(self, items):
        return str(items)

if __name__ == "__main__":
    pytest.main()
