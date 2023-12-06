#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Create an empty set to store unique integers
    unique_integers = set()

    # Iterate over the elements in the input list
    for element in my_list:
        # Add the element to the set if it is an integer
        if isinstance(element, int):
            unique_integers.add(element)

    # Compute the sum of the unique integers
    total = sum(unique_integers)

    return total
