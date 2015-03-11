#-*- coding: utf-8 -*-

from parser import arg_parse
from request import build_request

def main():
    params = arg_parse()
    request = build_request(params.request_type())
    response = request.execute(params)
    print response.status_code
    print "\n".join(["{}: {}".format(k, v) for k, v in response.headers.items()]) + "\n"
    print response.content

if __name__ == '__main__':
    main()
