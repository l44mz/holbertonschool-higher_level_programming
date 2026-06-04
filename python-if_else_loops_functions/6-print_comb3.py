#!/usr/bin/python3
print("{}".format(", ".join(
    str(i) + str(j)
    for i in range(10)
    for j in range(i + 1, 10)
)))
