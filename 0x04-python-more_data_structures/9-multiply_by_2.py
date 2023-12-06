#!/usr/bin/python3def multiply_by_2(a_dictionary):
    # Create a new dictionary to store the multiplied values
    multiplied_dict = {}

    # Iterate over the key-value pairs in the original dictionary
    for key, value in a_dictionary.items():
        multiplied_dict[key] = value * 2

    return multiplied_dict
