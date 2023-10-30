#!/usr/bin/env python3
'''
Module test_utils
'''
from parameterized import parameterized
import unittest
from typing import Dict, Tuple, Union, Dict
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
            ({"a": 1}, ("a"), 1),
            ({"a": {"b": 2}}, ("a"), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected_result: Union[Dict, int]) -> None:
        '''
        Test if fucntion returns expected out put
        '''

        res = access_nested_map(nested_map, path)
        self.assertEqual(res, expected_result)
