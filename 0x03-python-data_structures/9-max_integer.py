#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    sorted_list = sorted(my_list)
    max_value = sorted_list[-1]
    return max_value
