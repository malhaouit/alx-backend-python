#!/usr/bin/env python3
"""This module includes a function with type annotations and returns float."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes a float argument and returns returns a function that multiplies
    a float by multiplier."""
    def multiplier_function(value: float):
        return value * multiplier
    return multiplier_function
