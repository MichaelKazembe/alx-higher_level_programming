#!/usr/bin/python3
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def magic_calculation_102(a, b):
    c = 0

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
    else:
        return sub(a, b)
    
    return c
