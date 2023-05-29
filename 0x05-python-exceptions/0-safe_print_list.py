#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0
    try:
        for i in range(x):
            try:
                element = my_list[i]
                print(element, end="")
                printed += 1
            except IndexError:
                break

    except TypeError:
        return printed

    print()
    return printed
