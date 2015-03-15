#-*- coding: utf-8 -*-

class Response:

    def __init__(self, response, parameters):
        self._response = response
        self._parameters = parameters

    def out(self):
        res = self._response.content
        if self._parameters.debug():
            res = self._header() + res
        return res

    def _header(self):
        h = str(self._response.status_code) + "\n"
        h = h + "\n".join(["{}: {}".format(k, v) for k, v in self._response.headers.items()])
        return h + "\n" * 2
