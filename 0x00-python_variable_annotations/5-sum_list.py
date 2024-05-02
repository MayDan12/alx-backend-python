#!/usr/bin/env python3
from typing import List
"""This function sum_list takes a list
of input of float and return thier sums"""


def sum_list(input_list: List[float]) -> float:
    """Calculates the sum of all elements in a list of floats.

    Args:
        input_list: The list of floats.

    Returns:
        The sum of all elements in the list as a float.
    """
    total_sum = 0.0
    for num in input_list:
        total_sum += num
    return total_sum
