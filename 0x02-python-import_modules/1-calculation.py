#!/usr/bin/python3

def perform_calculations(a, b):
    """Perform calculations using the provided values."""
    from calculator_1 import add, sub, mul, div

    sum_result = add(a, b)
    diff_result = sub(a, b)
    prod_result = mul(a, b)
    quot_result = div(a, b)

    return sum_result, diff_result, prod_result, quot_result

def print_results(a, b, sum_result, diff_result, prod_result, quot_result):
    """Print the results of the calculations."""
    print("{} + {} = {}".format(a, b, sum_result))
    print("{} - {} = {}".format(a, b, diff_result))
    print("{} * {} = {}".format(a, b, prod_result))
    print("{} / {} = {}".format(a, b, quot_result))

if __name__ == "__main__":
    a = 10
    b = 5

    sum_result, diff_result, prod_result, quot_result = perform_calculations(a, b)
    print_results(a, b, sum_result, diff_result, prod_result, quot_result)
