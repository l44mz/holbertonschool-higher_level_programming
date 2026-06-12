#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    biggest = my_list[0]
    for nb in my_list:
        if nb > biggest:
            biggest = nb
    return biggest
