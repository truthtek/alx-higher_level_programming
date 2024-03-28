#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.

Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    x_request_id = response.getheader('X-Request-Id')
    print(x_request_id)
