#!/usr/bin/python3
def uppercase(s):
    result = ""
    for c in s:
        result += chr(ord(c) & 223)
    print(result)
