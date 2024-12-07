#!/usr/bin/env python3
"""make_multiplier function with type annotations."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by a multiplier.

    Args:
        multiplier (float): The multiplier to be used in the returned function.

    Returns:
        Callable[[float], float]: A function that multiplies a float.
    """
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
