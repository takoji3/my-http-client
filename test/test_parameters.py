#-*- coding: utf-8 -*-

import unittest
from parser import Parameters
from argparse import Namespace

class ParametersTest(unittest.TestCase):

    def test_method(self):
        self.parameters = Parameters(Namespace(method='get'))
        self.assertEqual(self.parameters.method(), 'get')

    def test_url(self):
        self.parameters = Parameters(Namespace(url='http://www.test.com'))
        self.assertEqual(self.parameters.url(), 'http://www.test.com')

    def test_url_with_prefix(self):
        self.parameters = Parameters(Namespace(url='test.com'))
        self.assertEqual(self.parameters.url(), 'http://test.com')

    def test_url(self):
        h = ['Host:test.com', 'User-Agent:Test User Agent']
        self.parameters = Parameters(Namespace(headers=h))
        self.assertEqual(
                self.parameters.headers(),
                dict({'Host': 'test.com', 'User-Agent': 'Test User Agent'})
                )

    def test_get_not_defined(self):
        namespace = Namespace()
        self.parameters = Parameters(namespace)
        self.assertRaises(AttributeError, self.parameters.method)

if __name__ == '__main__':
    unittest.main()
