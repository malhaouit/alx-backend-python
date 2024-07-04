#!/usr/bin/env python3
"""This module includes an addition function with mixed type annotations"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Takes a list of mixed type of numbers and returns the sum as float"""
    return sum(mxd_lst)
