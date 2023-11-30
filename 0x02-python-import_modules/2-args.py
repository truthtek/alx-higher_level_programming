#!/usr/bin/env python3
"""Print the number and list of command line arguments."""

import sys

def main():
    """Main function"""
    args = sys.argv[1:]
    num_args = len(args)
    
    print(f"{num_args} {'argument' if num_args == 1 else 'arguments'}:")
    
    if num_args > 0:
        for idx, arg in enumerate(args, start=1):
            print(f"{idx}: {arg}")
    else:
        print(".")

if __name__ == "__main__":
    main()
