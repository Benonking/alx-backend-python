#!/usr/bin/env python3

'''
Module test_client
'''
from client import GithubOrgClient
import unittest
from unittest.mock import (
    patch,
    MagicMock,
    Mock
)
from parameterized import parameterized
from typing import Dict


class TestGithuborgclient(unittest.TestCase):
    '''
    tests for GithubClient class
    '''
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch("client.get_json")
    def test_org(
            self,
            org: str,
            resp: Dict,
            mock_fn: MagicMock) -> None:
        '''
        test method client.org
        '''
        mock_fn.return_value = MagicMock(return_value=resp)
        gh_client = GithubOrgClient(org)
        self.assertEqual(gh_client.org(), resp)
        mock_fn.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org))
