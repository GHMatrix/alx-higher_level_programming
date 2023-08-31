#!/usr/bin/python3
"""
Function to find a peak in unsorted integers
"""


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers."""
    if list_of_integers:
        return max(list_of_integers)
    return None
