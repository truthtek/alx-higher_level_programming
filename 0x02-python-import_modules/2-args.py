#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    print("Number of argument{}:{}".format("s" if argc != 1 else "", argc))
    print(".") if argc == 0 else print("\n".join(["{}: {}".format(i, sys.argv[i])
                                                  for i in range(1, len(sys.argv))]))
