#!/usr/bin/python3
def common_elements(set_1, set_2):
    # Create an empty set to store the common elements
    common_set = set()

    # Iterate over the elements in set_1
    for element in set_1:
        # Check if the element is present in set_2
        if element in set_2:
            common_set.add(element)

    return common_set
