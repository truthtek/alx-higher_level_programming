#!/usr/bin/python3
output = ""
for i in range(90, 64, -1):
    output += "{}{}".format(chr(i + 32), chr(i))

print(output, end='')
