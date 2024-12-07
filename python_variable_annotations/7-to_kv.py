#!/usr/bin/env python3
"""to_kv function with type annotations."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing the key and the square of the value.

    Args:
        k (str): The key to be returned.
        v (Union[int, float]): The value to be squared.

    Returns:
        Tuple[str, float]:the key and the square of the value.
    """
    return (k, v * v)
