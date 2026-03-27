#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n = []
    for k in my_list:
        if k == search:
            n.append(replace)
        else:
            n.append(k)
    return n
