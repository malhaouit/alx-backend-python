#!/usr/bin/env python3
"""This module includes an addition function with type annotations"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Takes a list of float numbers as argument and returns the float sum"""
    return sum(input_list)
