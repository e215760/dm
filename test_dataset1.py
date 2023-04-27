import pytest
from dataset1 import true_function

@pytest.mark.parametrize(('number','expected'),[
    (0,123123),
])
def test_true_function(number,expected):
    assert true_function(number) == expected