#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n = {}

    for key in a_dictionary:
        value = a_dictionary[key]
        n[key] = value * 2
    return n
