#!/usr/bin/env python3
'''
Unit test for access_nested_map function using parameterized testing.
'''

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    '''
    Unit test class for access_nested_map function.
    '''

    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2),
    ])
    def test_access_nested_map(self, nested_map, path, result):
        '''
        Test access_nested_map function with various inputs.

        Args:
            nested_map (dict): The nested dictionary to access.
            path (tuple): The sequence of keys
            to follow in the nested dictionary.
            result: The expected result when
            accessing the nested dictionary with the given path.
        '''
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ('a',)),
        ({'a': 1}, ('a', 'b')),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        '''Test access_nested_map function raises KeyError properly.'''
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(error.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    '''
    Unit test class for get_json function.
    '''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('test_utils.get_json')
    def test_get_json(self, test_url, test_payload, mock_get):
        """ Method to test that utils.get_json returns the expected result """
        mock_get.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    '''
    Unit test class for memoize function.
    '''
    def test_memoize(self):
        '''
        Test that when calling a_property twice, the correct result is
        returned but a_method is only called once using assert_called_once
        '''
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            test_class = TestClass()
            result = test_class.a_property
            result = test_class.a_property
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
