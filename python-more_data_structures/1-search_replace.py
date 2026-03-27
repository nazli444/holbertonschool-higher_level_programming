#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for k in my_list:
        n = []
        if k == search:
            n.append(replace)
        else:
            n.append(search)
    return n
