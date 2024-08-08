import pytest
from stackusingabstract import stack_using_array
from test_stackusingabstract import TestsAbstractStack

class TestsStackUsingArray(TestsAbstractStack):

    @pytest.fixture
    def stack(self):
        return stack_using_array()

    def expected_str(self, items):
        return str(items)

if __name__ == "__main__":
    pytest.main()
