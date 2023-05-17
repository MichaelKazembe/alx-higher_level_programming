#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = []
    for integer in my_list:
        if integer not in unique_integers:
            unique_integers.append(integer)
    return sum(unique_integers)
