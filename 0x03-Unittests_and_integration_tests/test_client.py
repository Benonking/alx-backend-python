#!/usr/bin/env python3
'''
Module test_client 
'''
import unittest
from unittest.mock import patch, Mock

class TestGithuborgclient(unittest.TestCase):
	'''
	
	'''
	@patch('get_json')
	def test_org(self):
		'''
		test method client.org
		'''
		