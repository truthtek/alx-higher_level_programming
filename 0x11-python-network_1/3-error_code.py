#!/usr/bin/python3
"""
This module sends a request to a given URL and displays the body of the
response, decoded in utf-8. If an HTTP error occurs, it catches the exception
and prints the HTTP status code.
"""

import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
