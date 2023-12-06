#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Create an empty set to store the elements present in only one set
    different_elements = set()

    # Iterate over the elements in set_1
    for element in set_1:
        # Check if the element is not present in set_2
        if element not in set_2:
            different_elements.add(element)

    # Iterate over the elements in set_2
    for element in set_2:
        # Check if the element is not present in set_1
        if element not in set_1:
            different_elements.add(element)

    return different_elements
