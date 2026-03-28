#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string) or roman_string is None:
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    previous_value = 0
    for k in reversed(roman_string):
        value = roman.get(k, 0)
        if value < previous_value:
            total = total - value
        else:
            total = total + value
        previous_value = value
    return total

