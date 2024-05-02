#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple
"""Annotate the below function’s parameters and return
values with the appropriate types"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the list.

    Args:
    lst (Iterable[Sequence]): The input iterable containing
    sequences (e.g., list, tuple).

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples where the first
    element is a sequence (e.g., list, tuple)
    from the input iterable and the second element is the
    length of that sequence.
    """
    return [(i, len(i)) for i in lst]
