#!/usr/bin/env python3
"""This module covers utils.access_nested_map testing.
See file utils.py
"""

import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Union, Dict

access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test suite for access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self, nested_map: Mapping,
            path: Sequence,
            expected: Union[int, Dict]) -> None:
        """Test access_nested_map with different inputs"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
