#!/usr/bin/python3
def switch_values(a, b):
    # Insert your code here
    a, b = b, a
    return a, b

# Example usage:
a = 5
b = 10
a, b = switch_values(a, b)
print(a, b)  # Output: 10 5
