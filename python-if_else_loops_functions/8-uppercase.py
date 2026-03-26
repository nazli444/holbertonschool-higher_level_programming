#!/usr/bin/python3
def uppercase(str):
    n = ""
    for k in str:
        if "a" <= k <= "z":
            n = n + chr(ord(k) - 32)
        else:
            n = n + k
    print("{}".format(n))
