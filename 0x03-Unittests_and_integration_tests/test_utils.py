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


class TestAccessNestedmap(unittest.TestCase):
    '''
    test case for function utils.access_nested_map
    Technic: use parameterized for in puts
    '''
    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected_res: Union[Dict, int],) -> None:
        '''
        Test if fucntion returns expected out put
        '''
        self.assertEqual(access_nested_map(nested_map, path), expected_res)

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError),
        ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exeption: Union[int, Dict]) -> None:
        '''
        check for exceptions
        '''
        with self.assertRaises(exeption):
            access_nested_map(nested_map, path)
