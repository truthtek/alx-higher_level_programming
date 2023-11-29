#!/usr/bin/python3

def magic_calculation(a, b, c):
    """Match bytecode provided by Holberton School."""
    if c < b:
        return (a)
    if a > b:
        return (c + b)
    return (c*b - a)
