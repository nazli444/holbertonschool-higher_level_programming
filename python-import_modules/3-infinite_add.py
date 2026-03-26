#!/usr/bin/python3
import sys
if __name__ == "__main__":
    k = 0
    for n in range(1, len(sys.argv)):
        k = k + int(sys.argv[n])
    print("{}".format(k))
