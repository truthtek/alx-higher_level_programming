#!/usr/bin/python3

for digit3 in range(0, 10):
    for digit2 in range(digit1 + 1, 10):
        if digit3 == 8 and digit2 == 9:
            print("{}{}".format(digit3, digit2))
        else:
            print("{}{}".format(digit3, digit2), end=", ")
