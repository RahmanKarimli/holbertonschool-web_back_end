#!/usr/bin/env python3
"""sum_mixed_list function with type annotations."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of mixed floats and integers.

    Args:
        mxd_lst (List[Union[int, float]]):floats and integers to be summed.

    Returns:
        float: The sum of the list of mixed floats and integers.
    """
    return sum(mxd_lst)
