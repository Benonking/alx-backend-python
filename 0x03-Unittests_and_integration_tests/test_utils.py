#!/usr/bin/env python3
'''
Module test_utils
'''
from parameterized import parameterized, parameterized_class
import unittest
from typing import Mapping, Tuple, Union, Mapping
from utils import access_nested_map


class TestAccessNestedmap(unittest.TestCase):
    '''
    test case for function utils.access_nested_map
    Technic: use parameterized for in puts
    '''
    @parameterized.expand(
        [
            ({"a": 1}, ["a"], 1),
            ({"a": {"b": 2}}, ["a"], {"b": 2}),
            ({"a": {"b": 2}}, ["a", "b"], 2)
        ]
    )
    def test_access_nested_map(
            self,
            nested_map: Mapping,
            path: Tuple[str],
            expected_result: Union[Mapping, int]) -> None:
        '''
        test if fucntion returns
        '''
        try:
            res = access_nested_map(nested_map, path)
            self.assertEqual(res, expected_result)
        except KeyError as e:
            self.assertIsInstance(expected_result, type(e))


if __name__ == "__main__":
    unittest.main()
