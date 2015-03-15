#-*- coding: utf-8 -*-

from parser import arg_parse
from request import build_request

def main():
    params = arg_parse()
    request = build_request(params)
    response = request.execute(params)
    result = response.out()
    print(result)

if __name__ == '__main__':
    main()
