#!/usr/bin/python3
def common_elements(set_1, set_2):
    n = []
    for k in set_1:
        if k in set_2:
            n.append(k)
    return n
