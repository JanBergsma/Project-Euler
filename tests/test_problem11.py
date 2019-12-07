import numpy as np
from src.problem11 import euler11, DATA


def test_euler_11_should_be_70600674():
    assert euler11(DATA) == 70600674
