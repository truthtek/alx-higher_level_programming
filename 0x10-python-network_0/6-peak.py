#!/usr/bin/python3

def find_peak(list_of_integers):
    """Find a peak element in a list of integers."""
    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]

# Test cases
print(find_peak([1, 2, 3, 4, 5]))  # Expected output: 5
print(find_peak([5, 4, 3, 2, 1]))  # Expected output: 5
print(find_peak([1, 4, 6, 2, 1]))  # Expected output: 6
print(find_peak([5, 4, 6, 2, 1, 4, 5, 2]))  # Expected output: 6
