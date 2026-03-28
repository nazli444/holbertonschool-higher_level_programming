#!/usr/bin/python3
def safe_print_division(a, b):
    resurlt = None
    try:
        result = a / b
    except ZeroDivisonError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
