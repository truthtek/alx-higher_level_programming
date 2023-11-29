#!/usr/bin/python3

output = ""
upper = True

for i in range(90, 64, -1):
    if upper:
        output += "{}".format(chr(i)) 
    else:
        output += "{}".format(chr(i).lower())
    upper = not upper

print("{}"[::-1].format(output), end='')
