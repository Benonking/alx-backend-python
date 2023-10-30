#!/usr/bin/env python3
'''
Module test_utils
'''
from parameterized import parameterized
import unittest
import requests
from typing import Dict, Tuple, Union
from utils import (
    access_nested_map,
    get_json,
    memoize,
)
from unittest.mock import patch, Mock


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


class TestGetJson(unittest.TestCase):
    '''
    implement test_get_json function for utils.get_json
    '''
    @parameterized.expand([
        ("http://example.com", {"payload": True},),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(
            self, test_url: str,
            test_payload: Dict[str, any],
            mock_get
            ) -> None:
        '''test utils.get_json function'''
        # create a mock response
        mock_res = Mock()
        mock_res.json.return_value = test_payload

        # config the mock get method to return the mock response
        mock_get.return_value = mock_res
        result = get_json(test_url)

        # Assert that mock get method was called once with the url
        mock_get.assert_called_once_with(test_url)
        # assert that the result maches the expected JSON data
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    '''implement test_memoize method'''
    def test_memoize(self):
        '''test Tesclass instance a_method'''
        class TestClass:
            '''
            Define methods:
                a-method: returns 42
                a_property: return a_method()
            '''
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_instance = self.Testclass()
        with patch.object(test_instance, 'a_method') as mock_a_method:
            # call a_property twice
            res1 = test_instance.a_property
            res2 = test_instance.a_property

            # check if a method was called once
            mock_a_method.assert_called_once()
            self.assertEqual(res1, 42)
            self.assertEqual(res2, 2)
