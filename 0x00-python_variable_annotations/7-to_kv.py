#!/usr/bin/env python3
"""The module includes a function with type annotations and returns a tuple"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes two different type of arguments and returns a mixed tuple.
    Parameters:
    k (str): String
    v (typing.Union[int, float]): The value can be int or float

    Returns: A tuple in this format (string_value, int_or_float_value)
    """
    return (k, v * v)
