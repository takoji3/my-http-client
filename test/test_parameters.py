#-*- coding: utf-8 -*-

import unittest
from parser import Parameters
from argparse import Namespace

class ParametersTest(unittest.TestCase):

    def test_method(self):
        namespace = Namespace(method='get')
        self.parameters = Parameters(namespace)
        self.assertEqual(self.parameters.method(), 'get')

    def test_method_not_defined(self):
        namespace = Namespace()
        self.parameters = Parameters(namespace)
        self.assertRaises(AttributeError, self.parameters.method)

if __name__ == '__main__':
    unittest.main()
