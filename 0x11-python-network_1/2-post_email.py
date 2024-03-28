#!/usr/bin/python3
"""
This module sends a POST request to a given URL with an email as a parameter,
and displays the body of the response, decoded in utf-8.
"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    params = {'email': email}
    data = urllib.parse.urlencode(params)
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
