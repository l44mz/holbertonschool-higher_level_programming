#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a[:2]) + [0] * (2 - len(tuple_a))
    b = list(tuple_b[:2]) + [0] * (2 - len(tuple_b))
    return (a[0] + b[0], a[1] + b[1])
