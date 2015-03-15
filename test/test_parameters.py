#-*- coding: utf-8 -*-

import unittest
from parser import Parameters
from argparse import Namespace

class ParametersTest(unittest.TestCase):

    def test_method(self):
        parameters = Parameters(Namespace(method='get'))
        self.assertEqual(parameters.method(), 'get')

    def test_url(self):
        parameters = Parameters(Namespace(url='http://www.test.com'))
        self.assertEqual(parameters.url(), 'http://www.test.com')

    def test_url_with_prefix(self):
        parameters = Parameters(Namespace(url='test.com'))
        self.assertEqual(parameters.url(), 'http://test.com')

    def test_header(self):
        h = ['Host:test.com', 'User-Agent:Test User Agent']
        parameters = Parameters(Namespace(headers=h))
        self.assertEqual(parameters.headers(), dict({'Host': 'test.com', 'User-Agent': 'Test User Agent'}))

    def test_default_header(self):
        parameters = Parameters(Namespace(headers=''))
        self.assertEqual(parameters.headers(), dict())

    def test_data(self):
        d = ['test:abc def', 'id:123']
        parameters = Parameters(Namespace(data=d))
        self.assertEqual(parameters.data(), dict({'test': 'abc def', 'id': '123'}))

    def test_default_data(self):
        parameters = Parameters(Namespace(data=''))
        self.assertEqual(parameters.data(), dict())

    def test_request_type_plain(self):
        parameters = Parameters(Namespace(type='plain'))
        self.assertEqual(parameters.request_type(), 'plain')

    def test_request_type_oauth(self):
        parameters = Parameters(Namespace(type='oauth'))
        self.assertEqual(parameters.request_type(), 'oauth')

    def test_oauth_parameters_only_cunsumer_keys(self):
        parameters = Parameters(Namespace(consumer_key='consumer_key', consumer_secret='consumer_secret'))
        self.assertEqual(parameters.oauth_parameters(), ['consumer_key', 'consumer_secret'])

    def test_oauth_parameters(self):
        parameters = Parameters(Namespace(
            consumer_key='consumer_key',
            consumer_secret='consumer_secret',
            access_token='access_token',
            access_token_secret='access_token_secret'
            ))
        self.assertEqual(
                parameters.oauth_parameters(),
                ['consumer_key', 'consumer_secret', 'access_token', 'access_token_secret']
                )

    def test_debug_false(self):
        parameters = Parameters(Namespace(d=False))
        self.assertEqual(parameters.debug(), False)

    def test_debug_true(self):
        parameters = Parameters(Namespace(d=True))
        self.assertEqual(parameters.debug(), True)

    def test_get_not_defined(self):
        parameters = Parameters(Namespace())
        with self.assertRaises(AttributeError):
            parameters.method()

if __name__ == '__main__':
    unittest.main()
