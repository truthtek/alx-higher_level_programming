#!/usr/bin/python3

output = ""
upper = True

for i in range(90, 64, -1):
    if upper: 
        output += chr(i).upper()
    else:
        output += chr(i).lower()
    upper = not upper

print(output[::-1], end='')
