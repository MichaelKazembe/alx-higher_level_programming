#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    i = 0
    j = 0
    if len(tuple_a) < 2 or len(tuple_b) < 2:
        tuple_c = tuple_a + tuple_b
    else:
        tuple_c = (tuple_a[i] + tuple_b[i], tuple_a[j] + tuple_b[j])
    return tuple_c
