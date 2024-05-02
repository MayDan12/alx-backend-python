#!/usr/bin/env python3
from typing import List, Tuple
"""Annotate the below function’s parameters and return
values with the appropriate types"""


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Calculate the length of each element in the list.

    Args:
    lst (List[str]): The input list of strings.

    Returns:
    List[Tuple[str, int]]: A list of tuples where the first element is
    the original string
    from the input list and the second element is the length of that string.
    """
    return [(i, len(i)) for i in lst]
