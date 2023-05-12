#!/usr/bin/python3
from magic_calculation_102 import add, sub

a = 0
b = ('add', 'sub')
c = 0

if a < b:
    c = add(a, b)
    for i in range(4, 6):
        c = add(c, i)
    return c
else:
    return sub(a, b)
