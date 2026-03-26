#!/usr/bin/python3
from add_0 import add
if __name__ == "__main__":
    """a:first integer"""
    a = 1
    """b:second integer"""
    b = 2
    """print the value"""
    print("{} + {} = {}".format(a, b, add(a, b)))
