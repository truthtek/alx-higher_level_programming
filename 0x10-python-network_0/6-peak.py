#!/usr/bin/python3

def find_peak(list_of_integers):
    """Find a peak element in a list of integers."""
    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    # Base case: if list has only one element, return it
    if len(list_of_integers) == 1:
        return list_of_integers[0]

    mid_idx = len(list_of_integers) // 2
    mid_elem = list_of_integers[mid_idx]

    # Compare mid element with its neighbors
    if (mid_idx == 0 or mid_elem >= list_of_integers[mid_idx - 1]) and \
       (mid_idx == len(list_of_integers) - 1 or mid_elem >= list_of_integers[mid_idx + 1]):
        return mid_elem

    # If mid element is not peak, search in the left or right half
    if mid_idx > 0 and mid_elem < list_of_integers[mid_idx - 1]:
        return find_peak(list_of_integers[:mid_idx])
    else:
        return find_peak(list_of_integers[mid_idx + 1:])

# Test cases
print(find_peak([1, 2, 3, 4, 5]))  # Expected output: [5]
print(find_peak([5, 4, 3, 2, 1]))  # Expected output: [5]
print(find_peak([1, 4, 6, 2, 1]))  # Expected output: [6]
print(find_peak([5, 4, 6, 2, 1, 4, 5, 2]))  # Expected output: [6]
