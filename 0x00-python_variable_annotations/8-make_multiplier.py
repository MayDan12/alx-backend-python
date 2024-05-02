#!/usr/bin/env python3
from typing import Callable
"""function make_multiplier that takes a float multiplier as argument
and returns a function that multiplies a float by multiplier"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by a given multiplier.

    Args:
    multiplier (float): The multiplier to use for multiplication.

    Returns:
    Callable[[float], float]: A function that takes a float and returns
    the result of multiplying it by the multiplier.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
