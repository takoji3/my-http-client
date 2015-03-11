#-*- coding: utf-8 -*-

import requests
from requests_oauthlib import OAuth1Session

class Request:
    REQUEST_PLAIN = 'plain'
    REQUEST_OAUTH = 'oauth'

    def execute(self, params):
        raise NotImplementedError("Implement execute method")

class PlainRequest(Request):
    def execute(self, params):
        method = params.method()
        url = params.url()
        param = self.__extract(method, params)
        return requests.request(
                method,
                url,
                **param
                )

    def __extract(self, method, params):
        param = { 'headers': params.headers() }
        if method in ('post', 'put'):
            param.update({ 'data': params.data() })
        return param

class OAuthRequest(Request):
    def execute(self, params):
        req = OAuth1Session(*params.oauth_parameters())
        method = params.method()
        url = params.url()
        param = self.__extract(method, params)
        return req.request(
                method,
                url,
                **param
                )

    def __extract(self, method, params):
        param = { 'headers': params.headers() }
        if method in ('post', 'put'):
            param.update({ 'data': params.data() })
        return param

def build_request(req_type):
    if req_type == Request.REQUEST_PLAIN:
        return PlainRequest()
    elif req_type.startswith(Request.REQUEST_OAUTH):
        return OAuthRequest()
    else:
        raise NotImplementedError('Undefined request type')
