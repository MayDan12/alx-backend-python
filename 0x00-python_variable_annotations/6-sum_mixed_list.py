#!/usr/bin/env python3
"""This function takes mixed variables int nd string"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of elements in a list containing integers and floats.

    Args:
    mxd_lst (List[Union[int, float]]): A list of integers and/or
    floating-point numbers.

    Returns:
    float: The sum of the elements in the list.
    """
    return sum(mxd_lst)
