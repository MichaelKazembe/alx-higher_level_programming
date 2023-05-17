#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_3 = []
    for element in set_1:
        if element in set_2:
            set_3.append(element)
    return set_3
