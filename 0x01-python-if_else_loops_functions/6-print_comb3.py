#!/usr/bin/python3
for i in range(10):
    for j in range(i+1, 10):
        print("{:02d}, ".format(i), end="{:02d}, ".format(j))

print("{:02d}".format(9))
