#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        desired_key = None
        biggest_value = max(a_dictionary.values())
        for key, value in a_dictionary.items():
            if value == biggest_value:
                desired_key = key
                break
        return desired_key
