#!/usr/bin/python3
""" find peak of unsorted list of integers """


def search(low, high, ints):

    mid = (low + high) // 2

    if low == high:
        return ints[high]
    if ints[mid] < ints[mid + 1]:
        return(search(mid + 1, high, ints))

    return(search(low, mid, ints))


def find_peak(list_of_integers):

    if not list_of_integers:
        return

    return(search(0, len(list_of_integers) - 1, list_of_integers))
