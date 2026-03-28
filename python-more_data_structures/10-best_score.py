#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_key = None
    max_value = None
    for key in a_dictionary:
        if max_value = None or a_dictionary[key] > max_value:
            max_value = a_dictionary[key]
            best_key = key
    return best_key
