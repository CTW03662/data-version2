import pytest
import sys
import os

# Add the 'src' directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from src.exercise1 import divide

@pytest.mark.parametrize(['input1', 'input2', 'output'], [
    (10, 2, 5.0),    # Positive Division
    (-8, 4, -2.0),   # Negative Division
    (5, 3, 1.6666666666666667),  # Fractional Division
    (10, 0, ZeroDivisionError),  # Division by zero
])

def test_divide_function(input1, input2, output):
    if output is ZeroDivisionError:
        with pytest.raises(ZeroDivisionError):
            assert divide(input1, input2) == pytest.approx(output)
    else:
        assert divide(input1, input2) == pytest.approx(output)

    