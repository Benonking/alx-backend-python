#!/usr/bin/env python3
'''
Module test_utils
'''
from parameterized import parameterized
import unittest
from typing import Dict, Tuple, Union
from utils import (
    access_nested_map
)


class TestAccessNestedMap(unittest.TestCase):
    """Tests function  -> access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """Tests `access_nested_map`'s output."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
            ) -> None:
        """Tests function  access_nested_map exception raising."""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)
