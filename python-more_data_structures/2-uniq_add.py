#!/usr/bin/python3
def uniq_add(my_list=[]):
    n = []
    r = 0
    for k in my_list:
        if n.count(k) == 0:
            n.append(k)
    for i in n:
        r = r + i
    return r
