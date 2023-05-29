#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    try:
        for value in my_list:
            try:
                if isinstance(value, int):
                    print("{:d}".format(value), end="")
                    printed += 1
            except (ValueError, TypeError):
                pass
            if printed == x:
                break
    except TypeError:
        pass
    print()
    return printed
