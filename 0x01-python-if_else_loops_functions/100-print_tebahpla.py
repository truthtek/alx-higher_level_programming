#!/usr/bin/python3
output = ""
for i in range(90, 64, -1):
    if i % 2 == 0:
        output += "{}{}".format(chr(i + 32), chr(i))

print(output[::-1], end='')
