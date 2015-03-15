#-*- coding: utf-8 -*-

import requests
from requests_oauthlib import OAuth1Session
from response import Response

REQUEST_PLAIN = 'plain'
REQUEST_OAUTH = 'oauth'

class Request:

    def __init__(self):
        raise NotImplementedError

    def execute(self, params):
        method = params.method()
        url = params.url()
        param = { 'headers': params.headers() }
        if method in ('post', 'put'):
            param.update({ 'data': params.data() })

        res = self._request.request(
                method,
                url,
                **param
                )
        return Response(res, params)

class PlainRequest(Request):
    def __init__(self):
        self._request = requests

class OAuthRequest(Request):
    def __init__(self, oauth_parameters):
        self._request = OAuth1Session(*oauth_parameters)

def build_request(parameters):
    if parameters.request_type() == REQUEST_PLAIN:
        return PlainRequest()
    elif parameters.request_type().startswith(REQUEST_OAUTH):
        return OAuthRequest(parameters.oauth_parameters())
    else:
        raise NotImplementedError('Undefined request type')
